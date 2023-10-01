def reader(filename):
    with open(filename) as f:
        while True:
            # read next character
            char = f.read(1)
            # if not EOF, then at least 1 character was read, and 
            # this is not empty
            if char:
                yield char
            else:
                return


def is_letter(char):
    if 'a' <= char <= 'z':
        return True
    elif 'а' <= char <= 'я':
        return True
    else:
        return False


def main():
    SOURCE = './resources/article.txt'
    OUTPUT = './resources/article_solve.txt'
    data = {}
    total = 0

    r = reader(SOURCE)

    for c in r:
        char = c.lower() 
        if is_letter(char):
            if not char in data:
                data[char] = 0
            data[char] += 1
            total += 1

    fractions = [(char, count / total) for char, count  in sorted(data.items(), key=lambda x: x[1], reverse=True)]
    with open(OUTPUT, 'w') as output:
        for char, fraction in fractions:
            output.write(f"{char}: {fraction}\n")


if __name__ == '__main__':
    main()
