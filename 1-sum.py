def sum():
    n = int(input("Enter the nth term: "))
    sum=0
    for x in range(1, n+1):
        sum = sum + x
    print(sum)
sum()
