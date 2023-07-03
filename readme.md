# Bromide.py
A typed, sync/async wrapper for the SodiumDB API in Python.

## Quickstart
```python
from bromide import Bromide, AsyncBromide

import asyncio

br = Bromide(password="myAmazingPassword")
br.create({"hello": "world"})
print(br.read("hello")) # "world"

# async client too!

async def main():
    br = AsyncBromide(password="myAmazingPassword")
    await br.create({"hello": "async"})
    print(await br.read("hello")) # "async"

asyncio.run(main())
```