import re

def remove_virus(source: str, virus: str) -> str:
    s = source
    v = virus
    result = re.sub(re.escape(v), '', s, flags=re.IGNORECASE)
    if virus in result:
        return remove_virus(result, virus)
    return result


def main():
    source = input("Enter a source string:")
    virus = input("Enter a virus string:")
    print(remove_virus(source, virus))

if __name__ == '__main__':
    main()
