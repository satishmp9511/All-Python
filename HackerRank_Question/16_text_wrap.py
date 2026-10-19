import textwrap

def wrap(string, max_width):
    # textwrap.fill() string ko max_width ke hisaab se tod kar '\n' (new line) laga deta hai
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
