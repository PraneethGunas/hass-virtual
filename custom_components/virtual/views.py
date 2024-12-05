import logging
import yaml
import aiofiles
from homeassistant.components.http import HomeAssistantView
from homeassistant.core import HomeAssistant
from .const import COMPONENT_DOMAIN, IMPORTED_GROUP_NAME

_LOGGER = logging.getLogger(__name__)

class VirtualEntityAddView(HomeAssistantView):
    url = "/api/virtual/add"
    name = "api:virtual:add"
    requires_auth = True

    async def post(self, request):
        hass: HomeAssistant = request.app["hass"]
        entity_config = await request.json()

        _LOGGER.debug("Adding new virtual entity via API")

        try:
            entity_type = entity_config.get("platform")
            entity_name = entity_config.get("name", "Virtual Light (Simulator)")
            if entity_type == "light":
                await hass.components.virtual.light.async_add_virtual_light(
                    hass, entity_config
                )
                return self.json({"status": "success", "message": f"Virtual light '{entity_name}' added."})
            else:
                return self.json({"status": "error", "message": f"Unsupported entity type '{entity_type}'."})

        except Exception as e:
            _LOGGER.error(f"Failed to initiate config flow for '{entity_name}': {e}")
            return self.json({"status": "error", "message": f"Failed to add '{entity_name}': {str(e)}"})

class AutomationsConfigView(HomeAssistantView):
    url = "/api/virtual/automations/config"
    name = "api:virtual:automations:config"
    requires_auth = True

    async def get(self, request):
        hass = request.app["hass"]
        file_path = hass.config.path("automations.yaml")
        try:
            async with aiofiles.open(file_path, "r") as file:
                content = await file.read()
                automations = yaml.safe_load(content)
            return self.json(automations)
        except Exception as e:
            return self.json({"error": str(e)}, status=500)