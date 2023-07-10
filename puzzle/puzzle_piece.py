class Piece:
    def __init__(self, array1, array2, array3, array4):
        self.array1 = array1
        self.array2 = array2
        self.array3 = array3
        self.array4 = array4


    def get_array1(self):
        return self.array1

    def get_array2(self):
        return self.array2

    def get_array3(self):
        return self.array3

    def get_array4(self):
        return self.array4

    def set_array1(self, array):
        self.array1 = array

    def set_array2(self, array):
        self.array2 = array

    def set_array3(self, array):
        self.array3 = array

    def set_array4(self, array):
        self.array4 = array

    def print_arrays(self):
        print("Array 1:", self.array1)
        print("Array 2:", self.array2)
        print("Array 3:", self.array3)
        print("Array 4:", self.array4)