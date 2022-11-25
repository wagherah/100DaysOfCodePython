# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# Step 1
# Get all the name from file and save in names list
names_file = open('Input/Names/invited_names.txt', mode='r')
names = []

while True:
    name = names_file.readline()
    if not name:
        break
    names.append(name.strip())
names_file.close()


starting_letter = open('Input/Letters/starting_letter.txt', mode='r')
content = starting_letter.read()
print(content)
for name in names:
    temp = content
    temp_2 = temp.replace('[name]', name)
    f = open(f'Output/ReadyToSend/letter_for_{name}.txt', 'w')
    f.write(temp_2)

starting_letter.close()
