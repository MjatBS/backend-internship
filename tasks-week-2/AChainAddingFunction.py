class IntAdd(int):
   def __call__(self, integer):
      return IntAdd(self + integer)


def add(integer):
   return(IntAdd(integer))