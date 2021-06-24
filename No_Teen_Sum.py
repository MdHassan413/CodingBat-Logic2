# Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().


# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

a = int(input("Enter Value of 'A' : "))
b = int(input("Enter Value of 'B' : "))
c = int(input("Enter Value of 'C' : "))

if (a == 13 or a == 14 or a == 17 or a == 18 or a == 19 ):
    print(b+c)
elif (b == 13 or b == 14 or b == 17 or b == 18 or b == 19 ):
    print(a+c)
elif (c == 13 or c == 14 or c == 17 or c == 18 or c == 19 ):
    print(a+b)
else:
    print(a + b + c)