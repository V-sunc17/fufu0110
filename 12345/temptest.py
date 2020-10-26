# fufu F87441C
# fufu 1/10/2020 2:39 PM
'''
name = input("fufu?")

print(name)
'''

import re
#pattern = r'[1-9]{1,3}(\.[0-9]{1,3}){2}'

pattern = r'(\.[0-9]{1,3}){2}'
Str1 = '227.11.22.77.33 192.168.44.66'
match = re.findall(pattern, Str1, overlapped=True)
print(match)

for item in match:
    print(item[1])
