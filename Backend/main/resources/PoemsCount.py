# Archivo para el recurso de conteo de poemas

from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import PoemModel
from main.models import UserModel
from main.models import RatingModel
from datetime import datetime
from sqlalchemy import func
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from main.auth.decorators import admin_required
from main.auth import decorators

# Utilizo una clase Resources como recurso
class PoemsCount(Resource):
        
    # Obtengo recurso
    @jwt_required(optional=True)
    def get(self):
        total_poems = db.session.query(PoemModel).count()
        return total_poems, 200
        
    # # @app.route('/poems/count', methods=['GET'])
    # # Obtener cantidad de poemas
    # @jwt_required(optional=True)
    # def count(self):
    #     current_identity = get_jwt_identity()
    #     if current_identity:
    #         poems_count = db.session.query(func.count(PoemModel.id)).filter(PoemModel.user_id != current_identity).scalar()
    #     else:
    #         poems_count = db.session.query(func.count(PoemModel.id)).scalar()
    #     return jsonify({"count": poems_count})