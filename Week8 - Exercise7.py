def main():

    n = 20

    print (n)
def mystery(n):

    if n<=0:
        return 0
    else:
        return n + mystery(n //2) +1
main()
