def print_operation_table (operation, row, column):
    for i in range (1, row+1):
        for j in range (1, column+1):
            if operation(i, j)//10>=1:
                print (operation(i, j), end = " ")    
            else:
                print (operation(i, j), end = "  ")
        print()

print_operation_table(lambda x,y: x*y, 6, 6)
