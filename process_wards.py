import json

wards = dict()

with open("wards.geojson", "r+", encoding="utf-8") as file:
    data = json.load(file)

for feature in data["features"]:
    ward_name = feature["properties"]["AREA_NAME"]
    coords = feature["geometry"]["coordinates"][0][0]
    north = max(coords, key=lambda x: x[1])[1]
    south = min(coords, key=lambda x: x[1])[1]
    east = min(coords, key=lambda x: x[0])[0]
    west = max(coords, key=lambda x: x[0])[0]
    wards |= {ward_name: [south, north, east, west]}

print(wards)

