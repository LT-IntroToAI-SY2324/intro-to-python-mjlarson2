# Complete your individualized AI problems here

# def fizbuzz(input_num):
#     if(input_num % 3 == 0):
#         if(input_num % 5 == 0):
#             return 'FizzBuzz'
#         return 'Fizz'
#     elif(input_num % 5 == 0):
#         return 'Buzz'
#     else:
#         return input_num

# assert fizbuzz(1) == 1, "fizzbuzz 1 test"
# assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
# assert fizbuzz(4) == 4, "fizzbuzz 4 test"
# assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
# assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
# assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

# Binary to decimal



def toDecimal(binary:str):
    decimal = 0
    reversedBinary = binary[::-1]
    for i in range(len(reversedBinary)):
        decimal += ( int(reversedBinary[i:i + 1]) * (2 ** i) )
    return decimal

assert toDecimal("00000001") == 1
assert toDecimal("10010110") == 150
print("All tests passed!")

