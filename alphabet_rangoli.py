def print_rangoli(size):
    import string
    alphabets = string.ascii_lowercase

    lines = []
    for i in range(size):
        left = alphabets[size-1:i:-1]
        right = alphabets[i:size]
        row = '-'.join(left + right)
        width = 4 * size - 3
        lines.append(row.center(width, '-'))

    for line in lines[::-1] + lines[1:]:
        print(line)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)