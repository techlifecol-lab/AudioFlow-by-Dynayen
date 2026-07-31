"""Switch platform for AudioFlow."""

from homeassistant.components.switch import SwitchEntity

from .const import DOMAIN


async def async_setup_entry(hass, entry, async_add_entities):

    coordinator = hass.data[DOMAIN][entry.entry_id]

    entities = []

    # El AudioFlow tiene 4 zonas
    for zone in range(1, 5):
        entities.append(AudioFlowSwitch(coordinator, zone))

    async_add_entities(entities)


class AudioFlowSwitch(SwitchEntity):

    def __init__(self, coordinator, zone):

        self.coordinator = coordinator
        self.zone = zone

        self._attr_name = f"Zona {zone}"

        self._attr_unique_id = f"audioflow_zone_{zone}"

    @property
    def is_on(self):

        data = self.coordinator.data

        if not data:
            return False

        for z in data["zones"]:
            if z["id"] == self.zone:
                return z["state"] == "on"

        return False

    async def async_turn_on(self, **kwargs):

        await self.coordinator.api.set_zone(self.zone, True)

        await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs):

        await self.coordinator.api.set_zone(self.zone, False)

        await self.coordinator.async_request_refresh()

    async def async_update(self):

        await self.coordinator.async_request_refresh()
