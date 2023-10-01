

def f(num):
    return str(num).zfill(3)

def main():
    FILENAME = 'mask.log'

    with open(FILENAME, "w") as file:
        for i in range(255, -1, -1):
            for j in range(255, -1, -1):
                for k in range(255, -1, -1):
                    for z in range(255, -1, -1):
                        file.write(f"{f(i)}.{f(j)}.{f(k)}.{f(z)}\n")




if __name__ == '__main__':
    main()
