def append(list1, list2):
    return list1 + list2


def concat(lists):
    concat = []
    for list in lists:
        concat += list
    return concat


def filter(function, lists):
    items = []
    for list in lists:
        if function(list):
            items = concat([items, [list]])

    return items


def length(list):
    return sum(1 for x in list)


def map(function, list):
    return [function(x) for x in list]


def foldl(function, list, initial):
    for x in list:
        initial = function(initial, x)
    return initial


def foldr(function, list, initial):
    for x in list[::-1]:
        initial = function(initial, x)
    return initial


def reverse(list):
    return list[::-1]
