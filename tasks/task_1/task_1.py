array_1 = ["Alex", "Dima", "Kate", "Galina", "Ivan"]
array_2 = ["Dima", "Ivan", "Kate"]


def find_difference_without_collections(array_one, array_two):
    result_one = [el for el in array_one if el not in array_two]
    result_two = [el for el in array_two if el not in array_one]
    return result_one + result_two


def find_difference_with_collections(array_one, array_two):
    result_one = list(set(array_one).difference(set(array_two)))
    result_two = list(set(array_two).difference(set(array_one)))
    return set(result_one + result_two)


print(find_difference_with_collections(array_2, array_1))
