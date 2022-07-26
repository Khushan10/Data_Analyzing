import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Make a random walk, and plot points
while(True):
	rw = RandomWalk()
	rw.fill_walk()

	# Set size of plot window
	plt.figure(figsize=(14,7))

	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15)

	# Mark start and end
	plt.scatter(0, 0, c='green', edgecolor='none', s=100)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

	# plt.savefig('Random_walk_visual.png', bbox_inches='tight')
	plt.show()

	# Create another walk
	keep_running = int(input()) # Type 1 if you want else 0
	if(keep_running == 0):
		break