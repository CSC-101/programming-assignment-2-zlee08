from unittest.util import sorted_list_difference

import data
from data import Rectangle, Point, Duration
city_links = [['san luis obispo', 'santa margarita'],['san luis obispo', 'pismo beach'],['atascadero', 'santa margarita'],['atascadero', 'creston']]

# Write your functions for each part in the space below.

# Part 1
def create_rectangle(point1: Point, point2: Point):
    min_x = min(point1.x, point2.x)
    max_x = max(point1.x, point2.x)
    max_y = max(point1.y, point2.y)
    min_y = min(point1.y, point2.y)
    top_left = Point(min_x, max_y)
    bottom_right = Point(max_x, min_y)
    return Rectangle(top_left, bottom_right)

# Part 2
def shorter_duration_than(d1,d2):
    d1_total = d1.minutes*60 + d1.seconds
    d2_total = d2.minutes*60 + d2.seconds
    if d1_total < d2_total:
        return True
    else:
        return False

# Part 3
def songs_shorter_than(songs: list[data.Song], max_duration: Duration) -> list[data.Song]:
    return [song for song in songs if song.duration.seconds < max_duration.seconds]

# Part 4
def duration_sum(d0,d1):
    tot_minutes = d0.minutes + d1.minutes + ((d0.seconds + d1.seconds)//60)
    tot_seconds = (d0.seconds + d1.seconds) % 60
    return tot_minutes, tot_seconds

def running_time(my_list,pos):
    s = [my_list[x] for x in pos]
    tot = Duration(0,0)
    for x in s:
        tot=duration_sum(tot,x.duration)

# Part 5
def sort_list(my_list):
    sorted_list = [x for x in my_list if x.sort()!=""]
    return sorted_list

def validate_route(my_list1, my_list2):
    my_list1 = city_links
    y = sort_list(my_list1)
    i = 0
    if len(my_list2)<=1:
        return True
    else:
        valid = True
        travel_list=[]
        while i < len(my_list2)-1:
            travel_list.append(sorted([my_list2[i],my_list2[i+1]]))
            i = i+1
        for z in travel_list:
            if not z in y:
                valid = False
            return valid

# Part 6
def longest_repetition(my_list):
    result="None"
    integers = []
    idx = -1
    max = 1
    while my_list:
        integers.append(my_list.pop(0))
        count = 1
        idx = idx + 1
        current_index = idx
        while my_list != [] and integers[-1] == my_list[0]:
            my_list.pop(0)
            count = count + 1
            idx = idx + 1
            if count > max:
                result = current_index
                max = count
        return result
