import matplotlib.pyplot as plt

import pandas as pd

df = pd.read_json("meiose.json")

plt.plot(df.temps, df.adn, "-*b")

plt.xlabel("Temps (H)")

plt.ylabel("Quantité d'ADN par cellule (UA)")

plt.title("Quantité d'ADN par cellule en fonction du temps lors de la méiose", fontsize=8)

plt.savefig("meiose.png")

