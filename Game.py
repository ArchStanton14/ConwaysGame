import numpy as np

class game:
    def __init__(self, size, cells, cycles, syl = (0,1)):    #"cells" is an array of the coordinates of starting live cells
        self.size = size
        self.board = np.array([[syl[0] for i in range(size)]for i in range(size)])
        self.cycles = cycles
        self.cells = cells
        self.syl = syl
        #add support for different symbols

        for i in self.cells:         #look into parallelizing this later; also consider if cells should be linkedlist
            self.board[i[0]][i[1]] = syl[1]
    def run(self):              #keep dynamic list of cell neighbors_count instead of chekcing each time?
        print(self.board)
        while self.cycles > 0:
            marked = []
            maked = []
            neighbors = set()
            #check through list of live cells instead of every grid square
            for cell in self.cells:
                if self.neighbors_count(cell) < 2 or self.neighbors_count(cell) > 3:
                    marked.append(cell)
                #get list of empty cells neighboring live ones to check if they should come alive
                for i in self.empty_neighbors(cell):
                    neighbors.add(i)
            #add grown cells
            #print(neighbors)
            for cell in neighbors:
                #print(self.neighbors_count(cell))
                #print(cell, self.neighbors_count(cell))
                if self.neighbors_count(cell) == 3:
                    
                    maked.append(cell)
            #add new cells:
            for cell in maked:
                self.cells.append(cell)
                self.board[cell[0]][cell[1]] = self.syl[1]
            #remove marked cells:
            for cell in marked:
                self.board[cell[0]][cell[1]] = self.syl[0]
                self.cells.remove(cell)     #can be popped more efficiently
            for line in self.board:
                print("".join(line))
            #print(self.board)
            print("\n")
            self.cycles -= 1
    def empty_neighbors(self, cell):    #check number of lives neighbors_count
        directions = [(-1, 0), (1, 0), (0, -1), (0,1),(-1,-1),(1,1),(-1,1),(1,-1)]
        n = []
        for i in directions:    #check in each direction if there is a neighbor
            x = (cell[0] + i[0], cell[1] + i[1])
            #if self.inbounds(x):
            x = self.wrap(x)
            if self.board[x[0]][x[1]] == self.syl[0]:
                n.append(x)
        return n
    def neighbors_count(self, cell):    #check number of lives neighbors_count
        directions = [(-1, 0), (1, 0), (0, -1), (0,1),(-1,-1),(1,1),(-1,1),(1,-1)]
        n = 0
        for i in directions:    #check in each direction if there is a neighbor
            x = (cell[0] + i[0], cell[1] + i[1])
            #if self.inbounds(x):
            x = self.wrap(x)
            if self.board[x[0]][x[1]] == self.syl[1]:
                n += 1
        return n
    def inbounds(self, cell): #check if coord is in grid (later implement wrap around)
        return cell[0] >= 0 and cell[1] >= 0 and cell[0] < self.size and cell[1] < self.size
    def wrap(self, cell): #wrap around behavior. Desn't have to be complicated because we're only interested in steps of 1
        #tuples are immutable
        n = cell
        if cell[0] < 0:
            n = (self.size-1, n[1])
        if cell[1] < 0:
            n = (n[0], self.size-1)
        if cell[0] >= self.size:
            n = (0, n[1])
        if cell[1] >= self.size:
            n = (n[0], 0)
        return n


x = game(10, [(3,2),(3,3),(3,4),(2,4),(1,3)], 5000, (' |',' _'))
x.run()