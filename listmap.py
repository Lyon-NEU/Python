#!/usr/bin/env python
#see
#Function programming with map
def map(func,lst):
	if lst == []:
		return []
	else:
		return [func(lst[0])]+map(func,lst[1:])
def halveElements(lst):
	return map(lambda x:x/2.0,lst)
def main():
	input = [2, 4, 6, 8, 10]
	output = halveElements(input)
	print(output)
if __name__ == '__main__':
	main()