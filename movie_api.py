import httpx


def get_movie_title_and_show_times(movie_id: int):
    response = httpx.get(f'http://localhost:5555/movie-title/{movie_id}/').json()
    for day in range(7):
        response.update(httpx.get(f'http://localhost:5555/show-time/{movie_id}/{day}/').json())

    return response
