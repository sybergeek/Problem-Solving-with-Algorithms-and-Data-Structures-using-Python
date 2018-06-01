# Problem 3
# A program to check if opening and closing symbols in your program are balnced or not. 

from Stack import stack

def isBalanced(symbols):
    list=stack()
    balanced=True
    for symbol in symbols:
        if symbol in "{[(<":
            list.push(symbol)
        elif symbol in ")]}>":
            if list.isEmpty():
                balaned=False
                break
            else:
                opening=list.peek()
                closing=symbol
                if match(opening, closing):
                    list.pop()
                else:
                    balanced=False
                    break
    if not list.isEmpty():
        balanced=False
    return balanced

def match(opening, closing):
    opens="{[(<"
    closes="}])>"
    return opens.index(opening) == closes.index(closing)

print(isBalanced("int main()"))
print(isBalanced("#include<iostream>"))
print(isBalanced("std::vector<int> apples;"))
