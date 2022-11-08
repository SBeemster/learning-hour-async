import asyncio
import time

import httpx


def do_sync_stuff():
    start = time.time()

    responses = [httpx.get('http://localhost:5555/') for _ in range(7)]

    print([res.json() for res in responses])
    print(time.time() - start)


movie_ids = {
    10954600,
    338526,
    120347,
    6710474,
    120737,
    88763,
    78748,
    120735,
    88247,
    377092,
}


async def do_async_stuff():
    start = time.time()


    async with httpx.AsyncClient() as client:
        tasks = []
        for movie_id in movie_ids:
            tasks.append(client.get(f'http://localhost:5555/movie-title/{movie_id}/'))
            for day in range(7):
                tasks.append(client.get(f'http://localhost:5555/show-time/{movie_id}/{day}/'))
        responses = await asyncio.gather(*tasks)

    print([res.json() for res in responses])
    print(time.time() - start)


if __name__ == '__main__':
    # do_sync_stuff()
    asyncio.run(do_async_stuff())
    # start = time.time()
    # ress = [httpx.get(f'http://localhost:5555/show-time/377092/{day}/') for day in range(7)]
    # print([res.json() for res in ress])
    # print(time.time() - start)
