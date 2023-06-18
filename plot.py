import json
import matplotlib.pyplot as plt

# JSON dosyasını yükleme
with open('avg_result.json') as file:
    data = json.load(file)

# "tayf" ve "avg" verilerini ayırma
tayf = [d["tayf"] for d in data]
avg = [d["avg"] for d in data]

# "tayf" verilerini küçükten büyüğe sıralama
sorted_indices = sorted(range(len(tayf)), key=lambda k: tayf[k])
sorted_tayf = [tayf[i] for i in sorted_indices]
sorted_avg = [avg[i] for i in sorted_indices]

# Grafiği oluşturma
plt.scatter(sorted_tayf, sorted_avg)
plt.xlabel('Tayf')
plt.ylabel('avg')
plt.title('Tayf Verileri')
plt.show()