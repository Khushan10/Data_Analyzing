import pygal
from die import Die

die = Die()
result = []

for roll_num in range(10000):
	result.append(die.roll())

# Analysize result
freq = []
for value in range(1, die.num_side+1):
	freq.append(result.count(value))

# Visualize the result
hist = pygal.Bar()

hist.title = "Result of rolling die 10,000 times"
hist.x_lables = ['1', '2', '3', '4', '5', '6']
hist.x_titles = "Result"
hist.y_titles = "Frequency of Result"

hist.add('D6', freq)
hist.render_to_file('die_visual.svg')