import json
import matplotlib.pyplot as plt

# Loading JSON file
with open('avg_result.json') as file:
    data = json.load(file)

# separating "spectrum" and "avg" data
tayf = [d["tayf"] for d in data]
avg = [d["avg"] for d in data]

# Sorting "spectrum" data from smallest to largest
sorted_indices = sorted(range(len(tayf)), key=lambda k: tayf[k])
sorted_tayf = [tayf[i] for i in sorted_indices]
sorted_avg = [avg[i] for i in sorted_indices]

# Create the graph
plt.scatter(sorted_tayf, sorted_avg)
plt.xlabel('Tayf')
plt.ylabel('avg')
plt.title('Tayf Verileri')
plt.show()
