# import pygame library
import pygame

# initialise pygame font
pygame.font.init()

# set window size
screen = pygame.display.set_mode((500, 700))

# set game title and game icon
pygame.display.set_caption("Sudoku Solver Using Backtracking")
img = pygame.image.load('icon.jpeg')
pygame.display.set_icon(img)

# coordinate of a selected cell
x = 0
y = 0
# width and heigt of each cell
diff = 500/9
val = 0

# default sudoku board
grid = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

# load different fonts
font1 = pygame.font.SysFont("Arial", 40)
font2 = pygame.font.SysFont("Arial", 20)

# convert mouse location to the coordinate of a selected grid
def get_coordinate(pos):
    global x
    x = pos[0]//diff
    global y
    y = pos[1]//diff

# highlight the selected cell
def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (247, 144, 168), (x * diff-3, (y + i)*diff), (x * diff + diff + 3, (y + i)*diff), 7)
        pygame.draw.line(screen, (247, 144, 168), ((x + i)* diff, y * diff ), ((x + i) * diff, y * diff + diff), 7)

# draw lines to make sodoku grid
def draw():
    # draw lines
    for i in range(9):
        for j in range(9):
            if(grid[i][j] != 0):
                # fill light pink in numbered grid
                pygame.draw.rect(screen, (242, 179, 194), (i*diff, j*diff, diff+1, diff+1))

                # fill grid with default numbers
                text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
                screen.blit(text1, (i * diff + 15, j * diff + 15))
    # draw horizontal and vertical lines to form grid
    for i in range(10):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * diff), (500, i * diff), thick)
        pygame.draw.line(screen, (0, 0, 0), (i* diff, 0), (i * diff, 500), thick)

# fill value entered in cell
def draw_val(val):
    text1 = font1.render(str(val), 1, (0, 0, 0))
    screen.blit(text1, (x * diff + 15, y * diff + 15))

# trigger error when wrong value is entered
def raise_error1():
    text1 = font1.render("Wrong", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))
def raise_error2():
    text1 = font1.render("Wrong. Not a valid key.", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))

# check if the value entered is valid
def valid(g, i, j, val): 
    for it in range(9):
        # check if there is any duplicate number on the same row or any duplicate number on the same column
        if g[i][it] == val or g[it][j] == val:
            return False
    it = i//3 # floor division operator
    jt = j//3
    # check if there is any duplicate number in the 3*3 grid that grid[i][j] belongs to
    for i in range(it * 3, it * 3 + 3):
        for j in range (jt * 3, jt * 3 + 3):
            if g[i][j]== val:
                return False
    return True

# use backtracking to solve sudoku
def solve(grid, i, j):
    # skip filled grids
    while grid[i][j]!= 0:
        if i<8:
            i+= 1
        elif i == 8 and j<8:
            i = 0
            j+= 1
        elif i == 8 and j == 8:
            return True
    # updating this event queue
    pygame.event.pump()
    # it ranges from 1 to 9
    for it in range(1, 10):
        if valid(grid, i, j, it)== True:
            grid[i][j]= it
            global x, y
            x = i
            y = j
            screen.fill((255, 255, 255))
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(20)
            if solve(grid, i, j)== 1:
                return True
            else:
                grid[i][j]= 0
            screen.fill((255, 255, 255))
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(50) 
    return False

# display instruction on the game
def instruction():
    text1 = font2.render("Press D to reset to default soduku, R to clear", 1, (0, 0, 0))
    text2 = font2.render("Press Enter to visualise backtracking", 1, (0, 0, 0))
    screen.blit(text1, (20, 520))
    screen.blit(text2, (20, 540))

# display options when solved
def result():
    text1 = font1.render("Finished. Press R or D", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))
run = True
flag1 = 0 # allow user input when flag1 == 1
flag2 = 0 # auto solve sudoku if flag2 == 1
rs = 0
error = 0

# make window running
while run:
    screen.fill((255, 255, 255))
    # loop every events in event.get()
    for event in pygame.event.get():
        #quit button
        if event.type == pygame.QUIT:
            run = False
        # get mouse pos to inseert number
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            get_coordinate(pos)
        # get the number to be inserted when key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x += 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y -= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y += 1
                flag1 = 1
            if event.key == pygame.K_1:
                val = 1
            if event.key == pygame.K_2:
                val = 2
            if event.key == pygame.K_3:
                val = 3
            if event.key == pygame.K_4:
                val = 4
            if event.key == pygame.K_5:
                val = 5
            if event.key == pygame.K_6:
                val = 6
            if event.key == pygame.K_7:
                val = 7
            if event.key == pygame.K_8:
                val = 8
            if event.key == pygame.K_9:
                val = 9
            if event.key == pygame.K_RETURN:
                flag2 = 1
            # if R is pressed, clear the sudoku board
            if event.key == pygame.K_r:
                rs = 0
                error = 0
                flag2 = 0
                grid = [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                ]
            # if D is pressed, reset the sudoku to default
            if event.key == pygame.K_d:
                rs = 0
                error = 0
                flag2 = 0
                grid = [
                    [7, 8, 0, 4, 0, 0, 1, 2, 0],
                    [6, 0, 0, 0, 7, 5, 0, 0, 9],
                    [0, 0, 0, 6, 0, 1, 0, 7, 8],
                    [0, 0, 7, 0, 4, 0, 2, 6, 0],
                    [0, 0, 1, 0, 5, 0, 9, 3, 0],
                    [9, 0, 4, 0, 6, 0, 0, 0, 5],
                    [0, 7, 0, 3, 0, 0, 0, 1, 2],
                    [1, 2, 0, 0, 0, 7, 4, 0, 0],
                    [0, 4, 9, 2, 0, 6, 0, 0, 7]
                ]
    if flag2 == 1:
        if solve(grid, 0, 0) == False:
            error = 1
        else:
            rs = 1
        flag2 = 0
    if val != 0:
        draw_val(val)
        if valid(grid, int(x), int(y), val)==True:
            grid[int(x)][int(y)] = val
            flag1 = 0
        else:
            grid[int(x)][int(y)]=0
            raise_error2()
        val = 0
    if error == 1:
        raise_error1()
    if rs == 1:
        result()
    draw()
    if flag1 == 1:
        draw_box()
    instruction()
    pygame.display.update()

pygame.quit()
            