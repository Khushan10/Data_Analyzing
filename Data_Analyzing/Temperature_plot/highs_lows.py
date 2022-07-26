import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2021.csv'
with open(filename) as file:
	reader = csv.reader(file)
	header_row = next(reader)

	date, high, low = [], [], []
	for row in reader:
		date.append(datetime.strptime(row[2], "%d-%m-%Y"))
		high.append(int(row[5]))
		low.append(int(row[6]))

# Plot data
fig = plt.figure(dpi=128, figsize=(10,5))
plt.plot(date, high, c='red', alpha=0.5)
plt.plot(date, low, c='blue', alpha=0.5)
plt.fill_between(date, high, low, facecolor='purple', alpha=0.1)

# Format plot
plt.title("Daily high and low temperatures", fontsize=24)
# plt.xlabel()
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()