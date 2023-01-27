"""         columns
1.row       *
2.row       * *
3.row       * * *
4.row       * * * *
5.row       * * * * *
6.row       * * * *
7.row       * * *
8.row       * *
9.row       *

"""

rows = int(input("Enter number of rows: "))

for row in range(0, rows+1):
    for k in range(row):
        print("* ", end="")
    print()

    if row >= rows:
        for i in range(rows-1, -1, -1):
            for j in range(i):
                print("* ", end="")
            print()
