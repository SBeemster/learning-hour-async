import time
from unittest import IsolatedAsyncioTestCase

from movie_api import get_movie_title_and_show_times, get_movie_title, get_movie_show_times, \
    get_movie_title_and_show_times_async, get_multiple_movies


class TestMovieApi(IsolatedAsyncioTestCase):
    def test_mean_girls_show_times(self):
        response = get_movie_title_and_show_times(377092)
        self.assertEqual(
            response,
            {
                'title': 'Mean Girls',
                'monday': '14:00',
                'tuesday': '13:00',
                'wednesday': '17:00',
                'thursday': '22:00',
                'friday': '15:00',
                'saturday': '18:00',
                'sunday': '16:00',
            }
        )

    async def test_mean_girls_show_times_async(self):
        response = await get_movie_title_and_show_times_async(377092)
        self.assertEqual(
            response,
            {
                'title': 'Mean Girls',
                'monday': '14:00',
                'tuesday': '13:00',
                'wednesday': '17:00',
                'thursday': '22:00',
                'friday': '15:00',
                'saturday': '18:00',
                'sunday': '16:00',
            }
        )

    def test_mean_girls_show_times_performance(self):
        start = time.time()
        get_movie_title_and_show_times(377092)
        end = time.time() - start

        self.assertLess(end, 1)

    async def test_mean_girls_show_times_async_performance(self):
        start = time.time()
        await get_movie_title_and_show_times_async(377092)
        end = time.time() - start

        self.assertLess(end, 1)

    def test_get_title_of_movie(self):
        response = get_movie_title_and_show_times(88247)

        self.assertEqual(
            "The Terminator",
            response['title']
        )

    async def test_get_movie_title(self):
        response = await get_movie_title(88247)

        self.assertEqual(
            "The Terminator",
            response['title']
        )

    async def test_get_movie_show_times(self):
        show_times = await get_movie_show_times(88247)
        self.assertEqual(
            {'monday': '22:00',
             'tuesday': '10:00',
             'wednesday': '18:00',
             'thursday': '16:00',
             'friday': '10:00',
             'saturday': '13:00',
             'sunday': '21:00'
             },
            show_times
        )

    async def test_all_movies_and_times(self):
        response = await get_multiple_movies({
            # 10954600, 338526, 120347, 6710474, 120737, 88763, 78748, 120735, 88247, 377092
            10954600
        })
        self.assertEqual(
            response,
            {
                10954600: {
                    'title': 'Ant-Man and the Wasp: Quantumania',
                    'monday': '20:00',
                    'tuesday': '15:00',
                    'wednesday': '22:00',
                    'thursday': '10:00',
                    'friday': '22:00',
                    'saturday': '11:00',
                    'sunday': '16:00'
                },
                338526: {
                    'title': 'Van Helsing',
                    'monday': '17:00',
                    'tuesday': '12:00',
                    'wednesday': '20:00',
                    'thursday': '17:00',
                    'friday': '14:00',
                    'saturday': '22:00',
                    'sunday': '13:00'
                },
                120347: {
                    'title': 'Tomorrow Never Dies',
                    'monday': '13:00',
                    'tuesday': '17:00',
                    'wednesday': '20:00',
                    'thursday': '19:00',
                    'friday': '12:00',
                    'saturday': '22:00',
                    'sunday': '13:00'
                },
                6710474: {
                    'title': 'Everything Everywhere All at Once',
                    'monday': '17:00',
                    'tuesday': '16:00',
                    'wednesday': '13:00',
                    'thursday': '12:00',
                    'friday': '12:00',
                    'saturday': '10:00',
                    'sunday': '17:00'
                },
                120737: {
                    'title': 'The Lord of the Rings: The Fellowship of the Ring',
                    'monday': '19:00',
                    'tuesday': '20:00',
                    'wednesday': '13:00',
                    'thursday': '22:00',
                    'friday': '12:00',
                    'saturday': '15:00',
                    'sunday': '13:00'
                },
                88763: {
                    'title': 'Back to the Future',
                    'monday': '17:00',
                    'tuesday': '12:00',
                    'wednesday': '14:00',
                    'thursday': '11:00',
                    'friday': '13:00',
                    'saturday': '21:00',
                    'sunday': '15:00'
                },
                78748: {
                    'title': 'Alien',
                    'monday': '17:00',
                    'tuesday': '15:00',
                    'wednesday': '10:00',
                    'thursday': '22:00',
                    'friday': '21:00',
                    'saturday': '12:00',
                    'sunday': '14:00'
                },
                120735: {
                    'title': 'Lock, Stock and Two Smoking Barrels',
                    'monday': '15:00',
                    'tuesday': '14:00',
                    'wednesday': '13:00',
                    'thursday': '12:00',
                    'friday': '16:00',
                    'saturday': '12:00',
                    'sunday': '14:00'
                },
                88247: {
                    'title': 'The Terminator',
                    'monday': '22:00',
                    'tuesday': '10:00',
                    'wednesday': '18:00',
                    'thursday': '16:00',
                    'friday': '10:00',
                    'saturday': '13:00',
                    'sunday': '21:00'
                },
                377092: {
                    'title': 'Mean Girls',
                    'monday': '14:00',
                    'tuesday': '13:00',
                    'wednesday': '17:00',
                    'thursday': '22:00',
                    'friday': '15:00',
                    'saturday': '18:00',
                    'sunday': '16:00'
                }
            }
        )
