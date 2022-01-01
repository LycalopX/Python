import math
#entrada
a = float(input())
b = float(input())
c = float(input())

delta = b * b - 4 * a * c

if(delta > 0):
  raizdelta = math.sqrt(delta)
  m = -b/2*a
  k = -delta / 4 * a
  

  print ("================================\nA fórmula canônica corresponde à: \nf(x) =", a, "* ( x -", m, ")² +", k, "\n================================")
  #saída