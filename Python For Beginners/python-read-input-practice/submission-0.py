def add_two_numbers() -> int:
    userInp = input()
    listed = userInp.split(",")
    result = list()
    for x in listed:
        result.append(int(x))
    return sum(result)



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
