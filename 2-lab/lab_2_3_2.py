import csv

def main():
    SOURCE = 'resources/store.csv'
    OUTPUT = 'resources/categories.csv'

    data = {}

    with open(SOURCE,"r") as source:
        reader = csv.DictReader(source, delimiter=";")
        for row in reader:
            category = row['Category']
            if not category in data:
                data[category] = 0
            data[category] =+ float(row['Price'])


    categories = []
    for category, price in data.items():
            categories.append({'Category': category,'Price': price })

    with open(OUTPUT, 'w', newline="") as output:
        fieldnames = ["Category", "Price"]
        writer = csv.DictWriter(output, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        writer.writerows(categories)
    

if __name__ == '__main__':
    main()
