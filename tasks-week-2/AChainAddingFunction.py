class int_add(int):
   def __call__(self, integer):
      return int_add(self + integer)


def add(integer):
   return(int_add(integer))