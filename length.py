import json
import matplotlib.pyplot as plt
from geopandas import GeoDataFrame
df = GeoDataFrame.from_file("Tunnel/MapInfoRelationen/tunnel.MIF")
print(df.columns)
print(df.laenge)
print(type(df))
print(df.laenge.sum())
print(df.laenge.min())
print(df.laenge.max())
print(df.laenge.median())
print(df.bezeichnung.nunique())
hist = df.laenge.hist(bins=25)
plt.show()






