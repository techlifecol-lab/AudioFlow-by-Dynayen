"""API for AudioFlow."""

from __future__ import annotations

import aiohttp


class AudioFlowApi:
    """AudioFlow API client."""

    def __init__(self, host: str):
        self.host = host

    async def get(self, endpoint: str):
        """Execute GET request."""
        url = f"http://{self.host}/{endpoint}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                return await response.json()

    async def get_info(self):
        """Read device information."""
        return await self.get("switch")

    async def get_zones(self):
        """Read zones."""
        return await self.get("zones")
