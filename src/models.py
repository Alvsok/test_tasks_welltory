from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

engine = create_engine('postgresql://weuser:wepassword@localhost:5432/welltory_db')


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    gender = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    heart_rates = relationship('HeartRate', back_populates='user')


class HeartRate(Base):
    __tablename__ = 'heart_rates'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    timestamp = Column(DateTime, nullable=False, index=True)
    heart_rate = Column(Float, nullable=False)
    user = relationship('User', back_populates='heart_rates')
    __table_args__ = (
        Index('ix_heart_rates_user_id_timestamp', 'user_id', 'timestamp'),
    )


Base.metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
