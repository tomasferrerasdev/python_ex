import csv

with open("weather.csv", "r", encoding="utf-8") as file:
    data = list(csv.reader(file))

city = input("Enter a city: ")
for row in data:
    if row[0] == city:
        print(f"City: {row[0]}, Temperature: {row[1]}")
        break
