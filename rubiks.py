class RubiksCube:
    def __init__(self, n, front) -> None:
        self.front = front   
        self.n = n       
        faces = "BRGYWO"            #colors of the cube
        self.cube = {}              #dictionary to store the 6 faces of the cube
        for color in faces:         #create and store a face for every color
            self.cube[color] = [[color for i in range(n)]for j in range(n)]     #each face is represented by a 2d array
        self.vertical_order = "BYGW"
        self.horizontal_order = "BRGO"

    def R(self, face, reverse = False):
        idx = self.vertical_order.index(face)
        tmp = [row[self.n - 1] for row in self.cube[face]]      #store the right most values in each row of the face
        for i in range(4):
            pass

    def print_cube(self):
        for face in self.cube.values():
            for row in face:
                print(row)
            print("*"*40)

myCube = RubiksCube(3, "b")
myCube.print_cube()