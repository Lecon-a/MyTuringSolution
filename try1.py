def distinctValues(values) -> list:
    return [x for x in values if values.count(x) == 1]


print(
    f'The sum of all the mono concurrent values is {sum(distinctValues([1, 2, 3, 4, 5, 3, 5]))}')