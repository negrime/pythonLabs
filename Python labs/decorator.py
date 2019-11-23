import random
# 7)Создать декоратор, который проверяет, что возвращаемое функцией число - целое. Если нет, то оно округляется до сотых.


def decorator(a_function_to_decorate):
    def the_wrapper_around_the_original_function():
        num = a_function_to_decorate()
        print("Generated num: " + str(num))
        if not type(num) is int:
            return round(num, 2)
        else:
            return num

    return the_wrapper_around_the_original_function


@decorator
def random_num():
    if random.random() < .5:
        return random.randint(1, 10)
    else:
        return random.uniform(1, 10)


print(random_num())
