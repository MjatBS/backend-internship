class str_add(str):
	def __call__(self, *string):
		return self if len(string) == 0 else str_add(self + ' ' + string[0])


def create_message(s):
    return str_add(s)