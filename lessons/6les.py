text = 'Алла'
# def is_polindrom(text):
#
#     if text[::].lower == text[::-1].lower:
#          return True
#     else:
#          return False
#
def is_polindrom(text):
    text = text.lower()
    return  text == text [::-1]
print(is_polindrom(text))