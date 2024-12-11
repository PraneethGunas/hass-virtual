# Home Assistant Virtual Integration (hass-virtual)

The **hass-virtual** integration provides virtual devices that can be controlled and automated in Home Assistant. This is particularly useful for testing automations and configurations without needing physical devices.

---

## Features
- Create virtual sensors, switches, binary sensors, and more.
- Fully customizable states for testing automations.
- Lightweight and easy to set up.

---

## Prerequisites
- Home Assistant Core version 2021.3.0 or later.
- Knowledge of YAML configuration for Home Assistant.
- A working installation of Home Assistant.

---

## Installation

### Option 1: Manual Installation
1. **Download the integration**:
   - Visit the [hass-virtual GitHub repository](https://github.com/twrecked/hass-virtual) and download the ZIP file for the repository or clone it:
     ```bash
     git clone https://github.com/twrecked/hass-virtual.git
     ```

2. **Copy files**:
   - Extract the contents of the repository to your Home Assistant `custom_components` directory. The folder structure should look like this:
     ```
     config/
       custom_components/
         virtual/
           __init__.py
           manifest.json
           sensor.py
           ...
     ```

3. **Restart Home Assistant**:
   - Restart Home Assistant to recognize the new custom component.

---

## Configuration

1. **Enable the integration**:
   - Add the following configuration to your `configuration.yaml` file to define a virtual entity (e.g., sensor):
     ```yaml
     virtual:
       entities:
         - name: Test Virtual Sensor
           type: sensor
           initial_state: 0
           unit_of_measurement: "°C"
     ```

2. **Validate Configuration**:
   - Ensure your YAML configuration is valid using the "Check Configuration" button in Home Assistant.

3. **Reload the Integration**:
   - After saving changes to `configuration.yaml`, restart Home Assistant or reload the YAML configuration.

---

## Usage
- After installation, virtual entities will appear in Home Assistant under "Entities."
- Use the entities in automations, scripts, or dashboards for testing.

---

## Troubleshooting
- If the integration does not load, check the Home Assistant logs (`Settings > System > Logs`) for errors.
- Ensure the file structure and permissions for the `custom_components` directory are correct.

---

## Credits
Developed by [trecked](https://github.com/twrecked) and modified by [Praneeth](https://github.com/PraneethGunas). For more details, visit the official [hass-virtual GitHub repository](https://github.com/twrecked/hass-virtual).
