import time
from unittest import TestCase

from movie_api import get_movie_title_and_show_times


class TestMovieApi(TestCase):
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

    def test_mean_girls_show_times_performance(self):
        start = time.time()
        get_movie_title_and_show_times(377092)
        end = time.time() - start

        self.assertLess(end, 1)

    def test_all_movies_and_times(self):
        response = {}
        # TODO: somehow get all movie titles and show times

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
