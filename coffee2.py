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
        waterafter = water - 250
        beansafter = beans - 16
        moneyafter = money -4
        cupafter = cup-1
    elif choose == 2:
        waterafter = water -350
        milkafter = milk - 75
        beansafter = beans -20
        moneyafter = money -7
        cupafter = cup-1
    elif choose == 3:
        waterafter = water - 200
        milkafter = milk -100
        beansafter = beans - 12
        moneyafter = money - 6
        cupafter = cup-1

def fill(newwater,newmilk,newbeans,newcups):
    global water, milk, beans, cup, money
    milkafter = milk + newmilk
    waterafter = water + newwater
    beansafter = beans + newbeans
    cupsafter = cup + newcups

def take(moneytake):
    global water, milk, beans, cup, money

    moneytake = money
    money == 0

action=input("Write action (buy, fill, take):")
if action == "buy":
    choose = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:") 
    buy(choose)
elif action == "fill":
    newwater = input("Write how many ml of water you want to add:")

    newmilk = input("Write how many ml of milk you want to add:")

    newbeans = input("Write how many grams of coffee beans you want to add:")

    newcups = input("Write how many disposable coffee cups you want to add:")

    fill(newwater,newmilk,newbeans,newcups)
elif action == "take":
    moneytake = int(input("I gave you $"))
    take(moneytake)
print()
print(f'''The coffee machine has:
{water} of water
{milk} of milk
{beans} of coffee beans
{cup} of disposable cups
{money} of money
''')


    








