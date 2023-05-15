import random

class BinaryConverter:
    def __init__(self, start, end):
        self.data = random.randint(start, end)
    def binary(self, num):
        if num//2 == 0:
            return [num%2]
        return self.binary(num//2) + [num%2]

    def convert(self):
        binary_list = self.binary(self.data)
        return self.data, binary_list

binary_converter = BinaryConverter(4, 16)
data, binary_list = binary_converter.convert()
print(data, "Binary number is :", binary_list)
