import re

def remove_virus(source: str, virus: str) -> str:
    s = source
    v = virus
    return re.sub(re.escape(v), '', s, flags=re.IGNORECASE)


def main(source: str, virus: str) -> str:
    source = input("Enter a source string:")
    virus = input("Enter a virus string:")
    return remove_virus(source, virus)

if __name__ == '__main__':
    main()