#
# Practice file fpr loops
#


days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
/home/a1kerr/Desktop/workspace/
def main():
    x = 0
    # define a while loop
    while(x < 5):
        print(x)
        x = x + 1
    # difne a for loop
    for x in range(5, 20):
        print(x)
    # interate array
    for d in days:
        print(d)
        # print(enumerate(d))
    # break and continue statementa
    for x in range(10, 20):
        if(x == 15):
            # break
            continue
        if(x % 2 == 0):
            continue
        print(x)
    for i, d in enumerate(days):
        print(i, d)


main()
# print(enumerate(days))
