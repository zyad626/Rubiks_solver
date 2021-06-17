class RubiksCube:
    def __init__(self, n, front) -> None:
        self.front = front
        faces = "BRGYWO"
        self.cube = [
            [[color for i in range(n)]for j in range(n)]for color in faces
        ]
        
    def print_cube(self):
        for face in self.cube:
            for row in face:
                print(row)
            print("*"*40)

myCube = RubiksCube(3, "b")
myCube.print_cube()