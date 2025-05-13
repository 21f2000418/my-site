import json
import os

def handler(request):
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET",
        "Access-Control-Allow-Headers": "Content-Type"
    }

    if request.method != "GET":
        return {
            "statusCode": 405,
            "headers": headers,
            "body": json.dumps({"error": "Method not allowed"})
        }

    try:
        # Parse query
        query = request.query
        names = query.get("name", [])
        if isinstance(names, str):
            names = [names]

        # Load marks.json
        file_path = os.path.join(os.path.dirname(__file__), "../marks.json")
        with open(file_path, "r") as f:
            data = json.load(f)

        marks_dict = {entry['name']: entry['marks'] for entry in data}
        marks = [marks_dict.get(name, None) for name in names]

        return {
            "statusCode": 200,
            "headers": headers,
            "body": json.dumps({"marks": marks})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": headers,
            "body": json.dumps({"error": str(e)})
        }
