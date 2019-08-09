import copy
class Space:
    def __init__(self, x: int, y: int, val=None, tags=[]):
        self.x = x
        self.y = y
        self.value = val
        self.tags = tags

    def getTags(self):
        return self.tags

    def addTag(self, t: int):
        if t not in self.tags:
            self.tags.append(t)

    def getValue(self):
        return self.value

    def setValue(self, val: int):
        self.value = val


class Board:
    def __init__(self, board=[]):
        self.board = board
        if self.board == []:
            for i in range(9):
                self.board.append([])
                for j in range(9):
                    self.board[i].append(copy.deepcopy(Space(i, j)))

    def getValue(self, x: int, y: int):
        return self.board[x][y].getValue()

    def setValue(self, x: int, y: int, val: int):
        self.board[x][y].setValue(val)
        for i in range(9):
            self.board[i][y].addTag(val)
            self.board[x][i].addTag(val)
        newX = (x // 3) * 3
        newY = (y // 3) * 3
        for i in range(3):
            for j in range(3):
                self.board[newX + i][newY + j].addTag(val)

    def isGoodIdea(self, x: int, y: int, val: int):
        return not (val in self.board[x][y].getTags())

    def isDone(self):
        for i in range(9):
            for j in range(9):
                if self.getValue(i, j) == None:
                    return False
        return True

    def copy(self):
        arr = []
        for i in range(9):
            arr.append([])
            for j in range(9):
                arr[i].append(Space(i, j, self.board[i][j].getValue(), self.board[i][j].getTags()))
        return Board(arr)

    def toString(self):
        for i in range(9):
            out = ""
            for j in range(9):
                out += str(self.getValue(i, j)) + ", "
            print(out + "\n")

b = Board()


for i in range(9):
    for j in range(9):
        a = int(input())
        if a > 0:
            b.setValue(i, j, a)
    print("new line")

# bb = [  [1,2,0,4,5,6,7,8,9],
#         [4,5,0,7,8,9,1,0,0],
#         [7,8,9,1,2,3,4,5,6],
#         [2,3,4,5,6,7,8,9,1],
#         [5,6,7,8,9,1,2,3,4],
#         [8,9,1,2,3,4,5,6,7],
#         [3,4,5,6,7,8,9,1,2],
#         [6,7,8,0,1,2,3,4,5],
#         [9,1,2,3,4,5,6,7,8]]
#
# bb = [  [0,8,0,0,0,0,0,5,7],
#         [9,0,5,0,0,0,6,8,0],
#         [0,0,0,0,0,3,0,0,0],
#         [0,0,8,0,0,6,5,0,0],
#         [3,2,0,0,1,0,0,4,6],
#         [0,0,4,9,0,0,2,0,0],
#         [0,0,0,3,0,0,0,0,0],
#         [0,3,2,0,0,0,7,0,4],
#         [8,4,0,0,0,0,0,6,0]]

# for i in range(9):
#     for j in range(9):
#         a = bb[i][j]
#         if a > 0:
#             b.setValue(i, j, a)

def solve(b):
    if b.isDone():
        return b
    else:
        for g in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            for i in range(9):
                for j in range(9):
                    if b.isGoodIdea(i, j, g):
                        tempBoard = copy.deepcopy(b)
                        tempBoard.setValue(i, j, g)
                        solved = solve(tempBoard)
                        if not solved == None:
                            return solved


b = solve(b)
b.toString()
