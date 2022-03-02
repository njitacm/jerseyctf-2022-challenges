import zipfile
import itertools
from itertools import permutations


# Function for extracting zip files to test if the password works!
def extractFile(zip_file, password):
    try:
        zip_file.extractall(pwd=password.encode())
        return True
    except KeyboardInterrupt:
        exit(0)
    except Exception as e:
        pass

# Main code starts here...
# The file name of the zip file.
zipfilename = 'secret_folder.zip'

file1 = open('actorList.txt', 'r')
Lines = file1.readlines()

numbers_set = '0123456789'

zip_file = zipfile.ZipFile(zipfilename)

for actor_name in Lines:
    for c in itertools.product(numbers_set, repeat=4):

        password = actor_name.strip()+''.join(c)
        # Try to extract the file.
        print("Trying: %s" % password)
        # If the file was extracted, you found the right password.
        if extractFile(zip_file, password):
            print('*' * 20)
            print('Password found: %s' % password)
            print('Files extracted...')
            exit(0)

# If no password was found by the end, let us know!
print('Password not found.')
