from secrets import token_urlsafe
from flask import current_app, request, jsonify
from http import HTTPStatus
from app.models.admin_model import AdminModel
from app.configs.auth import auth
from app.services.register_service import validate_request


def signup():
    session = current_app.db.session

    admin_data = request.get_json()

    validate_data = validate_request(admin_data)

    validate_data['adm_key'] = token_urlsafe(16)

    password_to_hash = validate_data.pop("password")

    new_admin = AdminModel(**validate_data)

    new_admin.password = password_to_hash


    session.add(new_admin)
    session.commit()

    return jsonify(new_admin), HTTPStatus.CREATED



def signin():
    admin_data =  request.get_json()

    admin: AdminModel = AdminModel.query.filter_by(email = admin_data['email']).first()

    if not admin:
        return {"error": "email not found"}, HTTPStatus.UNAUTHORIZED
    
    if not admin.verify_password(admin_data['password']):
        return {"error": "email and password missmatch"}, HTTPStatus.UNAUTHORIZED


    return jsonify({"admin_key": admin.adm_key}), HTTPStatus.OK

    # Criar exception para verificar as chaves recebidas pelo JSON




# CRIAR FUNÇÕES QUE O ADM PODERÁ UTILIZAR
