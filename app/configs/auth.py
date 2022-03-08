from flask_httpauth import HTTPTokenAuth
from app.models.admin_model import AdminModel

auth = HTTPTokenAuth()

@auth.verify_token
def verify_token(adm_key: str):
    user = AdminModel.query.filter_by(adm_key=adm_key).first()

    return user
    