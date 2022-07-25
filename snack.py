"""snack"""
def main():
    """snack"""
    money = int(input())
    water = int(input())
    snack1 = int(input())
    snack2 = int(input())
    snack3 = int(input())
    cost = 0
    cost1 = (money - water)%3
    ans1 = cost1 == 0 and snack1*10 or cost1 == 1 and snack1*15 or snack1*20
    cost += ans1
    cost2 = (money-water-cost)%3
    ans2 = cost2 == 0 and snack2*12 or cost2 == 1 and snack2*15 or snack2*18
    cost += ans2
    cost3 = (money-water-cost)%3
    ans3 = cost3 == 0 and snack3*5 or cost3 == 1 and snack3*7 or snack3*9
    cost += ans3
    if money < cost:
        print("Now you have %d left." %money)
        print("You don't have enough money!")
    else:
        print("Now you have %d left." %(money-cost-water))
        print("Here's your order!")
        print("Water: %d baht" %water)
        print("Snack number 1: %d baht" %ans1)
        print("Snack number 2: %d baht" %ans2)
        print("Snack number 3: %d baht" %ans3)
main()
    