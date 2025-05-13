import json

def handler(request):
    # Enable CORS
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
    }

    if request.method != "GET":
        return {
            "statusCode": 405,
            "headers": headers,
            "body": json.dumps({"error": "Method not allowed"})
        }

    # Load JSON data
    with open("q-vercel-python.json", "r") as f:
        data = json.load(f)

    # Build name to marks mapping
    marks_dict = {entry['name']: entry['marks'] for entry in data}

    # Get query parameters
    query = request.query
    names = query.get("name", [])
    if isinstance(names, str):  # if it's a single string
        names = [names]

    # Get marks in the same order as names
    marks = [marks_dict.get(name, None) for name in names]

    return {
        "statusCode": 200,
        "headers": headers,
        "body": json.dumps({"marks": marks})
    }
