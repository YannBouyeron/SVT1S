import pandas as pd

import matplotlib.pyplot as plt


df = pd.read_json("https://ipfs.io/ipfs/QmaEerNc9isnYPmmzHuac3NPSTC6g8eyzXv1Q2LuBgqy8N")

plt.plot(df.temps, df.adn, "-*b")

plt.xlabel("Temps (H)")

plt.ylabel("Quantité d'ADN par cellule (UA)")

plt.title("Quantité d'ADN par cellule en fonction du temps")

plt.savefig("adncycle.png")

