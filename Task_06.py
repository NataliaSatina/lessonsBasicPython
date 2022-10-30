# Задача 6
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.
import random 

my_favorite_songs = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02
}

myList=list()
for i in range(3):
    myList.append(tuple(my_favorite_songs.items())[random.randint(0,8)])
print(myList)
print("Три песни звучат " + str(round(sum(n[1] for n in myList),2)) + " минут.")

# Как и в задании 4
time = 0
for song in sample(tuple(my_favorite_songs), 3):
    print(song)
    time += my_favorite_songs[song]

print(f'Три песни звучат {round(time, 2)}')
