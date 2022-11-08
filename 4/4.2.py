text = input()
data = {text[i]: text.count(text[i]) for i in range(0, len(text))}
data1 = {i:text.count(i) for i in text}
print(data)
print(data1)


h