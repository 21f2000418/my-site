import json
from urllib.parse import parse_qs
import csv


def handler(request, response):
    """
    Handles incoming requests and returns a JSON response.
    """
    # Extract the request body
    response.headers["Access-Control-Allow-Origin"] = "*"

    query = parse_qs(request.query_string. decode())
    names = query.get("name", [])

    with open("q-vercel-python.json", "r") as f:
        data = json.load(f)
        name_to_marks = {entry["name"]: int(entry["mark"]) for entry in data}

    marks = [name_to_marks.get(name, None) for name in names]

    # Return the JSON response
    return response.send(json.dumps({"marks": marks}), content_type="application/json")