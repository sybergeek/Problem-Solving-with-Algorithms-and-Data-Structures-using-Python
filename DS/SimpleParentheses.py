# Problem 2
# Write an algorithm that will read a string of parentheses from left to right and decide whether the symbols are balanced.

from stack import Stack

def isBalanced(symbols):
	balanced=True
	checker = Stack()
	for symbol in symbols:
		if symbol == '(':
			checker.push(symbol)
		elif symbol == ')':
			if checker.isEmpty():
				balanced = False
				break
			else:
				checker.pop()
	if not checker.isEmpty():
	    balanced = False
	return balanced

print(isBalanced("(())(())"))
