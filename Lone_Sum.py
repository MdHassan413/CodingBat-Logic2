# Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.


# lone_sum(1, 2, 3) → 6
# lone_sum(3, 2, 3) → 2
# lone_sum(3, 3, 3) → 0


a = int(input("Enter Value of 'A' : "))
b = int(input("Enter Value of 'B' : "))
c = int(input("Enter Value of 'C' : "))

if ((a == b) and (b == a)):
     print(c)
elif ((c == a) and (a == c)):
     print(b)
elif ((b == c) and (c == b)):
     print(a)
else:
    print(a+b+c)