import logging
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
