import asyncio

import httpx


def get_movie_title_and_show_times(movie_id: int):
    response = httpx.get(f'http://localhost:5555/movie-title/{movie_id}/').json()
    for day in range(7):
        response.update(httpx.get(f'http://localhost:5555/show-time/{movie_id}/{day}/').json())

    return response


async def get_movie_title_and_show_times_async(movie_id: int):
    result = await asyncio.gather(*[get_movie_title(movie_id), get_movie_show_times(movie_id)])
    flap = {}
    [flap.update(r) for r in result]
    return flap


async def get_movie_title(movie_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f'http://localhost:5555/movie-title/{movie_id}/')

    return response.json()


async def get_movie_show_times(movie_id: int):
    tasks = []
    async with httpx.AsyncClient() as client:
        for day in range(7):
            tasks.append(client.get(f'http://localhost:5555/show-time/{movie_id}/{day}/'))

        response = await asyncio.gather(*tasks)
        return {list(x.json().keys())[0]: list(x.json().values())[0] for x in response}


async def get_multiple_movies(movie_ids: set[int]):
    async def _sneaky_func(movie_id: int):
        return await get_movie_title_and_show_times_async(movie_id)

    result = {
        movie_id: await asyncio.gather(*[
            _sneaky_func(movie_id)
            for movie_id in movie_ids
        ])
        for movie_id in movie_ids
    }

    return result
