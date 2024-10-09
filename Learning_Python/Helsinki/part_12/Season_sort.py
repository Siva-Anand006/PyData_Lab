# Please write a function named sort_by_seasons(items: list) which takes a list of dictionaries as its argument. Each dictionary contains the information of a single TV show. The function should sort this list by the number of seasons each show has, in ascending order. The function should not change the original list, but return a new list instead.


#so i can do this with and without a lambda function

def get_season(show : dict):
    return show["seasons"]

def sort_by_seasons(shows):
    list1 = sorted(shows, key = get_season)
    return list1

def sort_by_seasons1(shows):
    return sorted(shows, key = lambda x :  x["seasons"] )

shows = [
    {"name": "Dexter", "rating": 8.6, "seasons": 9},
    {"name": "Friends", "rating": 8.9, "seasons": 10},
    {"name": "Simpsons", "rating": 8.7, "seasons": 32}
]

for show in sort_by_seasons1(shows):
    print(f"{show['name']} {show['seasons']} seasons")
    
for show in sort_by_seasons(shows):
    print(f"{show['name']} {show['seasons']} seasons")
