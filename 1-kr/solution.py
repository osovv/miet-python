from collections import defaultdict
from datetime import datetime
from functools import reduce

def main():
  hourly_profit = defaultdict(int)
  hourly_max_department = defaultdict(int)
  hourly_department_profit = defaultdict(lambda: defaultdict(int))
  n = int(input().strip())
  current_max = 0
  current_max_hour = -1
  current_max_department_amount = 0
  current_max_department = -1

  for _ in range(n):
    department, _, sale_time, sale_amount = input().strip().split()
    sale_time = datetime.strptime(sale_time, "%H:%M:%S")
    hour = sale_time.hour
    amount = int(sale_amount)
    hourly_profit[hour] += amount
    if hourly_profit[hour] > current_max:
      current_max = hourly_profit[hour]
      current_max_hour = hour
    hourly_department_profit[hour][department] += amount


  departments = hourly_department_profit[current_max_hour]
  most_profitable_department = max(departments, key=departments.get)

  print(current_max_hour, most_profitable_department)

if __name__ == '__main__':
  main()
