from random import randint
from time import sleep
from typing import Union

from fastapi import FastAPI, HTTPException

from app.movie_database import movie_database, week_days

app = FastAPI()


@app.get('/show-time/{movie_id}/{day}/')
def movie_time(movie_id: int, day: int, q: Union[str, None] = None):
    sleep(0.3)

    if q is not None and randint(1, 7) == 7:
        raise HTTPException(status_code=500, detail='Oops, something went wrong...')

    if movie_id not in movie_database:
        raise HTTPException(status_code=404, detail='Movie not found')

    movie = movie_database[movie_id]
    day_name = week_days[day % 7]
    return {day_name: movie['show_times'][day % 7]}


@app.get('/movie-title/{movie_id}/')
def movie_title(movie_id: int, q: Union[str, None] = None):
    sleep(0.3)

    if q is not None and randint(1, 7) == 7:
        raise HTTPException(status_code=500, detail='Oops, something went wrong...')

    if movie_id not in movie_database:
        raise HTTPException(status_code=404, detail='Movie not found')

    movie = movie_database[movie_id]
    return {'title': movie['title']}
