def count_seats_prices(tickets):
    data  = {}
    
    for ticket in tickets:
        row, seat, price = ticket

        if not row in data:
            data[row] = {}

        if not seat in data[row]:
            data[row][seat] = {}

        data[row][seat][price] = True

    result = []

    for row, seats in data.items():
        for seat, prices in seats.items():
            result.append((row, seat, len(prices.keys())))

    return result

def main():
    n = int(input("Enter the number of tickets:"))
    print("Enter the tickets information:")
    tickets = []
    for i in range(n):
        raw = input()
        row, seat, price = map(int, raw.split(" "))
        tickets.append((row, seat, price))
    prices = count_seats_prices(tickets)

    print("Results: ")
    for row, seat, count in prices:
        print(f"{row} {seat} - {count}")

if __name__ == "__main__":
    main()
