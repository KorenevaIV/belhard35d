text = input()
data = {text[i]: text.count(text[i]) for i in range(0, len(text))}
data = {i:text.count(i) for i in text}
