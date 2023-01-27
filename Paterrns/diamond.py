"""
Diamond Pattern

     *
    * *
   * * *
  * * * *
 * * * * *
  * * * *
   * * *
    * *
     *

"""

n = int(input("Enter number of rows: "))

for row in range(n):
    for j in range(row, n):
        print(" ", end="")
    for k in range(row+1):
        print("* ", end="")
    print()

for row in range(0, n-1):
    for j in range(0, row+2):
        print(" ", end="")
    for k in range(row, n-1):
        print("* ", end="")
    print()
