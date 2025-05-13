from http.server import BaseHTTPRequestHandler
import json
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Set CORS headers
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

        # Parse query parameters
        from urllib.parse import parse_qs, urlparse
        query = parse_qs(urlparse(self.path).query)
        names = query.get("name", [])

        # Load marks.json (ensure correct path)
        file_path = os.path.join(os.path.dirname(__file__), "marks.json")
        with open(file_path, "r") as f:
            data = json.load(f)
        marks_dict = {entry['name']: entry['marks'] for entry in data}

        marks = [marks_dict.get(name, None) for name in names]
        response = json.dumps({"marks": marks})

        self.wfile.write(response.encode())
