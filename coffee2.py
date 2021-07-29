print('''The coffee machine has:
400 of water
540 of milk
120 of coffee beans
9 of disposable cups
550 of money
''')
water = 400
milk = 540
beans = 120
cup = 9
money = 550


def buy(choose):
    global water, milk, beans, cup, money

    if choose == 1:
        water = water - 250
        beans = beans - 16
        money = money +4
        cup = cup-1
    elif choose == 2:
        water = water -350
        milk = milk - 75
        beans = beans -20
        money = money +7
        cup = cup-1
    elif choose == 3:
        water = water - 200
        milk = milk -100
        beans = beans - 12
        money = money + 6
        cup = cup-1

def fill(newwater,newmilk,newbeans,newcups):
    global water, milk, beans, cup, money
    milk = milk + newmilk
    water = water + newwater
    beans = beans + newbeans
    cup = cup + newcups

def mon(action):
    global water, milk, beans, cup, money
    a = str(money)
    print("I gave you $" + a)
    money -=550


action=input("Write action (buy, fill, take):")
if action == "buy":
    choose = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")) 
    buy(choose)
elif action == "fill":
    newwater = int(input("Write how many ml of water you want to add:"))

    newmilk = int(input("Write how many ml of milk you want to add:"))

    newbeans = int(input("Write how many grams of coffee beans you want to add:"))

    newcups = int(input("Write how many disposable coffee cups you want to add:"))

    fill(newwater,newmilk,newbeans,newcups)
elif action == "take":
    mon(action)

print()
print(f'''The coffee machine has:
{water} of water
{milk} of milk
{beans} of coffee beans
{cup} of disposable cups
{money} of money
''')


    








