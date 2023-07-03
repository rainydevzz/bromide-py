import requests, aiohttp, typing


class ResultDict(typing.TypedDict):
    result: str | int | list | bool | None


class Bromide:
    def __init__(self, url: str = "http://127.0.0.1:8080", password: str = ""):
        self.url = url
        self.headers = {"Authorization": password, "Content-Type": "application/json"}

    def request(self, data, url_ext):
        r = requests.post(f"{self.url}{url_ext}", headers=self.headers, json=data)
        if r.status_code != 200:
            return None
        else:
            return r.json()

    def read(self, data: str) -> typing.Optional[ResultDict]:
        return self.request({"entry": data}, "/read")

    def create(self, data: dict) -> dict:
        return self.request(data, "/create")

    def delete(self, data: str) -> dict:
        return self.request({"entry": data}, "/delete")


class AsyncBromide:
    def __init__(self, url: str = "http://127.0.0.1:8080", password: str = ""):
        self.url = url
        self.headers = {"Authorization": password, "Content-Type": "application/json"}

    async def request(self, data, url_ext):
        async with aiohttp.ClientSession() as cs:
            async with cs.post(
                f"{self.url}{url_ext}", json=data, headers=self.headers
            ) as resp:
                if resp.status != 200:
                    return None
                else:
                    return await resp.json()

    async def read(self, data: str) -> typing.Optional[ResultDict]:
        return await self.request({"entry": data}, "/read")

    async def create(self, data: dict) -> dict:
        return await self.request(data, "/create")

    async def delete(self, data: str) -> typing.Optional[dict]:
        return await self.request({"entry": data}, "/delete")
