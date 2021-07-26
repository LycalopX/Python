print("Quantos reais deve/na aplicação?")
C = float(input())
print("Qual a taxa de juros?")
i = float(input())
print("Quanto tempo?")
t = float(input())

J = C * (i + 1) ** t

print("Os juros compostos finais serão:", round(J, 2), "reais.")