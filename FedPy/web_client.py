import aiohttp

class ClientSession:
    async def __aenter__(self):
        self._session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, *err):
        await self._session.close()

    async def get(self, url):
        async with self._session.get(url) as resp:
            resp.raise_for_status()
            return await resp.read()
