from flask import Blueprint, request, jsonify
from ..models.user import db
from ..models.ebook import Ebook

ebooks_bp = Blueprint('ebooks', __name__)

@ebooks_bp.route('/ebooks', methods=['GET'])
def list_ebooks():
    q = Ebook.query.filter_by(is_active=True)
    category = request.args.get('category')
    search = request.args.get('search')
    if category:
        q = q.filter(Ebook.category==category)
    if search:
        like = f"%{search}%"
        q = q.filter(Ebook.title.ilike(like) | Ebook.description.ilike(like))
    return jsonify([e.to_dict() for e in q.order_by(Ebook.id.desc()).all()])

@ebooks_bp.route('/ebooks/popular', methods=['GET'])
def popular_ebooks():
    q = Ebook.query.filter_by(is_active=True).order_by(Ebook.rating.desc()).limit(6).all()
    return jsonify([e.to_dict() for e in q])

@ebooks_bp.route('/ebooks/<int:eid>', methods=['GET'])
def get_ebook(eid):
    e = Ebook.query.get_or_404(eid)
    return jsonify(e.to_dict())

@ebooks_bp.route('/ebooks', methods=['POST'])
def create_ebook():
    data = request.get_json() or {}
    e = Ebook(**{k:v for k,v in data.items() if k in Ebook().__dict__})
    db.session.add(e); db.session.commit()
    return jsonify(e.to_dict()), 201

@ebooks_bp.route('/ebooks/<int:eid>', methods=['PUT'])
def update_ebook(eid):
    e = Ebook.query.get_or_404(eid)
    data = request.get_json() or {}
    for k,v in data.items():
        if hasattr(e, k):
            setattr(e, k, v)
    db.session.commit()
    return jsonify(e.to_dict())

@ebooks_bp.route('/ebooks/<int:eid>', methods=['DELETE'])
def delete_ebook(eid):
    e = Ebook.query.get_or_404(eid)
    e.is_active = False
    db.session.commit()
    return jsonify({"success": True})
