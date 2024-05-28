import re

text = 'Today is 3/27/2018. Tomorrow is 3/28/2018.'
print(text)

findall = re.findall(r'\d+/\d+/\d+', text)
print(findall)

sub = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(sub)
