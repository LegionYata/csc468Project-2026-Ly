from pymongo import MongoClient
from flask import Flask
import os

app = Flask(__name__)

# Connect to MongoDB using the service name as the hostname
client = MongoClient(os.environ.get("MONGO_URL", "mongodb://db:27017/"))
db = client["visitordb"]
counter = db["counter"]

# Initialize counter document if it doesn't exist
if counter.find_one({"_id": "visits"}) is None:
    counter.insert_one({"_id": "visits", "count": 0})

@app.route("/")
def index():
    # Atomically increment the visit count and return the updated value
    result = counter.find_one_and_update(
        {"_id": "visits"},
        {"$inc": {"count": 1}},
        return_document=True
    )
    count = result["count"]
    return f"""
    <html>
        <body>
            <h1>Welcome to the Visitor Counter!</h1>
            <p>Total Visits: <strong>{count}</strong></p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
