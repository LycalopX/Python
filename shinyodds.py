import math
encontros = float(input())
método = input()
#entrada

if método.isnumeric() == True:
  print("Isso é um número :/")

#As chances específicas:
rawMasudaCombo = 100 * (1 - ((511 / 512) ** encontros))
masudaCombo = round(rawMasudaCombo, 2)

rawFishChain = 100 * (1- ((119/120) ** encontros))
fishChain = round(rawFishChain, 2)

rawSoftReset = 100 * (1 - ((4095/4096) ** encontros))
softReset = round(rawSoftReset, 2)

rawOgSoftReset = 100 * (1 - ((8191/8192) ** encontros))
ogSoftReset = round(rawOgSoftReset, 2)


if método == "masuda":
  print("A chance de conseguir o pokémon é", masudaCombo, "%")
  #saída
if método == "combo" or método == "catch combo":
  print("A chance de conseguir o pokémon é", masudaCombo, "%")
  #saída
if método == "fishchain" or método == "fish" or método == "fishrod":
  print("A chance de conseguir o pokémon é", fishChain, "%")
  #saída
if método == "softreset" or método == "sr" or método == "reset":
  print("A chance de conseguir o pokémon é", softReset, "%")
  #saída
if método == "og softreset" or método == "osr" or método == "old reset" or método == "og reset":
  print("A chance de conseguir o pokémon é", ogSoftReset, "%")
  #saída
