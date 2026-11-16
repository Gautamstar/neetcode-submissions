def remove_fourth_character(word: str) -> str:
    beforeFourth = word[:3]
    afterFourth = word[4:]
    return beforeFourth + afterFourth


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
