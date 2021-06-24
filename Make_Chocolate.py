# We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.


# make_chocolate(4, 1, 9) → 4
# make_chocolate(4, 1, 10) → -1
# make_chocolate(4, 1, 7) → 2

smal = int(input("Enter Value of 'Small' : "))
big = int(input("Enter Value of 'Big' : "))
goal = int(input("Enter Value of 'Goal' : "))
d = smal - big
if((smal + big * 5) < goal):
    print("-1")
elif((smal + big * 5) > goal):
    print(d)
else:
    print(smal)
