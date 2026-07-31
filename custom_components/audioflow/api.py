"""AudioFlow REST API client."""

import aiohttp


class AudioFlowApi:

    def __init__(self, host):
        self.host = host.rstrip("/")

    async def get_status(self):

        url = f"http://{self.host}/status"

        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=5) as response:

                response.raise_for_status()

                return await response.json()

    async def set_zone_source(self, zone, source):

        url = f"http://{self.host}/zones/{zone}"

        payload = {
            "source": source
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(
                url,
                json=payload,
                timeout=5,
            ) as response:

                response.raise_for_status()

                return await response.json()
