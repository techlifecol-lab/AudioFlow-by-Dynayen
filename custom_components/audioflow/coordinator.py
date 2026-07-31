"""Data coordinator for AudioFlow."""

from datetime import timedelta

from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
)

from .api import AudioFlowApi
from .const import DOMAIN, DEFAULT_SCAN_INTERVAL


class AudioFlowCoordinator(DataUpdateCoordinator):
    """Coordinator para AudioFlow."""

    def __init__(self, hass, host):
        """Inicializa el coordinador."""

        self.api = AudioFlowApi(host)

        super().__init__(
            hass,
            logger=None,
            name=DOMAIN,
            update_interval=timedelta(seconds=DEFAULT_SCAN_INTERVAL),
        )

    async def _async_update_data(self):
        """Obtiene información del AudioFlow."""

        try:
            return await self.api.get_zones()

        except Exception as err:
            raise UpdateFailed(f"Error comunicando con AudioFlow: {err}")
