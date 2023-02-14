"""
CamelCase to snake_case converter
"""

def convert_to_python_case(text):
    s = ""
    for c in range(len(text)):
        if text[c].isupper():
            s += "_" + text[c].lower()
        elif text[c].isalnum():
            s += text[c]
    return s[1:]

txt = input()

print(convert_to_python_case(txt))