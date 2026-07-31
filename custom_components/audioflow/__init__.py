"""AudioFlow integration."""

from .coordinator import AudioFlowCoordinator


async def async_setup_entry(hass, entry):

    coordinator = AudioFlowCoordinator(
        hass,
        entry.data["host"],
    )

    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault("audioflow", {})
    hass.data["audioflow"][entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(
        entry,
        ["switch"],
    )

    return True


async def async_unload_entry(hass, entry):

    await hass.config_entries.async_unload_platforms(
        entry,
        ["switch"],
    )

    hass.data["audioflow"].pop(entry.entry_id)

    return True
