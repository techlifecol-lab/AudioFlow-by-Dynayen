"""AudioFlow REST API."""

from __future__ import annotations

import aiohttp


class AudioFlowApi:
    """AudioFlow API."""

    def __init__(self, host):
        self.host = host.rstrip("/")

    async def get_zones(self):
        """Read all zones."""

        url = f"http://{self.host}/zones"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                return await response.json()

    async def set_zone(self, zone, state):
        """Enable or disable a zone."""

        url = f"http://{self.host}/zones/{zone}"

        value = "1" if state else "0"

        async with aiohttp.ClientSession() as session:
            async with session.put(
                url,
                data=value,
            ) as response:

                response.raise_for_status()

                return await response.json()
