# We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks


# make_bricks(3, 1, 8) → True
# make_bricks(3, 1, 9) → False
# make_bricks(3, 2, 10) → True

sma_gol = int((input("Enter Small Bicks")))
big_gol = int((input("Enter Big Bicks")))
make_gol = int((input("Enter How Much Make Bicks")))
big = big_gol * 5 
if ((big + sma_gol >= make_gol)):
    print("True")
else:
    print("False")