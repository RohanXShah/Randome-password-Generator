import random
import string
def passgenerate(length):

  allcher=string.ascii_letters+string.digits+string.punctuation
  password = "".join(random.choice(allcher) for i in range(length))

  return password


passwordorg = passgenerate(10)
print(f"Your password is {passwordorg}")