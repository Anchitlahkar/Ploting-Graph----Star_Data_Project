import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


rows = []
with open("Star_Data.csv", "r") as f:
    csv_reader = csv.reader(f)

    for row in csv_reader:
        rows.append(row)


star_data = rows[1:]

mass = []
radius = []
gravity = []

temp_star_data = list(star_data)

for data in temp_star_data:
    planet_gravity = data[5]

    if planet_gravity.lower() == 'unknown':
        star_data.remove(data)

for data in star_data:
    gravity.append(data[5])
    mass.append(data[3])
    radius.append(data[4])


mass.sort()
radius.sort()
gravity.sort()


plt.figure()
sns.lineplot(mass, radius, marker='o')
plt.title('Graph ( Mass, Radius)')
plt.xlabel('Mass')
plt.ylabel('Radius')
plt.show()


plt.figure()
sns.lineplot(mass, gravity, marker='o')
plt.title('Graph ( Mass, Gravity)')
plt.xlabel('Mass')
plt.ylabel('Gravity')
plt.show()
