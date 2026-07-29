def matrix():
    row = int(input("Enter row no:"))
    column = int(input("Enter column no:"))
    arr = []

    for i in range(row):
        x = list(map(int, input(f"Enter row {i + 1} elements: ").split()))
        if len(x) != column:
            print("Invalid input for column length. Please try again.")
            return
        arr.append(x)
    
    print("The matrix is:")
    for i in range(row):
        for j in range(column):
            print(arr[i][j], end=" ")
        print('')

matrix()
