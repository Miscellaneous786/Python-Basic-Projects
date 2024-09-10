def checkerboard():
    for x in range(1,9):
        if x%2 == 0:
            print("  * "*8)
        else:
            print("*   "*8)
checkerboard()