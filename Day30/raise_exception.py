height = float(input('Enter Height'))
weight = int(input('Enter Weight'))

if height > 3:
    raise ValueError('Human Height should not be greater than 3 meters')

bmi = weight / (height ** 2)
print(bmi)
