# GLOBAL
namespace = "Global"

def greet():

  # ENCLOSING
  namespace = "Enclosing"

  def hello():
    # LOCAL
    namespace = "Local"

    print('Hello, my ' + namespace + " dude")

  hello()

greet()

x = 50

def func():
  global x
  print(f'X is {x}')

  # LOCAL REASSIGNMENT
  x = 200
  print(f'X has been reassigned to {x}')

func()
print(x)