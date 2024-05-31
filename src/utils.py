from sqlalchemy.orm import Session
from sqlalchemy import func, extract
from models import SessionLocal, User, HeartRate
from datetime import datetime


def query_users(min_age: int, gender: str, min_avg_heart_rate: float, date_from: datetime, date_to: datetime):
    session = SessionLocal()
    try:
        users = session.query(User).filter(
            User.age > min_age,
            User.gender == gender
        ).all()

        result = []

        for user in users:
            avg_heart_rate = session.query(func.avg(HeartRate.heart_rate)).filter(
                HeartRate.user_id == user.id,
                HeartRate.timestamp >= date_from,
                HeartRate.timestamp <= date_to
            ).scalar()

            if avg_heart_rate is not None and avg_heart_rate > min_avg_heart_rate:
                result.append(user)

        return result
    finally:
        session.close()


def query_for_user(user_id: int, date_from: datetime, date_to: datetime):
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
