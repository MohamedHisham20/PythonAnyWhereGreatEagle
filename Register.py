from database import Users, db
from extensions import bcrypt
from flask import request, jsonify, Blueprint
from flask_cors import CORS


register = Blueprint("register", __name__, static_folder="static")

#register route using sqlalchemy and add the user into the database
@register.route('/register', methods=['POST'])
def register_1():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    name = data.get('name')
    age = data.get('age')
    email = data.get('email')

    #check if email and password are provided
    if not email or not password:
        return jsonify({"error": "Please provide both email and password"}), 400

    #check if user exists in the db
    user = Users.query.filter_by(email=email).first()
    if user:
        return jsonify({"error": "User already exists"}), 400

    #hash the password
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    #add the user to the database
    new_user = Users(username=username, password=hashed_password, name=name, age=age, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201

