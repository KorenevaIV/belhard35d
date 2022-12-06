import re
#
#
# # email = '[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
# text = 'alex info@info.com pavel pavel@info.com'
# email = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
#
# print(re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text))

# for i in itertools.repeat('hello', 5):
#     for j in i:
#         print(j)

# words = ['', '', 'python', '', '']
# words = list(itertools.takewhile(lambda x: not x, words))
# print(words)

# print(list(itertools.compress('hello', (1, 1, 0, 1, 0))))
from itertools import zip_longest

text = '''
Hello
Python
World
Hello
Python
World
Hello
Python
World
'''
lines = [line for line in text.split('\n') if line]
# lines_iter = iter(lines)
# lines = list(zip_longest(*([lines_iter]*4)))
print(lines)