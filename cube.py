YELLOW = 0; WHITE = 1; BLUE = 2; GREEN = 3; ORANGE = 4; RED = 5
color_map = {"Y": 'up', "W": 'down', "B": 'front', "G": 'back', "O": 'left', "R": 'right', 'up': "Y", 'down': "W", 'front': "B", 'back': "G", 'left': "O", 'right': "R"}
dictionary = {0: 'up', 1: 'down', 2: 'front', 3: 'back', 4: 'left', 5: 'right', 'up': 0, 'down': 1, 'front': 2, 'back': 3, 'left': 4, 'right': 5}
clockwise_side_face_map = {'left': 0, 'front': 1, 'right': 2, 'back': 3,  0: 'left', 1: 'front', 2: 'right', 3: 'back'}

class Cube:
    """
                 |************|
                 |*U1**U2**U3*|
                 |************|
                 |*U4**U5**U6*|
                 |************|
                 |*U7**U8**U9*|
                 |************|
     ************|************|************|************
     *L1**L2**L3*|*F1**F2**F3*|*R1**R2**R3*|*B1**B2**B3*
     ************|************|************|************
     *L4**L5**L6*|*F4**F5**F6*|*R4**R5**R6*|*B4**B5**B6*
     ************|************|************|************
     *L7**L8**L9*|*F7**F8**F9*|*R7**R8**R9*|*B7**B8**B9*
     ************|************|************|************
                 |************|
                 |*D1**D2**D3*|
                 |************|
                 |*D4**D5**D6*|
                 |************|
                 |*D7**D8**D9*|
                 |************|
    """
    def __init__(self, serial_string=None):
        if serial_string is not None:
            self.cube = dict(zip(dictionary.values(), [[], [], [], [], [], []]))
            # self.cube = {"up": [], "down": [], "front": [], "back": [], "left": [], "right": []}
            count = 0
            ptr = 0
            for char in serial_string:
                self.cube[dictionary[ptr]].append(char)
                count += 1
                if count % 9 == 0:
                    ptr += 1
        else:
            # self.cube = {"up": [YELLOW] * 9, "down": [WHITE] * 9, "front": [BLUE] * 9, "back": [GREEN] * 9,
            #          "left": [ORANGE] * 9, "right": [RED] * 9}
            self.cube = {"up": ['Y'] * 9, "down": ['W'] * 9, "front": ['B'] * 9, "back": ['G'] * 9,
                         "left": ['O'] * 9, "right": ['R'] * 9}
        self.command = []
        for (key, value) in self.cube.items():
            print(key+"value:"+str(value))

    def __str__(self):
        return """
                 |************|
                 |**%s***%s***%s*|
                 |************|
                 |**%s***%s***%s*|
                 |************|
                 |**%s***%s***%s*|
                 |************|
     ************|************|************|************
     **%s***%s***%s*|**%s***%s***%s*|**%s***%s***%s*|**%s***%s***%s*
     ************|************|************|************
     **%s***%s***%s*|**%s***%s***%s*|**%s***%s***%s*|**%s***%s***%s*
     ************|************|************|************
     **%s***%s***%s*|**%s***%s***%s*|**%s***%s***%s*|**%s***%s***%s*
     ************|************|************|************
                 |************|
                 |**%s***%s***%s*|
                 |************|
                 |**%s***%s***%s*|
                 |************|
                 |**%s***%s***%s*|
                 |************|
    """ % (*self.cube['up'],
           *self.cube['left'][0:3], *self.cube['front'][0:3], *self.cube['right'][0:3], *self.cube['back'][0:3],
           *self.cube['left'][3:6], *self.cube['front'][3:6], *self.cube['right'][3:6], *self.cube['back'][3:6],
           *self.cube['left'][6:9], *self.cube['front'][6:9], *self.cube['right'][6:9], *self.cube['back'][6:9],
           *self.cube['down'])

    @staticmethod
    def rotate(face, clockwise):
        temp = face[0:3]
        if clockwise:
            face[0:3] = face[6::-3]
            face[6::-3] = face[8:5:-1]
            face[8:5:-1] = face[2:9:3]
            face[2:9:3] = temp
        else:
            face[0:3] = face[2:9:3]
            face[2:9:3] = face[9:5:-1]
            face[9:5:-1] = face[6::-3]
            face[6::-3] = temp

    def up_roll(self, clockwise):
        self.rotate(self.cube['up'], clockwise)
        temp = self.cube['front'][0:3]
        if not clockwise:  # U'
            self.cube['front'][0:3] = self.cube['left'][0:3]
            self.cube['left'][0:3] = self.cube['back'][0:3]
            self.cube['back'][0:3] = self.cube['right'][0:3]
            self.cube['right'][0:3] = temp
            self.command.append("U'")
        else:  # U
            self.cube['front'][0:3] = self.cube['right'][0:3]
            self.cube['right'][0:3] = self.cube['back'][0:3]
            self.cube['back'][0:3] = self.cube['left'][0:3]
            self.cube['left'][0:3] = temp
            self.command.append("U")

    def down_roll(self, clockwise):
        self.rotate(self.cube['down'], clockwise)
        temp = self.cube['front'][6:9]
        if not clockwise:
            self.cube['front'][6:9] = self.cube['right'][6:9]
            self.cube['right'][6:9] = self.cube['back'][6:9]
            self.cube['back'][6:9] = self.cube['left'][6:9]
            self.cube['left'][6:9] = temp
            self.command.append("D'")
        else:
            self.cube['front'][6:9] = self.cube['left'][6:9]
            self.cube['left'][6:9] = self.cube['back'][6:9]
            self.cube['back'][6:9] = self.cube['right'][6:9]
            self.cube['right'][6:9] = temp
            self.command.append("D")

    def front_roll(self, clockwise):
        self.rotate(self.cube['front'], clockwise)
        temp = self.cube['up'][6:9]
        if clockwise:
            self.cube['up'][6:9] = self.cube['left'][8:1:-3]
            self.cube['left'][8:1:-3] = self.cube['down'][2::-1]
            self.cube['down'][2::-1] = self.cube['right'][0:7:3]
            self.cube['right'][0:7:3] = temp
            self.command.append("F")
        else:
            self.cube['up'][6:9] = self.cube['right'][0:7:3]
            self.cube['right'][0:7:3] = self.cube['down'][2::-1]
            self.cube['down'][2::-1] = self.cube['left'][8:1:-3]
            self.cube['left'][8:1:-3] = temp
            self.command.append("F'")

    def back_roll(self, clockwise):
        self.rotate(self.cube['back'], clockwise)
        temp = self.cube['up'][0:3]
        if clockwise:
            self.cube['up'][0:3] = self.cube['right'][2:9:3]
            self.cube['right'][2:9:3] = self.cube['down'][8:5:-1]
            self.cube['down'][8:5:-1] = self.cube['left'][6::-3]
            self.cube['left'][6::-3] = temp
            self.command.append("B")
        else:
            self.cube['up'][0:3] = self.cube['left'][6::-3]
            self.cube['left'][6::-3] = self.cube['down'][8:5:-1]
            self.cube['down'][8:5:-1] = self.cube['right'][2:9:3]
            self.cube['right'][2:9:3] = temp
            self.command.append("B'")

    def left_roll(self, clockwise):
        self.rotate(self.cube['left'], clockwise)
        temp = self.cube['up'][0:7:3]
        if clockwise:
            self.cube['up'][0:7:3] = self.cube['back'][8:1:-3]
            self.cube['back'][8:1:-3] = self.cube['down'][0:7:3]
            self.cube['down'][0:7:3] = self.cube['front'][0:7:3]
            self.cube['front'][0:7:3] = temp
            self.command.append("L")
        else:
            self.cube['up'][0:7:3] = self.cube['front'][0:7:3]
            self.cube['front'][0:7:3] = self.cube['down'][0:7:3]
            self.cube['down'][0:7:3] = self.cube['back'][8:1:-3]
            self.cube['back'][8:1:-3] = temp
            self.command.append("L'")

    def right_roll(self, clockwise):
        self.rotate(self.cube['right'], clockwise)
        temp = self.cube['up'][2:9:3]
        if clockwise:
            self.cube['up'][2:9:3] = self.cube['front'][2:9:3]
            self.cube['front'][2:9:3] = self.cube['down'][2:9:3]
            self.cube['down'][2:9:3] = self.cube['back'][6::-3]
            self.cube['back'][6::-3] = temp
            self.command.append("R")
        else:
            self.cube['up'][2:9:3] = self.cube['back'][6::-3]
            self.cube['back'][6::-3] = self.cube['down'][2:9:3]
            self.cube['down'][2:9:3] = self.cube['front'][2:9:3]
            self.cube['front'][2:9:3] = temp
            self.command.append("R'")

    def formula(self, command):
        for move in command:
            if move == 'U':
                self.up_roll(True)
            elif move == "U'":
                self.up_roll(False)
            elif move == 'D':
                self.down_roll(True)
            elif move == "D'":
                self.down_roll(False)
            elif move == 'F':
                self.front_roll(True)
            elif move == "F'":
                self.front_roll(False)
            elif move == 'B':
                self.back_roll(True)
            elif move == "B'":
                self.back_roll(False)
            elif move == 'L':
                self.left_roll(True)
            elif move == "L'":
                self.left_roll(False)
            elif move == 'R':
                self.right_roll(True)
            elif move == "R'":
                self.right_roll(False)

    @staticmethod
    def orientation(mov, front, top):
        front = front.lower()
        top = top.lower()
        algo = []
        # w->b b->y y->g g->w
        key = {'U': 'U', "U'": "U'", 'F': 'F', "F'": "F'", 'R': 'R', "R'": "R'", 'L': 'L', "L'": "L'", 'B': 'B',
               "B'": "B'", 'D': 'D', "D'": "D'"}
        if front == 'b': # b
            if top == 'y': # y
                key = {'U': 'U', "U'": "U'", 'F': 'F', "F'": "F'", 'R': 'R', "R'": "R'", 'L': 'L', "L'": "L'", 'B': 'B',
                       "B'": "B'", 'D': 'D', "D'": "D'"}
            elif top == 'r':
                key = {'U': 'R', "U'": "R'", 'F': 'F', "F'": "F'", 'R': 'D', "R'": "D'", 'L': 'U', "L'": "U'", 'B': 'B',
                       "B'": "B'", 'D': 'L', "D'": "L'"}
            elif top == 'w':
                key = {'U': 'D', "U'": "D'", 'F': 'F', "F'": "F'", 'R': 'L', "R'": "L'", 'L': 'R', "L'": "R'", 'B': 'B',
                       "B'": "B'", 'D': 'U', "D'": "U'"}
            elif top == 'o':
                key = {'U': 'L', "U'": "L'", 'F': 'F', "F'": "F'", 'R': 'U', "R'": "U'", 'L': 'D', "L'": "D'", 'B': 'B',
                       "B'": "B'", 'D': 'R', "D'": "R'"}
        elif front == 'r':
            if top == 'y':
                key = {'U': 'U', "U'": "U'", 'F': 'R', "F'": "R'", 'R': 'B', "R'": "B'", 'L': 'F', "L'": "F'", 'B': 'L',
                       "B'": "L'", 'D': 'D', "D'": "D'"}
            elif top == 'g':
                key = {'U': 'B', "U'": "B'", 'F': 'R', "F'": "R'", 'R': 'D', "R'": "D'", 'L': 'U', "L'": "U'", 'B': 'L',
                       "B'": "L'", 'D': 'F', "D'": "F'"}
            elif top == 'w':
                key = {'U': 'D', "U'": "D'", 'F': 'R', "F'": "R'", 'R': 'F', "R'": "F'", 'L': 'B', "L'": "B'", 'B': 'L',
                       "B'": "L'", 'D': 'U', "D'": "U'"}
            elif top == 'b':
                key = {'U': 'F', "U'": "F'", 'F': 'R', "F'": "R'", 'R': 'U', "R'": "U'", 'L': 'D', "L'": "D'", 'B': 'L',
                       "B'": "L'", 'D': 'B', "D'": "B'"}
        # w->b b->y y->g g->w
        elif front == 'g':
            if top == 'y':
                key = {'U': 'U', "U'": "U'", 'F': 'B', "F'": "B'", 'R': 'L', "R'": "L'", 'L': 'R', "L'": "R'", 'B': 'F',
                       "B'": "F'", 'D': 'D', "D'": "D'"}
            elif top == 'o':
                key = {'U': 'L', "U'": "L'", 'F': 'B', "F'": "B'", 'R': 'D', "R'": "D'", 'L': 'U', "L'": "U'", 'B': 'F',
                       "B'": "F'", 'D': 'R', "D'": "R'"}
            elif top == 'w':
                key = {'U': 'D', "U'": "D'", 'F': 'B', "F'": "B'", 'R': 'R', "R'": "R'", 'L': 'L', "L'": "L'", 'B': 'F',
                       "B'": "F'", 'D': 'U', "D'": "U'"}
            elif top == 'r':
                key = {'U': 'R', "U'": "R'", 'F': 'B', "F'": "B'", 'R': 'U', "R'": "U'", 'L': 'D', "L'": "D'", 'B': 'F',
                       "B'": "F'", 'D': 'L', "D'": "L'"}
        # w->b b->y y->g g->w
        elif front == 'o':
            if top == 'y':
                key = {'U': 'U', "U'": "U'", 'F': 'L', "F'": "L'", 'R': 'F', "R'": "F'", 'L': 'B', "L'": "B'", 'B': 'R',
                       "B'": "R'", 'D': 'D', "D'": "D'"}
            elif top == 'b':
                key = {'U': 'F', "U'": "F'", 'F': 'L', "F'": "L'", 'R': 'D', "R'": "D'", 'L': 'U', "L'": "U'", 'B': 'R',
                       "B'": "R'", 'D': 'B', "D'": "B'"}
            elif top == 'w':
                key = {'U': 'D', "U'": "D'", 'F': 'L', "F'": "L'", 'R': 'B', "R'": "B'", 'L': 'F', "L'": "F'", 'B': 'R',
                       "B'": "R'", 'D': 'U', "D'": "U'"}
            elif top == 'g':
                key = {'U': 'B', "U'": "B'", 'F': 'L', "F'": "L'", 'R': 'U', "R'": "U'", 'L': 'D', "L'": "D'", 'B': 'R',
                       "B'": "R'", 'D': 'F', "D'": "F'"}
        # w->b b->y y->g g->w
        elif front == 'y':
            if top == 'r':
                key = {'U': 'R', "U'": "R'", 'F': 'U', "F'": "U'", 'R': 'F', "R'": "F'", 'L': 'B', "L'": "B'", 'B': 'D',
                       "B'": "D'", 'D': 'L', "D'": "L'"}
            elif top == 'b':
                key = {'U': 'F', "U'": "F'", 'F': 'U', "F'": "U'", 'R': 'L', "R'": "L'", 'L': 'R', "L'": "R'", 'B': 'D',
                       "B'": "D'", 'D': 'B', "D'": "B'"}
            elif top == 'o':
                key = {'U': 'L', "U'": "L'", 'F': 'U', "F'": "U'", 'R': 'B', "R'": "B'", 'L': 'F', "L'": "F'", 'B': 'D',
                       "B'": "D'", 'D': 'R', "D'": "R'"}
            elif top == 'g':
                key = {'U': 'B', "U'": "B'", 'F': 'U', "F'": "U'", 'R': 'R', "R'": "R'", 'L': 'L', "L'": "L'", 'B': 'D',
                       "B'": "D'", 'D': 'F', "D'": "F'"}
        # w->b b->y y->g g->w
        elif front == 'w':
            if top == 'b':
                key = {'U': 'F', "U'": "F'", 'F': 'D', "F'": "D'", 'R': 'R', "R'": "R'", 'L': 'L', "L'": "L'", 'B': 'U',
                       "B'": "U'", 'D': 'B', "D'": "B'"}
            elif top == 'r':
                key = {'U': 'R', "U'": "R'", 'F': 'D', "F'": "D'", 'R': 'B', "R'": "B'", 'L': 'F', "L'": "F'", 'B': 'U',
                       "B'": "U'", 'D': 'L', "D'": "L'"}
            elif top == 'g':
                key = {'U': 'B', "U'": "B'", 'F': 'D', "F'": "D'", 'R': 'L', "R'": "L'", 'L': 'R', "L'": "R'", 'B': 'U',
                       "B'": "U'", 'D': 'F', "D'": "F'"}
            elif top == 'o':
                key = {'U': 'L', "U'": "L'", 'F': 'D', "F'": "D'", 'R': 'F', "R'": "F'", 'L': 'B', "L'": "B'", 'B': 'U',
                       "B'": "U'", 'D': 'R', "D'": "R'"}
        for m in mov:
            algo.append(key[m])
        return algo

    def find_edge(self, color1, color2):
        edges = [[4, 1, 0, 3], [4, 3, 3, 5], [4, 5, 2, 3], [4, 7, 1, 3],
                 [5, 1, 0, 5], [5, 3, 2, 5], [5, 5, 3, 3], [5, 7, 1, 5],
                 [2, 1, 0, 7], [2, 7, 1, 1], [3, 1, 0, 1], [3, 7, 1, 7]]
        for edge in edges:
            e = [self.cube[dictionary[edge[0]]][edge[1]], self.cube[dictionary[edge[2]]][edge[3]]]
            if (color1 in e) and (color2 in e):
                if color1 != e[0]:
                    edge[0], edge[1], edge[2], edge[3] = edge[2], edge[3], edge[0], edge[1]
                return edge

    def find_corner(self, color1, color2, color3):
        corners = [[4, 0, 0, 0, 3, 2], [4, 2, 0, 6, 2, 0], [4, 6, 1, 6, 3, 8], [4, 8, 1, 0, 2, 6],
                   [5, 0, 0, 8, 2, 2], [5, 2, 0, 2, 3, 0], [5, 6, 2, 8, 1, 2], [5, 8, 1, 8, 3, 6]]
        for corner in corners:
            c = [self.cube[dictionary[corner[0]]][corner[1]], self.cube[dictionary[corner[2]]][corner[3]], self.cube[dictionary[corner[4]]][corner[5]]]
            if (color1 in c) and (color2 in c) and (color3 in c):
                for index in range(3):
                    if color1 == c[index]:
                        c1_l = index
                    elif color2 == c[index]:
                        c2_l = index
                    else:
                        c3_l = index
                return corner[2 * c1_l:2 * c1_l + 2] + corner[2 * c2_l:2 * c2_l + 2] + corner[2 * c3_l:2 * c3_l + 2]  # TODO change

    def step1(self):
        count = 0
        while count < 4:
            count = 0
            for (face, colors) in self.cube.items():
                found = False
                if face == 'up':
                    for index in range(1, len(colors), 2):
                        if colors[index] == color_map['down']:
                            count += 1
                elif face in clockwise_side_face_map:
                    for index in range(len(colors)):
                        if index % 2 == 1 and colors[index] == color_map['down']:  # 边块
                            if index == 1 and clockwise_side_face_map.__contains__(face):
                                eval('self.'+face+'_roll(False)')
                                self.up_roll(True)
                                temp = clockwise_side_face_map[face]-1 if clockwise_side_face_map[face]-1 >= 0 else 3
                                eval('self.'+clockwise_side_face_map[temp]+'_roll(False)')
                                count += 1
                                found = True
                                break
                            elif index == 3:
                                temp = clockwise_side_face_map[face]-1 if clockwise_side_face_map[face]-1 >= 0 else 3
                                for i in range(3):
                                    eval('self.' + clockwise_side_face_map[temp] + '_roll(False)')
                                    if self.judge(count, False):
                                        count += 1
                                        found = True
                                        break
                                    eval('self.' + clockwise_side_face_map[temp] + '_roll(True)')
                                    self.up_roll(True)
                            elif index == 5:
                                temp = clockwise_side_face_map[face] + 1 if clockwise_side_face_map[face] + 1 <= 3 else 0
                                for i in range(3):
                                    eval('self.' + clockwise_side_face_map[temp] + '_roll(True)')
                                    if self.judge(count, False):
                                        count += 1
                                        found = True
                                        break
                                    eval('self.' + clockwise_side_face_map[temp] + '_roll(False)')
                                    self.up_roll(True)
                            elif index == 7:
                                for i in range(3):
                                    eval('self.' + face + '_roll(False)')
                                    if self.judge(count, True):
                                        found = True
                                        break
                                    eval('self.' + face + '_roll(True)')
                                    self.up_roll(True)
                else:  # down
                    for index in range(len(colors)):
                        if index % 2 == 1 and colors[index] == color_map['down']:  # 边块
                            rotate_map = {1: "front", 3: "left", 5: "right", 7: "back"}
                            for i in range(3):
                                eval('self.' + rotate_map[index] + '_roll(True)')
                                eval('self.' + rotate_map[index] + '_roll(True)')
                                if self.judge(count, False):
                                    found = True
                                    count += 1
                                    break
                                eval('self.' + face + '_roll(False)')
                                eval('self.' + face + '_roll(False)')
                                self.up_roll(True)
                if found:
                    break
        for i in range(4):
            face = clockwise_side_face_map[i]
            position = self.find_edge(color_map['down'], color_map[face])
            offset = self.translate_face_to_clockwise(position[2]) - clockwise_side_face_map[face]
            for j in range(abs(offset)):
                self.up_roll(offset > 0)
            eval('self.' + face + '_roll(True)')
            eval('self.' + face + '_roll(True)')

    def step2(self):
        corner_pos = ['BR', 'RG', 'GO', 'OB']
        for corner in corner_pos:
            position = self.find_corner(color_map['down'], corner[0], corner[1])
            if position[0]*position[2]*position[4] == dictionary['up']:  # 情况1
                face = dictionary[color_map[corner[0]]]
                for i in range(3):
                    if (position[0] == face and position[1] == 2) or (position[2] == face and position[3] == 2) or (position[4] == face and position[5] == 2):
                        break
                    self.up_roll(True)
                    position = self.find_corner(color_map['down'], corner[0], corner[1])

                formula = self.orientation(['R', 'U', "R'", "U'"], corner[0], color_map['up'])
                position = self.find_corner(color_map['down'], corner[0], corner[1])
                while not (position[3] == 8 and position[5] == 6):
                    self.formula(formula)
                    position = self.find_corner(color_map['down'], corner[0], corner[1])
            else:  # 情况2
                face = dictionary[color_map[corner[0]]]
                count = 0
                for i in range(3):
                    if (position[0] == face and position[1] == 8) or (position[2] == face and position[3] == 8) or (
                            position[4] == face and position[5] == 8):
                        break
                    self.down_roll(True)
                    count += 1
                    position = self.find_corner(color_map['down'], corner[0], corner[1])
                if position[0] == dictionary['down'] and position[2] == face and count == 0:
                    continue
                formula = self.orientation(['R', 'U', "R'", "U'"], corner[0], color_map['up'])
                self.formula(formula)
                for j in range(count):
                    self.down_roll(False)
                position = self.find_corner(color_map['down'], corner[0], corner[1])
                while not (position[3] == 8 and position[5] == 6):
                    self.formula(formula)
                    position = self.find_corner(color_map['down'], corner[0], corner[1])

    def step3(self):
        edge_pos = ['BR', 'RG', 'GO', 'OB']
        count = 0
        while count < 4:
            found = False
            count = 0
            for edge in edge_pos:
                position = self.find_edge(edge[0], edge[1])
                if position[0] == dictionary[color_map[edge[1]]] and position[2] == dictionary[color_map[edge[0]]]:  # 情况1
                    formula = self.orientation("R U U R' U R U U R' U F' U' F".split(sep=' '), edge[0], color_map['up'])
                    self.formula(formula)
                    count += 1
                    found = True
                elif position[0] == dictionary[color_map[edge[0]]] and position[2] == dictionary[color_map[edge[1]]]:
                    count += 1
                elif position[0]*position[2] == 0:
                    while position[0] != dictionary[color_map[edge[0]]] and position[2] != dictionary[color_map[edge[0]]]:
                        self.up_roll(True)
                        position = self.find_edge(edge[0], edge[1])
                    if position[0] == dictionary[color_map[edge[0]]]:  # 情况2
                        formula = self.orientation("U R U' R' U' F' U F".split(sep=' '), edge[0], color_map['up'])
                        self.formula(formula)
                        count += 1
                        found = True
                    else:  # 情况3
                        self.up_roll(False)
                        formula = self.orientation("R' U' R' U' R' U R U R".split(sep=' '), edge[0], color_map['up'])
                        self.formula(formula)
                        count += 1
                        found = True

            if not found and count != 4:
                for edge in edge_pos:
                    position = self.find_edge(edge[0], edge[1])
                    if color_map[dictionary[position[0]]] != edge[0] or color_map[dictionary[position[2]]] != edge[1]:
                        if position[1] == 5:  # 置换出来
                            self.formula(self.orientation("U R U' R' U' F' U F".split(sep=" "),color_map[dictionary[position[0]]], color_map['up']))
                        else:
                            self.formula(self.orientation("U R U' R' U' F' U F".split(sep=" "),color_map[dictionary[position[0]]], color_map['up']))


    def step4(self):
        if self.cube['up'][1] == self.cube['up'][3] == self.cube['up'][5] == self.cube['up'][7] == color_map['up']:
            return
        if self.cube['up'][1] == self.cube['up'][7] == color_map['up']:  # 情况1
            self.formula(self.orientation("F R U R' U' F'".split(sep=' '), color_map['left'], color_map['up']))
        elif self.cube['up'][3] == self.cube['up'][5] == color_map['up']:  # 情况1
            self.formula(self.orientation("F R U R' U' F'".split(sep=' '), color_map['front'], color_map['up']))

        elif self.cube['up'][1] == self.cube['up'][3] == color_map['up']:  # 情况2
            self.formula(self.orientation("F R U R' U' F' F R U R' U' F'".split(sep=' '), color_map['front'], color_map['up']))
        elif self.cube['up'][1] == self.cube['up'][5] == color_map['up']:  # 情况2
            self.formula(self.orientation("F R U R' U' F' F R U R' U' F'".split(sep=' '), color_map['left'], color_map['up']))
        elif self.cube['up'][3] == self.cube['up'][7] == color_map['up']:  # 情况2
            self.formula(self.orientation("F R U R' U' F' F R U R' U' F'".split(sep=' '), color_map['right'], color_map['up']))
        elif self.cube['up'][5] == self.cube['up'][7] == color_map['up']:  # 情况2
            self.formula(self.orientation("F R U R' U' F' F R U R' U' F'".split(sep=' '), color_map['back'], color_map['up']))

        else:  # 情况3
            self.formula(self.orientation("F R U R' U' F' F R U R' U' F' U F R U R' U' F'".split(sep=' '), color_map['front'], color_map['up']))

    def step5(self):
        if self.cube['up'][0] == self.cube['up'][2] == self.cube['up'][6] == self.cube['up'][8] == color_map['up']:
            return
        clockwise_map = {0: 2, 2: 1, 6: 3, 8: 0}
        corner_pos = ['BR', 'RG', 'GO', 'OB']
        right_pos = []
        formula6 = "R' U U R U R' U R"
        formula7 = "U' R U' U' R' U' R U' R'"
        for block in clockwise_map:
            if self.cube['up'][block] == color_map['up']:
                right_pos.append(block)
        if len(right_pos) == 1:
            temp = clockwise_map[right_pos[0]]
            if self.cube[color_map[corner_pos[temp][1]]][2] == self.cube[color_map[corner_pos[(temp+1) % 4][1]]][2] == self.cube[color_map[corner_pos[(temp+2) % 4][1]]][2] == color_map['up']:  # 情况1
                self.formula(self.orientation(formula6.split(sep=' '), corner_pos[temp][0], color_map['up']))
            else:  # 情况2
                self.formula(self.orientation(formula7.split(sep=' '), corner_pos[temp][0], color_map['up']))
        elif len(right_pos) == 2:
            if abs(clockwise_map[right_pos[0]] - clockwise_map[right_pos[1]]) == 2:  # 情况3
                if right_pos[0] == 0 or right_pos[1] == 0:  # 以左为前
                    self.formula(self.orientation(formula6.split(sep=' ') + formula7.split(sep=' '), color_map['left'], color_map['up']))
                else:
                    self.formula(self.orientation(formula6.split(sep=' ') + formula7.split(sep=' '), color_map['front'], color_map['up']))
            else:
                temp1 = clockwise_map[right_pos[0]]
                temp2 = clockwise_map[right_pos[1]]
                if self.cube[color_map[corner_pos[temp1][1]]][2] == color_map['up']:  # 情况5
                    self.formula(self.orientation(formula7.split(sep=' ') + formula6.split(sep=' '), corner_pos[temp1][1], color_map['up']))
                elif self.cube[color_map[corner_pos[temp2][1]]][2] == color_map['up']:  # 情况5
                    self.formula(self.orientation(formula7.split(sep=' ') + formula6.split(sep=' '), corner_pos[temp2][1], color_map['up']))
                else:  # 情况7
                    front = color_map[corner_pos[(temp1+1) % 4][1]] if self.cube[color_map[corner_pos[(temp1+1) % 4][1]]][0] == color_map['up'] else color_map[corner_pos[(temp2+1) % 4][1]]
                    self.formula(self.orientation(formula7.split(sep=' ') + ['U', 'U'] + formula6.split(sep=' '), front, color_map['up']))
        else:  # len(right_pos) == 0
            face_got_2_block = None
            for i in range(4):
                if self.cube[clockwise_side_face_map[i]][0] == self.cube[clockwise_side_face_map[i]][2] == color_map['up']:
                    face_got_2_block = clockwise_side_face_map[i]
                    break
            if self.cube[clockwise_side_face_map[(clockwise_side_face_map[face_got_2_block]+1) % 4]][2] == color_map['up']:  # 情况6
                self.formula(self.orientation(formula6.split(sep=' ') + ["U'"] + formula6.split(sep=' '), color_map[face_got_2_block], color_map['up']))
            else:  # 情况4
                self.formula(self.orientation(formula6.split(sep=' ') + formula6.split(sep=' '), color_map[face_got_2_block], color_map['up']))

    def step6(self):
        color = None
        pos = None
        for i in range(4):
            if self.cube[clockwise_side_face_map[i]][0] == self.cube[clockwise_side_face_map[i]][2]:
                color = self.cube[clockwise_side_face_map[i]][0]
                pos = clockwise_side_face_map[i]
                break
        if color is None:
            self.formula(self.orientation("R B' R F F R' B R F F R R".split(sep=" "), color_map['front'], color_map['up']))
            for i in range(4):
                if self.cube[clockwise_side_face_map[i]][0] == self.cube[clockwise_side_face_map[i]][2]:
                    color = self.cube[clockwise_side_face_map[i]][0]
                    pos = clockwise_side_face_map[i]
                    break

        offset = clockwise_side_face_map[pos] - clockwise_side_face_map[color_map[color]]
        for j in range(abs(offset)):
            self.up_roll(offset > 0)
        self.up_roll(True)
        self.formula(self.orientation("R B' R F F R' B R F F R R".split(sep=" "), color_map[clockwise_side_face_map[(clockwise_side_face_map[color_map[color]]-1) % 4]], color_map['up']))

    def step7(self):
        formula9 = "R U' R U R U R U' R' U' R R"
        formula10 = "R R U R U R' U' R' U' R' U R'"
        clockwise_edge_color = [self.cube['left'][1], self.cube['front'][1], self.cube['right'][1], self.cube['back'][1]]
        pos = None
        for i in range(4):
            if clockwise_edge_color[i] == color_map[clockwise_side_face_map[i]]:
                pos = i
        if pos is not None:  # 情况1或者情况2
            if clockwise_edge_color[(pos + 2) % 4] == color_map[clockwise_side_face_map[(pos - 1) % 4]]:  # 情况1
                self.formula(self.orientation(formula9.split(sep=" "), color_map[clockwise_side_face_map[(pos + 2) % 4]], color_map['up']))
            else:  # 情况2
                self.formula(self.orientation(formula10.split(sep=" "), color_map[clockwise_side_face_map[(pos + 2) % 4]], color_map['up']))
        elif self.cube['front'][1] == color_map['back'] and self.cube['back'][1] == color_map['front']:  # 情况3
            self.formula(self.orientation(formula9.split(sep=" ")+["U"]+formula9.split(sep=" ")+["U'"], color_map['front'], color_map['up']))
        elif self.cube['front'][1] == color_map['right'] and self.cube['back'][1] == color_map['left']:  # 情况4
            self.formula(self.orientation(formula9.split(sep=" ")+["U'"]+formula9.split(sep=" ")+["U"], color_map['front'], color_map['up']))
        elif self.cube['front'][1] == color_map['left'] and self.cube['back'][1] == color_map['right']:  # 情况4
            self.formula(self.orientation(formula9.split(sep=" ")+["U'"]+formula9.split(sep=" ")+["U"], color_map['back'], color_map['up']))

    @staticmethod
    def translate_face_to_clockwise(position):
        return clockwise_side_face_map[dictionary[position]]

    def judge(self, count, no_less):
        temp_count = 0
        for color in range(1, len(self.cube['up']), 2):
            if self.cube['up'][color] == color_map['down']:
                temp_count += 1
        if no_less:
            if temp_count >= count:
                return True
            else:
                return False
        else:
            if temp_count > count:
                return True
            else:
                return False

    def print_command(self):
        last_move = ""
        repetition = []
        new_command = []
        for move in self.command:
            last_move = self.de_weight(new_command, move, repetition, last_move)
        self.command = new_command
        for move in self.command:
            print(move, end=" ")

    def de_weight(self, new_command, move, repetition, last_move):
        if last_move == move + "'" or move == last_move + "'":
            new_command.pop()
            repetition.pop()
            last_move = new_command[len(new_command) - 1] if len(new_command) - 1 >= 0 else ""
            return last_move
        elif move == last_move:
            new_command.append(move)
            repetition.append(repetition[len(repetition) - 1] + 1)
            if repetition[len(new_command) - 1] == 3:
                repetition.pop()
                repetition.pop()
                repetition.pop()
                new_command.pop()
                new_command.pop()
                new_command.pop()
                last_move = new_command[len(new_command) - 1]
                return self.de_weight(new_command, move+"'" if len(move) == 1 else move[0], repetition, last_move)
            else:
                return last_move
        else:
            new_command.append(move)
            last_move = move
            repetition.append(1)
            return last_move

    def print_cube(self):
        print(self)

    def solve(self):
        self.step1()
        self.step2()
        self.step3()
        self.step4()
        self.step5()
        self.step6()
        self.step7()

if __name__ == '__main__':
    cube = Cube("YBYWYWBWWWOWGWWRGYWBGRBYRGGOYORGORRBBGOBOBYYBRRGORYOOG")
   # cube = Cube()
    # cube.formula('RRLULUBUBFBFFFULRULUURBFBUUULULRBBLB')
    cube.solve()
    # cube.formula("R R D' D' U R R D' D' U R R D' D' U L L U' L L U U F F U' U' R R U' U' B B D R U R' U' D' R U R' U' R U R' U' R U R' U' R U R' U' R U R' U' D' B U B' U' D B U B' U' B U B' U' B U B' U' B U B' U' B U B' U U L U L' F U F' U U R U' R' U' F' U F B U' B' U' R' U R U' U' L' U' L' U' L' U L U L F U' F' U' L' U L L F U F' U' L' F' U U F U F' U' F U F' U F R B' R F F R' B R F F R R U U B L' B R R B' L B R R U B U B' U' B' U' B' U B'".split(" "))
    cube.print_cube()
    cube.print_command()
