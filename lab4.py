
# # x = ["ser","szynka","jogurt","chleb"]
# print (x)
# print (x[1], x[2])
#
# x[2] = "mleko"
# print(x)
#
# print(x[-1], x[-2])
# print(x[-2:])
import random
n=int(input("Podaj długość listy: "))
zestaw1 = []
for i in range(n):
    k = random.randint(1, 10)
    zestaw1.append(k)
print(zestaw1)

n=int(input("Podaj długość listy: "))
zestaw2 = [random.randint(5, 15) for i in range(n)]
print(zestaw2)

liczba = int(input("podaj liczbę: "))
if liczba in zestaw1:
    print("liczba występuje w zestawie 1")
elif liczba in zestaw2:
    print("liczba wystepuje w zestawie 2")
else:
    print("liczba nie występuje w żadnym zestawie")

zestaw3 =zestaw1+zestaw2
print("poniżej połączone listy 1 i 2")
print(zestaw3)
zestaw3.sort()
print(zestaw3)



