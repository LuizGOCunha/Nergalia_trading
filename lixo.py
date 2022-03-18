
x5 = ["0,5","1,5","2,5","3,5","4,5","5,5",]
x4 = ["0,4","1,4","2,4","3,4","4,4","5,4",]
x3 = ["0,3","1,3","2,3","3,3","4,3","5,3",]
x2 = ["0,2","1,2","2,2","3,2","4,2","5,2",]
x1 = ["0,1","1,1","2,1","3,1","4,1","5,1",]
x0 = ["0,0","1,0","2,0","3,0","4,0","5,0",]


x5 = ["mm","mm","mm","mm","mm","mm",]
x4 = ["mm","mm","mm","tt","mm","mm",]
x3 = ["II","II","II","II","II","-v",]
x2 = ["-v","tt","tt","II","mm","mm",]
x1 = ["mm","tt","tt","II","mm","mm",]
x0 = ["mm","mm","mm","II","mm","mm",]

grid = [
    x5,
    x4,
    x3,
    x2,
    x1,
    x0
]


for x_axis in grid:
    string = "*"
    for coordenate in x_axis:
        string += coordenate
    string += "*"
    print(string)








    if 0 < y < len(self.grid):
            return False
        # fazemos o mesmo com o x
        elif 0 < x < len(self.grid[y]):
            return False