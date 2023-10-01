import csv

def main():
    SOURCE = 'resources/store.csv'
    OUTPUT = 'resources/categories.csv'

    data = {}

    with open(SOURCE,"r") as source:
        reader = csv.DictReader(source, delimiter=";")
        for row in reader:
            category = row['Категория']
            if not category in data:
                data[category] = 0
            data[category] =+ float(row['Стоимость'])


    categories = []
    for category, price in data.items():
            categories.append({'Категория': category,'Стоимость': price })

    with open(OUTPUT, 'w', newline="") as output:
        fieldnames = ["Категория", "Стоимость"]
        writer = csv.DictWriter(output, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        writer.writerows(categories)
    

if __name__ == '__main__':
    main()
