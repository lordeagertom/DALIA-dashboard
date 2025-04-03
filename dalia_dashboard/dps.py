import pandas
import os
import re
from functools import reduce

from dalia_dashboard.utils import get_project_root

root = get_project_root()

class DPS:
    def __init__(self, poi_lon, poi_lat, poi_elev, number, name):
        self.lon = poi_lon
        self.lat = poi_lat
        self.elev = poi_elev
        self.number = number
        self.name = name
        self.data = self.read_data()
    
    def read_data(self):
        data_dir = os.path.join(root, "data")
        files = os.listdir(data_dir)

        pattern = f"DPS{self.number}"
        for file in files:
            if re.search(pattern, file):
                break
        else:
            raise FileNotFoundError(f"No file found for DPS{self.number} in the data directory.")

        df = pandas.read_csv(os.path.join(data_dir, file), index_col=0)
        return df


def common_indexes(instances):
    if not instances:
        return []
    common = reduce(lambda x, y: x.intersection(y), (set(instance.data.index) for instance in instances))
    return list(common)


DPS1 = DPS(poi_lon=17.455, poi_lat=47.849, poi_elev=120, number=1, name="Hungary Sziegetköz")
DPS2 = DPS(poi_lon=11.286, poi_lat=48.746, poi_elev=389, number=2, name="Bergheim-Ingolstadt")
DPS3 = DPS(poi_lon=16.604, poi_lat=49.183, poi_elev=237, number=3, name="Dyje-Thaya")
DPS4 = DPS(poi_lon=18.731, poi_lat=49.218, poi_elev=378, number=4, name="Zilna")
DPS5 = DPS(poi_lon=19.604, poi_lat=45.222, poi_elev=80, number=5, name="Begečka Jama")
DPS6 = DPS(poi_lon=22.562, poi_lat=44.307, poi_elev=46, number=6, name="Iron Gates")
DPS7 = DPS(poi_lon=29.284, poi_lat=45.288, poi_elev=0, number=7, name="Danube Delta")
DPS8 = DPS(poi_lon=21.572, poi_lat=48.319, poi_elev=116, number=8, name="Bodrog River Basin")
DPS9 = DPS(poi_lon=21.843, poi_lat=47.081, poi_elev=142, number=9, name="Crisuri Water Basin")

dps_instances = [DPS1, DPS2, DPS3, DPS4, DPS5, DPS6, DPS7, DPS8, DPS9]
common_indexes = common_indexes(dps_instances)