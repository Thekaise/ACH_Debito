from fastapi import FastAPI

app = FastAPI()

# Lista simulada (normalmente sería una base de datos)
users = ["Alice", "Bob", "Charlie"]

@app.get("/users")
def get_users():
    return {"users": users}

@app.post("/users")
def create_user(name: str):
    users.append(name)
    return {"message": f"User {name} created"}
