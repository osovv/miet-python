

def f(num):
    return str(num).zfill(3)


def main():
    SOURCE_FILE = 'mask.log'
    OUTPUT_FILE = 'ip_solve.log'

    ip = input("Enter the IPv4 address:")

    parts = map(int, ip.split('.'))

    with open(INPUT_FILE, 'r') as source:
        with open(OUTPUT_FILE, 'w') as output:
            mask_parts = map(int, source.readline().split('.'))
            result = '.'.join([str(x & y) for x, y in zip(parts, mask_parts)])
            output.write(result)


if __name__ == '__main__':
    main()
