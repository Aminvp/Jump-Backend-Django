import asyncio
import httpx

async def fetch(url, client):
    # TODO return url and response.text
    response = await client.get(url)
    return url, response.text

async def fetch_all(urls):
    async with httpx.AsyncClient() as client:
        # TODO implement the logic here
        # return a dict of url and content
        tasks = [fetch(url, client) for url in urls]
        results = await asyncio.gather(*tasks)
        return {url: content for url, content in results}
