# try
# code that might cause an exception

# except
# code that executes when exception occurs

# else
# code that executes if there were no exceptions

# finally
# code that runs, no matter what happens

# Example:
try:
    my_file = open('a_file.text')
    dictionary = {'Hello': 'World'}
    print(dictionary['hello'])

except FileNotFoundError:
    # if the file don't exist, create it
    my_file = open('a_file.text', 'w')

except KeyError as error_message:
    print(f'The key {error_message} does not exists')

# if no exception occurs
else:
    content = my_file.read()

# when everything proceed successfully
finally:
    my_file.close()
    # if we want to raise our own exception
    raise TypeError


