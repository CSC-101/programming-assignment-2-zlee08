from cgitb import reset
from unittest import expectedFailure

import data
import hw2
import unittest
city_links = [['san luis obispo', 'santa margarita'],['san luis obispo', 'pismo beach'],['atascadero', 'santa margarita'],['atascadero', 'creston']]
from data import Rectangle, Point, Duration
from hw2 import shorter_duration_than


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle1(self):
        p1 = Point (2,2)
        p2 = Point(10,10)
        result = hw2.create_rectangle(p1, p2)
        expected = (Point(2,10), Point(10,2))
        self.assertEqual(result,expected)

    def test_create_rectangle2(self):
        p1 = Point (10,10)
        p2 = Point(2,2)
        result = hw2.create_rectangle(p1,p2)
        expected = (Point(2,10), Point(10,2))
        self.assertEqual(result,expected)

    # Part 2
    def test_shorter_duration_than1(self):
        d1 = Duration(1,30)
        d2 = Duration(2,25)
        result = hw2.shorter_duration_than(d1, d2)
        expected = True
        self.assertEqual(result, expected)

    def test_shorter_duration_than2(self):
        d1 = Duration(2,25)
        d2 = Duration(1,30)
        result = hw2.shorter_duration_than(d1, d2)
        expected = False
        self.assertEqual(result, expected)

    # Part 3
    def test_songs_shorter_than1(self):
        song_list = [data.Song('its_my_life', Duration(3, 20)), data.Song('Cal_Poly', Duration(3, 11))]
        durs = Duration(3,11)
        result = hw2.songs_shorter_than(song_list,durs)
        expected = [data.Song('Cal_Poly', Duration(3, 11))]
        self.assertEqual(result,expected)

    def test_songs_shorter_than2(self):
        song_list = [data.Song('baby_shark', Duration(4,32)), data.Song('Ryan_Reynolds', Duration(2,40))]
        durs = Duration(2,40)
        result = hw2.songs_shorter_than(song_list,durs)
        expected = [data.Song('Ryan_Reynolds', Duration(2,40))]
        self.assertEqual(result, expected)

    # Part 4
    def test_running_time1(self):
        song_list = [('its_my_life', Duration(2, 42)), ('freedom', Duration(3, 11))]
        pos = [0,1]
        result = hw2.running_time(song_list, pos)
        expected = Duration(5,53)
        self.assertEqual(result, expected)

    def test_running_time2(self):
        song_list = [('baby_shark', Duration(4, 32)), ('Ryan_Reynolds', Duration(2, 40))]
        pos=[0,1,0]
        result = hw2.running_time(song_list,pos)
        expected = Duration(11,44)
        self.assertEqual(result, expected)

    # Part 5
    def test_validate_route1(self):
        route1 = ['san luis obispo', 'santa margarita']
        route2 = ['atascadero', 'santa margarita']
        result = hw2.validate_route(route1, route2)
        expected = True
        self.assertEqual(result, expected)

    def test_validate_route2(self):
        route1 = ['San Luis Obispo','los angeles']
        route2 = ['san luis obispo', 'pismo beach']
        result = hw2.validate_route(route1, route2)
        expected = False
        self.assertEqual(result, expected)

    # Part 6
    def test_longest_repetition1(self):
        list1 = [1, 1, 2, 2, 1, 1, 1, 3, 3]
        result = hw2.longest_repetition(list1)
        expected = 4
        self.assertEqual(result, expected)

    def test_longest_repetition2(self):
        list1 = [1,2,2,2,2,2,3,3,3,3,3,3,3,3,4,4]
        result = hw2.longest_repetition(list1)
        expected = 6
        self.assertEqual(result, expected)




if __name__ == '__main__':
    unittest.main()
