# Napisz skrypt, w którym tworzysz listę ulubionych sportów, odwróć ją a następnie dodaj mniej lubiane sporty na koniec

sports = ['piłka nożna', 'siatkówka', 'koszykówka']
print("Lista, stan początkowy:", sports)
sports.reverse()
print("Lista, stan po odwróceniu:", sports)
sports.append('hokej')
sports.append('lekkoatletyka')
sports.append('tenis')
print("Lista, stan po dodaniu mniej lubianych sportów:", sports)
