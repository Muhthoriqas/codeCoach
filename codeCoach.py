## Made By Thoriq As

##! Easy Problem

# TODO: Popsicles

siblings = int(input())
popsicles = int(input())

if popsicles  % siblings  == 0:
  print('give away')
else:
  print('eat them yourself')


# TODO: Hallowen Candy


import math
houses = int(input())

result= houses/2
hasil=100/result

print(math.ceil(hasil))

# TODO: Fruit Bowl

fruit = int(input())

x = fruit//2
print(x//3)

# TODO: Cheer Creator

yards =int(input())
if yards >10:
 print("High Five")
elif yards>1 and yards <=10:
 print("Ra!" * yards )
elif yards <= 1:
 print("shh" )


# TODO: Skee-Ball

score = int(input())
squirtGun = int(input())

ticket = score/12

if(ticket >= squirtGun):
    print("Buy it!")
else:
    print("Try again")


# TODO: Paint costs

inputColor = int(input("How much color you need? "))
import math
total = (5.00 * inputColor) + 40.00
tax = (total * 10//100)

print(math.ceil(total + tax))


# TODO: Store Argentina

inputPesos = int(input())
inputDollar = int(input())
exchange = inputPesos//50;
if(inputDollar > exchange):
    print("Pesos")
else:
    print("Dollars")


# TODO: Gotham City

inputCriminals = int(input())

if inputCriminals < 5:
    print("I got this!")
elif inputCriminals >= 5 and inputCriminals <=10:
    print("Help me Batman")
else:
    print("Good Luck out")


# TODO: Hovercraft

inputHovercrafts = int(input())

spent = 21000000
sell = 3000000 * inputHovercrafts

if sell > spent:
    print("Profit")
elif spent > sell:
    print("Loss")
else:
    print("Broke Even")


# TODO: Jungle Camping

noise = input()

a = noise.replace('Grr', 'Lion')
b = a.replace('Rawr', 'Tiger')
c = b.replace('Ssss', 'Snake')
d = c.replace('Chirp', 'Bird')

print(d)


# TODO: Extra-Terrestrials

print(input()[::-1])

#! End Easy Problem