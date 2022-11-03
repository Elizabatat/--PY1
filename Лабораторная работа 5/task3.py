import random
def get_unique_list_numbers() -> list[int]:
    a = []
    for i in range(-10,10):
        a.append(i)
    list = random.sample(a, 15)
    return list

   # TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
