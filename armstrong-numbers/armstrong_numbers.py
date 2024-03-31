def is_armstrong(number):
    num_to_str = str(number)
    sum = 0
    for alghar in num_to_str:
        sum += int(alghar) ** len(num_to_str)

    return sum == number


print(is_armstrong(153))