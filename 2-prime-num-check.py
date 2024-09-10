def prime_no():
    n = int(input("Enter a number: "))
    if n < 1:
        print("Enter a number greater than 1.")
    else:
        pri_no = True
        for x in range(2, n):
            if n%x == 0:
                pri_no = False
        if pri_no:
             print(n, "is a prime number.")
        else:
             print(n, "is not a prime number")     
prime_no()