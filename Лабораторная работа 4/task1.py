# TODO решите задачу
import json
def task() -> float:
    json_file = "input.json"
    with open(json_file, 'r') as file:
        data = json.load(file)
        product = sum(item["score"] * item["weight"] for item in data)
        return round(product, 3)
print(task())
