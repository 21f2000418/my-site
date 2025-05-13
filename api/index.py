import json

def handler(request, response):
    # Enable CORS
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'

    # Only allow GET
    if request.method != "GET":
        response.status_code = 405
        return response.json({"error": "Method not allowed"})

    # Load marks.json
    with open("q-vercel-python.json", "r") as f:
        data = json.load(f)

    # Build a name->marks dict for quick lookup
    marks_dict = {entry['name']: entry['marks'] for entry in data}

    # Get names from query params
    names = request.query.getlist("name")
    # For single name, getlist may not work, so handle both
    if not isinstance(names, list):
        names = [names]

    # Get marks in order
    marks = [marks_dict.get(name, None) for name in names]

    return response.json({"marks": marks})
