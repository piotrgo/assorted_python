# which letter occurred the most in given string
import sys
import re
from collections import Counter


entry_string = str(sys.argv[1])
is_letter = re.compile('[^a-z ]')
found = is_letter.match(entry_string)
if found:
    print('Invalid entry string, only letters are allowed')
    exit()

most_common_letter = Counter(entry_string)
print(most_common_letter.most_common()[0])
