# One Way
# file = open(file='my_file.txt')
# contents = file.read()
# print(contents)
# file.close()

# Another Way
# needs no close statement

with open(file='my_file.txt', mode='w+') as file:
    contents = file.read()
    print(contents)

# Over-Write Content
# with open(file='my_file.txt', mode='w' ) as file:
#     file.write('New Content')

# Append Content
# with open(file='my_file.txt', mode='a' ) as file:
#     file.write('New Content')
