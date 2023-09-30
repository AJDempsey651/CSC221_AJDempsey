
def numbers(a, b = 3.14):
    numbers_list = [a, b]
    print(a + b)
    x = sorted(numbers_list)
    print(x)
numbers(5)

def numbers2(a, b = 3.14, verbose = False):
    if verbose == True:
      numbers_list = [a, b]
      print(a + b)
      x = sorted(numbers_list)
      print(x)
numbers2(5)


if __name__=='__main__':
   b = 3.14
   numbers(6, b)
   numbers2(5, b, verbose = True)