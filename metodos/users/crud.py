from db import USERS
from validations import validate_email

def list_users():
    return [user for user in USERS]

def create_users(username, email, password):
    if not validate_email(email):
        return "email invalido"
    
    id = len(USERS) + 1
    new_user = {
        'id': id,
        'username': username,
        'email': email,
        'password': password
    }
    USERS.append(new_user)
    return "email cadastrado com exito"

def update_user (id, username, email, password):
    if not validate_email(email):
        return "email invalido"
    USERS [id - 1] = {
        'id': id,
        'username': username,
        'email': email,
        'password': password
    }
    return 'usuario atualizado com exito'

