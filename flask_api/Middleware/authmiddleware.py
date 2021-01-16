from flask import jsonify, current_app, request
from functools import wraps
import jwt
from flask_api.Models.User import User

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401
        try: 
            data = jwt.decode(token, current_app.config['SECRET_KEY'],algorithm='SH256')
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401
    
        return f(current_user, *args, **kwargs)
    return decorated


def isAdmin(f):
    @wraps(f)
    def decorated(current_user,*args,**kwargs):
        if not current_user.admin:
            return jsonify({"message" : "Insuficient Permission"})
        
        return f(current_user, *args, **kwargs)
    return decorated