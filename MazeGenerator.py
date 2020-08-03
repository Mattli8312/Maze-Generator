import pygame, random
pygame.init()
Grid = []
Stack = []
Width = 400
gap = 20
win = pygame.display.set_mode((Width, Width))
rows = cols = Width//gap
class Nodes():
    def __init__(self,i,j):
        self.i, self.j = i,j
        self.walls = [True,True,True,True]
        self.c = (0,0,0)
        self.visited = False
    def Generate(self,surf):
        thickness = 5
        wall_color = (0,0,0)
        if self.visited: self.c = (255,255,255)
        pygame.draw.rect(surf,self.c,(self.i*gap,self.j*gap,gap,gap))
        if self.walls[0]:
            pygame.draw.line(surf,wall_color,(self.i*gap,self.j*gap),(self.i*gap+gap,self.j*gap),thickness) #Top
        if self.walls[1]:
            pygame.draw.line(surf,wall_color,(self.i*gap,self.j*gap),(self.i*gap,self.j*gap+gap),thickness) #Left
        if self.walls[2]:
            pygame.draw.line(surf,wall_color,(self.i*gap,self.j*gap+gap),(self.i*gap+gap,self.j*gap+gap),thickness) #Bottom
        if self.walls[3]:
            pygame.draw.line(surf,wall_color,(self.i*gap+gap,self.j*gap),(self.i*gap+gap,self.j*gap+gap),thickness) #Right
    def CheckNeighbors(self):
        self.neighbors = []
        if self.i + 1 < cols:
            if not Grid[self.j][self.i+1].visited: self.neighbors.append(Grid[self.j][self.i+1]) # Right
        if self.j + 1 < rows:
            if not Grid[self.j+1][self.i].visited: self.neighbors.append(Grid[self.j+1][self.i]) # Bottom
        if not Grid[self.j][self.i-1].visited and self.i-1 >= 0: self.neighbors.append(Grid[self.j][self.i-1]) # Top
        if not Grid[self.j-1][self.i].visited and self.j - 1 >= 0: self.neighbors.append(Grid[self.j-1][self.i]) # Left
        if len(self.neighbors) > 0:
            index = random.randint(0,len(self.neighbors)-1)
            return self.neighbors[index]
        else:
            return False
def MakeGrid():
    grid = []
    for i in range(rows):
        grid.append([])
        for j in range(cols):
            grid[i].append(Nodes(j,i))
    return grid
def GenerateMaze():
    global Grid, Current, Stack
    next = Current.CheckNeighbors()
    if next:
        next.visited = True
        if next.i - Current.i == 1:
            next.walls[1] = Current.walls[3] = False
        elif next.i - Current.i == -1:
            next.walls[3] = Current.walls[1] = False
        elif next.j - Current.j == 1:
            next.walls[0] = Current.walls[2] = False
        else:
            next.walls[2] = Current.walls[0] = False
        Stack.append(next)
        Current = next
    elif len(Stack) > 0:
        Current = Stack.pop()
def Main():
    global Grid, Current
    run = True
    clock = pygame.time.Clock()
    Grid = MakeGrid()
    Current = Grid[0][0]
    Current.visited = True
    while run:
        clock.tick(30)
        pygame.time.delay(50)
        win.fill((255,255,255))
        for G in Grid:
            for b in G:
                b.Generate(win)
        pygame.draw.rect(win,(255,0,0),(Current.i*gap,Current.j*gap,gap,gap))
        GenerateMaze()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    pygame.quit()
Main()