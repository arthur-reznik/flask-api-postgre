from flask import Blueprint, jsonify,request,make_response, current_app
from werkzeug.security import check_password_hash
import jwt,datetime
from flask_api.Models.User import User


main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({"msg" : "raiz"})

@main.route('/login')
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    user = User.query.filter_by(name=auth.username).first()

    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'public_id' : user.public_id,
         'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, 
         current_app.config['SECRET_KEY'])

        return jsonify({'token' : token.decode('UTF-8')})

    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})
