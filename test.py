import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values = [15, 5, 2, 22, 20]
colors = ['red', 'blue', 'green', 'orange', 'purple']

plt.bar(categories, values, color=colors)

plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Colored Bar Graph')
plt.show()
