# Actually what i have to do i do not know
# How the fuck i am suppose to know the stuff that currently out of my hand and mind
# Just check my iq lower than average
# Atleast i deserver to be about 10lpa


def prevSmaller(A):
	stack = []
	res = []
	for el in A:
		if len(stack) == 0:
			res.append(-1)
		elif len(stack):
			while len(stack) and el <= stack[-1]:
			    stack.pop(-1)
			if len(stack) == 0:
			    res.append(-1)
			else:
			    res.append(stack[-1])
		stack.append(el)
	return res

print(prevSmaller([39, 27, 11, 4, 24, 32, 32, 1]))