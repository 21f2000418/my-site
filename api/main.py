from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS for all origins and all methods/headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks.json once at startup
with open("q-vercel-python.json") as f:
    data = json.load(f)
marks_dict = {entry['name']: entry['marks'] for entry in data}

@app.get("/api")
def get_marks(name: list[str] = Query([])):
    # Return marks in the order of names provided
    print(marks_dict)  # Debugging line to check the loaded data
    marks = [marks_dict.get(n, None) for n in name]
    return {"marks": marks}
