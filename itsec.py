class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0

    def get_value(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[row][col]
        else:
            print("Invalid row or column index")
            return None
        
    def get_coordinates(self, char):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] == char:
                    return i, j
        return None
        
def split_into_pairs(input_string):
    pairs = [input_string[i:i+2] for i in range(0, len(input_string), 2)]

    return pairs

upper = [
    ['P', 'R', 'I', 'V', 'A'],
    ['C', 'Y', 'B', 'D', 'E'],
    ['F', 'G', 'H', 'J', 'K'],
    ['L', 'M', 'N', 'O', 'S'],
    ['T', 'U', 'W', 'X', 'Z']
]     

lower = [
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I', 'J'],
    ['K', 'L', 'M', 'N', 'O'],
    ['P', 'R', 'S', 'T', 'U'],
    ['V', 'W', 'X', 'Y', 'Z']
]

upper_matrix = Matrix(upper)
lower_matrix = Matrix(lower)

input = "KTOUOFKERKVZFARSWFYUCEABLUBEPCNARSEPNRTANCBUWHDOWFDUZMSAXPYUOJLCDIGRPUFCABVMWFBUIOBEMNWLLHMTADVRICROUVNTTBABMTVMWFBUIOYUMYKKIGMTAXONTAOPZMSURUCJMTADVRICROUVNTTBABPULAVMZAXTDIGRPUJSFCZAOCSURVVSGCOTHCFCPBDPYUOJOSKCLESBEKSPOLJGADOUKCLESBDIGRPUJHOSKCDFIFYUZAXTVMYPCRZKGRPUJXWFISISABKARRDEZKIUVUPBNSPAABNCDW"

pairs = split_into_pairs(input)

decyphered_text = ""

for pair in pairs:
    first_char = pair[0]
    second_char = pair[1]

    # Find coordinates in the upper matrix
    upper_coordinates = upper_matrix.get_coordinates(first_char)

    # Find coordinates in the lower matrix for the second element in the pair
    lower_coordinates = lower_matrix.get_coordinates(second_char)

    upper_decyphered_coordinates = upper_coordinates[0], lower_coordinates[1]
    lower_decyphered_coordinates = lower_coordinates[0], upper_coordinates[1]

    upper_element = upper_matrix.get_value(upper_decyphered_coordinates[0], upper_decyphered_coordinates[1])
    lower_element = lower_matrix.get_value(lower_decyphered_coordinates[0], lower_decyphered_coordinates[1])

    decyphered_text += upper_element + lower_element

print(decyphered_text)