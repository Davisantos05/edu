from flask import Blueprint, request, jsonify
from ..models.user import db, User

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json() or {}
    if 'username' not in data: return jsonify({'error':'username obrigatório'}), 400
    u = User(username=data['username'], email=data.get('email'))
    db.session.add(u); db.session.commit()
    return jsonify(u.to_dict()), 201

@user_bp.route('/users/<int:uid>', methods=['GET'])
def get_user(uid):
    u = User.query.get_or_404(uid)
    return jsonify(u.to_dict())

@user_bp.route('/users/<int:uid>', methods=['PUT'])
def update_user(uid):
    u = User.query.get_or_404(uid)
    data = request.get_json() or {}
    if 'username' in data: u.username = data['username']
    if 'email' in data: u.email = data['email']
    db.session.commit()
    return jsonify(u.to_dict())
