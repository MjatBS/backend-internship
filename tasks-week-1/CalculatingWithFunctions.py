def zero(*args): 
	return number(0, *args)
def one(*args): 
	return number(1, *args)
def two(*args): 
	return number(2, *args)
def three(*args): 
	return number(3, *args)
def four(*args):
	return number(4, *args)
def five(*args):
	return number(5, *args)
def six(*args):
	return number(6, *args)
def seven(*args):
	return number(7, *args)
def eight(*args):
	return number(8, *args)
def nine(*args):
	return number(9, *args)

def plus(num):
	return (lambda x, y: x + y), num
def minus(num):
	return (lambda x, y: x - y), num
def times(num):
	return (lambda x, y: x * y), num
def divided_by(num):
	return (lambda x, y: x // y), num

def number(num, *args):
	if len(args) == 0:
		return num
	else:
		action = args[0]
		fun = action[0]
		second_num = action[1]
		return fun(num, second_num)