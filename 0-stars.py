def stars():
    print("A tringle made from asterisks")
    for x in range(1, 11):
        print("  "*(10-x),"* "*(2*x-1))
stars()
