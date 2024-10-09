'''Please write a function named sort_by_ratings(items: list) which takes a list of dictionaries as its argument. The structure of the dictionaries is identical to the previous exercise. This function should sort the dictionaries in descending order based on the shows' ratings. The function should not change the original list, but return a new list instead.'''

def sort_by_ratings(shows):
    return sorted(shows, key = lambda x : x["rating" ], reverse= True)
    
shows = [{ "name": "Dexter", "rating" : 8.6, "seasons":9 }, { "name": "Friends", "rating" : 8.9, "seasons":10 },  { "name": "Simpsons", "rating" : 8.7, "seasons":32 }  ]

print("Rating according to IMDB")
for show in sort_by_ratings(shows):
    print(f"{show['name']}  {show['rating']}")