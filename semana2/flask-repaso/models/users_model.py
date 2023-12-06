# pip install Flask-Migrate
# flask db upgrade
# https://github.com/12aptor/flask_sqlalchemy_boilerplate

from db import db
from sqlalchemy import Integer, String, Text, Boolean, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class UserModel(db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    email: Mapped[str] = mapped_column(String(200), nullable=False)
    password: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[int] = mapped_column(Boolean, nullable=False, default=False)
    created_at: Mapped[str] = mapped_column(
        DateTime, nullable=False, default=func.current_timestamp()
    )
    updated_at: Mapped[str] = mapped_column(
        DateTime, nullable=False, default=func.current_timestamp()
    )
    rol_id: Mapped[int] = mapped_column(Integer, ForeignKey('rol.id'), nullable=False)
