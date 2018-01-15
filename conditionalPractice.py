#
# Practice file for conditional structors
#


def main():
    x, y = 101, 100
    if(x < y):
        st = "x is LESS than y"
    elif(x == y):
        st = "x is EQUAL to y"
    else:
        st = "x is GREATER than y"
    print(st)

    st = "x is LESS than y" if (x < y) else "x is GREATER than y"
    print(st)


main()
