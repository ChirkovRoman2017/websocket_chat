from fastapi import status, HTTPException


class TokenExpiredException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail="Токен истек")


class TokenNoFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail="Токен не найден")


UserAlreadyExistException = HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Пользователь уже существует")

PasswordMismatchException = HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Пароли не совпадают")

IncorrectEmailOrPasswordException = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Неверная почта или пароль")

NoJwtException = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Не валидный токен")

NoUserIdException = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="ID пользователя не найден")

ForbiddenException = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Недостаточно прав доступа")