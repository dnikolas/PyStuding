import unicodedata
import re

strlen = unicodedata.name('\U0001f4a9')
print(f'{strlen} = {unicodedata.lookup(strlen)}')
utf8str = strlen.encode('utf-8')
print(utf8str)
asciistr = utf8str.decode('utf-8')
print(re.findall('[PO]+', asciistr))
