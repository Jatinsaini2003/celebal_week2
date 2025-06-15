import re

def check_regex_validity():
    T = int(input())
    for _ in range(T):
        pattern = input()
        try:
            re.compile(pattern)
            print("True")
        except re.error:
            print("False")

if __name__ == '__main__':
    check_regex_validity()