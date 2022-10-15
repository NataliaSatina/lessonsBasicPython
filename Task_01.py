# Задача 1
# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.


print(my_favorite_songs[0:my_favorite_songs.find(",")])
print(my_favorite_songs[my_favorite_songs.rfind(",")+2:])
print(my_favorite_songs[my_favorite_songs.find(",")+2:][0:my_favorite_songs[my_favorite_songs.find(",")+2:].find(",")])
print(my_favorite_songs[0:my_favorite_songs.rfind(",")][my_favorite_songs[0:my_favorite_songs.rfind(",")].rfind(",")+2:])
