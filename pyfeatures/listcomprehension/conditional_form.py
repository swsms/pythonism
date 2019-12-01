numbers = [x for x in range(10) if x % 2 == 0]
print(numbers)  # [0, 2, 4, 6, 8]

movie_genres = ['action', 'comedy', 'drama', 'sci-fi', 'thriller']
genres_with_a = [genre for genre in movie_genres if 'a' in genre]
print(genres_with_a)  # ['action', 'drama']
