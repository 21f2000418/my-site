import json

def handler(request):
    # Set CORS headers
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
    }

    try:
        if request.method != "GET":
            return {
                "statusCode": 405,
                "headers": headers,
                "body": json.dumps({"error": "Method not allowed"})
            }

        # Load the JSON data
        with open("q-vercel-python.json", "r") as f:
            data = json.load(f)

        # Create a name->marks mapping
        marks_dict = {entry['name']: entry['marks'] for entry in data}

        # Handle query parameters
        query = request.query
        names = query.get("name", [])
        if isinstance(names, str):
            names = [names]

        # Build the list of marks
        marks = [marks_dict.get(name, None) for name in names]

        return {
            "statusCode": 200,
            "headers": headers,
            "body": json.dumps({"marks": marks})
        }

    except Exception as e:
        # Catch and return errors as JSON
        return {
            "statusCode": 500,
            "headers": headers,
            "body": json.dumps({"error": str(e)})
        }
