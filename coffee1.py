
a = int(input("Write how many ml of water the coffee machine has:"))

b = int(input("Write how many ml of milk the coffee machine has:"))

c = int(input("Write how many grams of coffee beans the coffee machine has:"))

d = int(input("Write how many cups of coffee you will need:"))

a1 = a//200

b1 = b//50

c1 = c//15

cups = min(a1,b1,c1)
cupsout = str(cups)
if cups == d:
    print("Yes, I can make that amount of coffee")
elif cups < d:
    print("No, I can make only"+" "+cupsout+" "+"cups of coffee")
elif cups > d:
    cupsmore = cups-d
    cupsmoreout = str(cupsmore)
    print("Yes, I can make that amount of coffee (and even"+" "+cupsmoreout+" "+"more than that)")
