def append(list1, list2):
    return list1.append(list2)


def concat(lists):
    return lists.concat()


def filter(function, list):
    return function(list)


def length(list):
    return len(list)


def map(function, list):
    return function(list)


def foldl(function, list, initial):
    return function(list, initial)


def foldr(function, list, initial):
    return function(list, initial)


def reverse(list):
    return list.reverse()
