# task 1 Strings:
def len_str(a: str) -> int:
    """
    Function for get len of string
    :param a: string
    :return: integer
    """
    return len(a)


def add_str(a: str, b: str) -> str:
    """
    Function for concatenating two strings
    :param a: string
    :param b: string
    :return: string
    """
    return a + b


# task 2 Int/Float:
def square_num(a):
    """
    Function for calculating the square of a number
    :param a: integer or float
    :return: integer or float
    """
    return a**2


def add_num(a, b):
    """
    Function for calculating the sum of two numbers
    :param a: integer or float
    :param b: integer or float
    :return: integer or float
    """
    return a + b


def div_num(a: int, b: int):
    """
    Function returns the integer part and the remainder of the division of two numbers
    :param a: integer
    :param b: integer
    :return: integer, integer
    """
    if b == 0:
        print('division is impossible')
        return 0, 0
    else:
        return a//b, a % b


# task 3 Lists:
def mean_list(a: list) -> float:
    """
    Function to calculate the average value of a list of numbers
    :param a: list
    :return: float
    """
    return float(sum(a)/len(a))


def concat_list(a: list, b: list) -> list:
    """
    Function returns a list that contains the common elements two lists
    :param a: list
    :param b: list
    :return: list
    """
    return list(set(a) & set(b))


# task 4 Dictionaries:
def key_dict(a: dict):
    """
    Function returns the dictionary keys
    :param a: dictionary
    :return: object dict_keys
    """
    return a.keys()


def concat_dict(a: dict, b: dict) -> dict:
    """
    Function returns a dictionary that is the concatenating two dictionaries
    :param a: dictionary
    :param b: dictionary
    :return: dictionary
    """
    a.update(b)
    return a


# task 5 Sets:
def concat_sets(a: set, b: set) -> set:
    """
    Function returns a set that is the concatenating two sets
    :param a: set
    :param b: set
    :return: set
    """
    return a | b


def sub_set(a: set, b: set) -> bool:
    """
    Function checks whether one set is a subset of another
    :param a: set
    :param b: set
    :return: bool
    """
    return a.issubset(b)


#  task 6 Conditional expressions and cycles:
def even_num(a: int) -> str:
    """
    Function checks whether the input number is even
    :param a: integer
    :return: string
    """
    if a % 2 == 0:
        return "number is even"
    else:
        return "number is odd"


def even_cycle(a: list) -> list:
    """
    Function returns a list containing even numbers
    :param a: list
    :return:  list
    """
    b = []
    for el in a:
        if el % 2 == 0:
            b.append(el)
    return b


res_1a = len_str('test')
res_1b = add_str('test', 'test')
res_2a = square_num(3)
res_2b = add_num(4, 7)
res_2c, res_2cc = div_num(5, 1)
res_3a = mean_list([1, 2, 3, 4, 5])
res_3b = concat_list([1, 2, 3], [2, 3, 4, 5, 6])
res_4a = key_dict({'a': '1', 'b': '2', 'c': '3'})
res_4b = concat_dict({'a': '1', 'b': '2', 'c': '3'}, {'d': '4', 'f': '5'})
res_5a = concat_sets({2, 3, 4}, {6, 7, 8, 9})
res_5b = sub_set({2, 3, 4}, {2, 3, 4, 9})
res_6a = even_num(5)
res_6b = even_cycle([4, 5, 5, 6, 7, 6])

print('1.a len of string', res_1a)
print('1.b concatenating two strings', res_1b)

print('2.a square of a number', res_2a)
print('2.b sum of two numbers', res_2b)
print('2.c integer part', res_2c, 'the remainder', res_2cc)

print('3.a average value of a list of numbers', res_3a)
print('3.b common elements two lists', res_3b)

print('4.a dictionary keys', list(res_4a))
print('4 b concatenating two dictionaries', res_4b)

print('5.a concatenating two sets', res_5a)
print('5.b a is b subset', res_5b)

print('6.a', res_6a)
print('6.b list containing even numbers', res_6b)