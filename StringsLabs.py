"""
title: StringsLabs
author: Kaly
date: 2019-06-13 09:58
"""


# def short_hand(short):
#     short = short.lower().replace("and","&").replace("you","U").replace("for","4").replace("too","2")
#     short = short.replace("a","").replace("e","").replace("i","").replace("o","").replace("u","")
#     return short
#
#
# print(short_hand("Thank you for that! You are too sweet and kind!"))
inp = input("Enter a phrase")
# print(short_hand(inp))


def removing(check):
    check = check.replace(",", "").replace(' ', "").replace("'", "").replace(";", '').replace("?", "").replace('!', '')\
        .replace(".", '')
    return check


print(removing(inp))


def palindrome(check):
    check = removing(check)
    return check == check[::-1]


print(palindrome("Madam, I'm Adam"))
print(palindrome("computer"))