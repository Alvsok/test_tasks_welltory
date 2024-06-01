from sqlalchemy.orm import Session
from sqlalchemy import func, extract
from models import SessionLocal, User, HeartRate
from datetime import datetime


def query_users(min_age: int, gender: str, min_avg_heart_rate: float, date_from: datetime, date_to: datetime):
    """
    Извлекает пользователей из базы данных, которые удовлетворяют заданным критериям: старше заданного возраста,
    имеют заданный пол, и средний пульс выше заданного значения за определенный период времени.

    Аргументы:
    min_age : int - минимальный возраст пользователя.
    gender : str - пол пользователей.
    min_avg_heart_rate : float - минимальный средний пульс пользователя.
    date_from : datetime - начальная дата временного диапазона.
    date_to : datetime - конечная дата временного диапазона.

    Возвращает:
    list - список пользователей, удовлетворяющих критериям.
    """
    with SessionLocal() as session:
        # Создаём запрос, который одновременно фильтрует пользователей по возрасту, полу
        # и считает средний пульс, проверяя, что он выше заданного значения.
        users = session.query(User).join(HeartRate, User.id == HeartRate.user_id).filter(
            User.age > min_age,
            User.gender == gender,
            HeartRate.timestamp >= date_from,
            HeartRate.timestamp <= date_to
        ).group_by(User.id).having(
            func.avg(HeartRate.heart_rate) > min_avg_heart_rate
        ).all()

        return users


def query_for_user(user_id: int, date_from: datetime, date_to: datetime):
    """
    Возвращает топ 10 самых высоких средних значений пульса пользователя по часам за заданный период времени.

    Аргументы:
    user_id : int - идентификатор пользователя.
    date_from : datetime - начальная дата временного диапазона.
    date_to : datetime - конечная дата временного диапазона.

    Возвращает:
    list - список кортежей с часом (int) и средним значением пульса (float).
    """
    session = SessionLocal()
    try:
        results = session.query(
            extract('hour', HeartRate.timestamp).label('hour'),
            func.avg(HeartRate.heart_rate).label('avg_heart_rate')
        ).filter(
            HeartRate.user_id == user_id,
            HeartRate.timestamp >= date_from,
            HeartRate.timestamp <= date_to
        ).group_by(
            extract('hour', HeartRate.timestamp)
        ).order_by(
            func.avg(HeartRate.heart_rate).desc()
        ).limit(10).all()

        return results
    finally:
        session.close()
