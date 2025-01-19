from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
def read_root():
    """
    Главная страница
    """
    return {"message": "Главная страница"}

@app.get("/user/admin")
def read_admin():
    """
    Страница администратора
    """
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
def read_user(
    user_id: Annotated[int, Path(description="Enter User ID", ge=1, le=100)]
):
    """
    Страница пользователя по ID
    """
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/{username}/{age}")
def read_user_info(
    username: Annotated[str, Path(description="Enter username", min_length=5, max_length=20)],
    age: Annotated[int, Path(description="Enter age", ge=18, le=120)]
):
    """
    Страница пользователя с параметрами в адресной строке
    """
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
