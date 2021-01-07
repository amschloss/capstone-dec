import json
import requests

# secrets.json is intentionally not part of this repo
with open("../data/secrets.json") as f:
    secrets = json.load(f)
    token = secrets['socrata_token']

with requests.Session() as s:
    s.headers.update({"X-App-Token": token})
    result = s.get("https://data.cityofchicago.org/resource/74p9-q2aq.geojson")
    json_res = result.json()
    with open(f"../data/boundaries.geojson", "w") as f:
        json.dump(json_res, f)
        print(f"Retrieved census block records")
