from fastapi import FastAPI, HTTPException

app = FastAPI()

# Изначальный словарь пользователей
users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
def get_users():
    """
    Возвращает словарь пользователей.
    """
    return users

@app.post("/user/{username}/{age}")
def create_user(username: str, age: int):
    """
    Добавляет нового пользователя в словарь.
    """
    user_id = str(max(map(int, users.keys()), default=0) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: str, username: str, age: int):
    """
    Обновляет информацию о пользователе по user_id.
    """
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"

@app.delete("/user/{user_id}")
def delete_user(user_id: str):
    """
    Удаляет пользователя из словаря по user_id.
    """
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return f"User {user_id} has been deleted"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.2", port=8000)
