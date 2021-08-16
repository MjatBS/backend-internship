class StrAdd(str):
	def __call__(self, *string):
		return self if len(string) == 0 else StrAdd(self + ' ' + string[0])


def create_message(s):
    return StrAdd(s)