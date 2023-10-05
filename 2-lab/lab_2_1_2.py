def main():
    FILENAME = 'resources/mask.log'

    possible_values = [
        '255', '254', '252', '248', '240', '224', '192', '128', '000'
    ]

    xs = ['255' for _ in range(24)] + possible_values + ['000' for _ in range(0)]
    ys = ['255' for _ in range(16)] + possible_values + ['000' for _ in range(8)]
    ks = ['255' for _ in range(8)] + possible_values + ['000' for _ in range(16)]
    zs = ['255' for _ in range(0)] + possible_values + ['000' for _ in range(24)]

    data = zip(xs, ys, ks, zs)

    length = len(possible_values)

    with open(FILENAME, "w") as file:
        for x, y, k ,z  in data:
            file.write(f"{x}.{y}.{k}.{z}\n")




if __name__ == '__main__':
    main()
