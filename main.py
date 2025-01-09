from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """
    Главная страница
    """
    return {"Главная страница"}

@app.get("/user/admin")
def read_admin():
    """
    Страница администратора
    """
    return {"Вы вошли как администратор"}

@app.get("/user/{user_id}")
def read_user(user_id: int):
    """
    Страница пользователя по ID
    """
    return {f"Вы вошли как пользователь № {user_id}"}

@app.get("/user")
def read_user_info(username: str, age: int):
    """
    Страница пользователя с параметрами в адресной строке
    """
    return {f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
