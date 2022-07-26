import matplotlib.pyplot as plt

x_values = list(range(1, 101))
y_values = [x*x for x in x_values]
plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Reds, edgecolor = "blue", s=40)

#Set chart title and labels
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Sqaure of Value", fontsize = 14)

#Set size of labels
plt.tick_params(axis = "both", labelsize = 14)

# Set range of axis
plt.axis([0, 110, 0, 11000])

#Omit last argument to keep white space
plt.savefig('sqaures_plot.png', bbox_inches='tight')
plt.show()