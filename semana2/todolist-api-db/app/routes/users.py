from app.crypt import bcrypt
from app.db import db
from app.models.tasks import Task
from app.models.users import User
from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from utils import response_error, response_success

user_route = Blueprint("user_route", __name__)


@user_route.route("/users")
def get_users():
    try:
        users = User.query.all()
        serialized_users = [user.to_json() for user in users]
        return response_success(serialized_users)
    except Exception as e:
        return response_error(str(e))


@user_route.route("/users/<int:user_id>")
def get_user(user_id):
    try:
        user = User.query.get(user_id)
        return response_success(user.to_json())
    except Exception as e:
        return response_error(str(e))


@user_route.route("/users", methods=["POST"])
def add_user():
    try:
        user = User(**request.get_json())
        user.password = bcrypt.generate_password_hash(
            "user.password", rounds=12
        ).decode("utf-8")
        db.session.add(user)
        db.session.commit()

        return response_success("Usuario creado correctamente", 201)
    except IntegrityError:
        return response_error("El username o email ya existen")
    except Exception as e:
        return response_error(str(e))


@user_route.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    try:
        user = User.query.get(user_id)

        if user is None:
            return response_error("User not found")

        new_user = request.json
        user.name = new_user.get("name", user.name)
        user.lastname = new_user.get("lastname", user.lastname)
        user.email = new_user.get("email", user.email)
        user.username = new_user.get("username", user.username)
        user.address = new_user.get("address", user.address)
        user.phone = new_user.get("phone", user.phone)

        db.session.commit()

        return response_success("Tarea actualizada correctamente")
    except Exception as e:
        return response_error(str(e))


@user_route.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    try:
        # verificar que no tenga tareas relacionadas primero
        tasks_by_user = Task.query.filter_by(user_id=user_id).all()

        if len(tasks_by_user) is 0:
            user = User.query.get(user_id)

            if not user:
                return response_error("User not found")

            db.session.delete(user)
            db.session.commit()
            return response_success("User deleted")

        return response_success(
            "El usuario no puede ser eliminado porque tiene tareas pendientes"
        )
    except Exception as e:
        return response_error(str(e))


@user_route.route("/users/login", methods=["POST"])
def login():
    try:
        body = request.get_json()
        email = body.get("email")
        password = body.get("password")

        user = User.query.filter_by(email=email).first()

        if not user:
            print("User not found")
            return response_error("Email y/o Password incorrecto")
        # param 1: es el password encriptado
        # param 2: password sin encriptar
        if bcrypt.check_password_hash(user.password, password):
            return response_error("Email y/o Password incorrecto")

        return response_success(user.to_json())

    except Exception as e:
        return response_error(str(e))
