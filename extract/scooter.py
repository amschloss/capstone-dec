import json
import requests

num_records = 50000

# secrets.json is intentionally not part of this repo
with open("../data/secrets.json") as f:
    secrets = json.load(f)
    token = secrets['socrata_token']

with requests.Session() as s:
    s.headers.update({"X-App-Token": token})
    offset = 0
    batch_count = num_records
    counter = 0

    while batch_count == num_records: # and counter < 10:
        # paginate query
        # with 150M records, need to balance between individual requests timing out and getting throttled
        rq_params = {"$limit": num_records, "$offset": offset, "$order": "start_time"}
        result = s.get("https://data.cityofchicago.org/resource/2kfw-zvte.json", params = rq_params)
        json_res = result.json()
        with open(f"../data/scooter_{counter}.json", "w") as f:
            json.dump(json_res, f)
        counter += 1
        batch_count = len(json_res)
        offset += batch_count
        print(f"Retrieved {offset} records")
