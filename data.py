import geopandas
import matplotlib.pyplot as plt
import json
from geopandas import GeoDataFrame
df = GeoDataFrame.from_file("Tunnel/MapInfoRelationen/tunnel.MIF")
print(df.columns)
#df.plot()
#plt.show()
print(df.geometry)
combined_tunnels = []
for t in df["geometry"]:
    #print(type(t))
    #print(len(t.coords))
    coordinate_list = list(t.coords)
    start = coordinate_list[0]
    end = coordinate_list[-1]
    #print(start, end)
    combined_tunnels.append((start,end))
with open('data.json', 'w') as outfile:
    json.dump(combined_tunnels, outfile)











