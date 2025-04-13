from fastapi import FastAPI
from ad_connector import connect
from reports import list_all_users

app = FastAPI()

@app.get("/users")
def get_users():
    conn = connect()
    results = list_all_users.run(conn)
    return [entry.entry_to_json() for entry in results]
