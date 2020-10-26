# fufu F87441C
# fufu 1/10/2020 2:39 PM

import urllib.request

response = urllib.request.urlopen('http://mx660.now.net.cn/mail/')
html = response.read()
print(html)