"""
Создать декоратор, который проверяет, что возвращаемая функцией строка заканчивается на . / ! / ? .
Если нет, то строка дополняется точкой в конце.
"""


def decorator(function_to_decorate):
    def wrapper_around_the_original_function():
        text = function_to_decorate()
        sym = text[-1]
        if sym in ".?!":
            pass
        else:
            text += "."
            print("Sentence does not have any symbol. Point was added!")
        return text

    return wrapper_around_the_original_function


@decorator
def get_string():
    return 123


print(get_string())
