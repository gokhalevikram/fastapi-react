from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from psycopg2.extras import RealDictCursor
import json

todos = [
    {
        "id": "1",
        "item": "Read a book."
    },
    {
        "id": "2",
        "item": "Cycle around town."
    },
    {
        "id": "3",
        "item": "Play chess."
    }
]

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your todo list."}

@app.get("/todo", tags=["todos"])
async def get_todos() -> dict:
    return { "data": todos }

@app.get("/users", tags=["users"])
async def get_users():

    conn = psycopg2.connect(database="vms",
                            host="localhost",
                            user="vmsadmin",
                            password="0xdeadbeef",
                            port="5432")
    
    cur = conn.cursor(cursor_factory=RealDictCursor)
    query_sql = "SELECT row_number() OVER (ORDER BY name) AS id, name, email, short_intro from public.users_profile"
    cur.execute(query_sql)
    results = cur.fetchall()
    # results_json = json.dumps(results)
    print(results)
    return results