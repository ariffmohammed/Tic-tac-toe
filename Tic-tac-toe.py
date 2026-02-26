while True:
 grid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
 p1 = input("enter name for player 1\n")
 p2 = input("enter name for player 2\n")
 print("current board")
 print(grid[0], grid[1], grid[2])
 print(grid[3], grid[4], grid[5])
 print(grid[6], grid[7], grid[8])
 while True:
    pm1 = int(input("enter x position: "))
    if pm1 in grid:
        grid[pm1-1] = 'x'
        print(grid[0], grid[1], grid[2])
        print(grid[3], grid[4], grid[5])
        print(grid[6], grid[7], grid[8])
        if (grid[0] == grid[1] == grid[2] == 'x') or \
           (grid[3] == grid[4] == grid[5] == 'x') or \
           (grid[6] == grid[7] == grid[8] == 'x') or \
           (grid[0] == grid[4] == grid[8] == 'x') or \
           (grid[2] == grid[4] == grid[6] == 'x') or \
           (grid[0] == grid[3] == grid[6] == 'x') or \
           (grid[1] == grid[4] == grid[7] == 'x') or \
           (grid[2] == grid[5] == grid[8] == 'x'):
            print("\n" + p1 + " wins!")
            break
    pm2 = int(input("enter o position: "))
    if pm2 in grid:
        grid[pm2-1] = 'o'
        print(grid[0], grid[1], grid[2])
        print(grid[3], grid[4], grid[5])
        print(grid[6], grid[7], grid[8])
        if (grid[0] == grid[1] == grid[2] == 'o') or \
           (grid[3] == grid[4] == grid[5] == 'o') or \
           (grid[6] == grid[7] == grid[8] == 'o') or \
           (grid[0] == grid[4] == grid[8] == 'o') or \
           (grid[2] == grid[4] == grid[6] == 'o') or \
           (grid[0] == grid[3] == grid[6] == 'o') or \
           (grid[1] == grid[4] == grid[7] == 'o') or \
           (grid[2] == grid[5] == grid[8] == 'o'):
            print("\n" + p2 + " wins!")
            break
    if all(cell == 'x' or cell == 'o' for cell in grid):
            print("\nIt's a draw!")
            break
 relay=input("do u wnat to play again").lower()
 if relay!='yes':
  break
 

