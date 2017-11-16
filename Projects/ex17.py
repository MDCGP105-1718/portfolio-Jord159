class Fraction(object):
  def __init__(self, num, denom):
    self.num = int(num)
    self.denom = int(denom)

  def __add__(self, other):
    return Fraction(self.num * other.denom + other.num * self.denom, self.denom * other.denom)

  def __sub__(self, other):
    return Fraction(self.num * other.denom - other.num * self.denom, self.denom * other.denom)

  def __mul__(self, other):
    return Fraction(self.num * other.num, self.denom * other.denom)

  def __truediv__(self, other):
    return Fraction(self.num * other.denom, self.denom * other.num)

  def inverse(self):
    temp = self.num
    self.num = self.denom
    self.denom = temp
    return str(self.num) + "/" + str(self.denom)

  def __str__(self):
    return str(self.num) + "/" + str(self.denom)

Frac1 = Fraction(input(), input())
Frac2 = Fraction(input(), input())

print(Frac1)
print(Frac2)
print(Frac1 + Frac2)
print(Frac1 - Frac2)
print(Frac1 * Frac2)
print(Frac1 / Frac2)
print(Frac1.inverse())
print(Frac2.inverse())
