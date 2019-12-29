# The regex library is widely use with many of the standard libraries
# It acts as a normal regex library with a very easy interface to work with
import re

# You can easily check for a regex match in the following way
pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)
if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")

# You can also find all of the occurances
string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'
result = re.findall(pattern, string) 
print(result)

# And split by regex
string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'
result = re.split(pattern, string) 
print(result)

# One of the more commonly used functions of regex is sub
# It is used to switch one regex pattern with a string value
string = 'abc 12 de 23 f45 6'
# Matches all whitespace characters
pattern = '\s+'
# Replace them with empty string
replace = ''
new_string = re.sub(pattern, replace, string) 
print(new_string)
# Output: abc12de23f456

# Lastly, the search function is used to search for the first occurance of a regex
# If found, will return a match object that can print the group, which is the found string
# And print the start and end indices
string = '39801 356, 2102 1111'
# Three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'
match = re.search(pattern, string) 
if match:
  print(match.group())
else:
  print("Pattern not found")