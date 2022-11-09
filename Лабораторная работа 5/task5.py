import random
def get_random_password() -> str:
    # TODO написать функцию генерации случайных паролей
    list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password =''.join(random.sample(list,8))
    return str(password)


print(get_random_password())
