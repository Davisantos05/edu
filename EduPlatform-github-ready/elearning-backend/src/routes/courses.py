from flask import Blueprint, request, jsonify
from ..models.user import db
from ..models.course import Course

courses_bp = Blueprint('courses', __name__)

@courses_bp.route('/courses', methods=['GET'])
def list_courses():
    q = Course.query.filter_by(is_active=True)
    category = request.args.get('category')
    search = request.args.get('search')
    if category:
        q = q.filter(Course.category==category)
    if search:
        like = f"%{search}%"
        q = q.filter(Course.title.ilike(like) | Course.description.ilike(like))
    return jsonify([c.to_dict() for c in q.order_by(Course.id.desc()).all()])

@courses_bp.route('/courses/featured', methods=['GET'])
def featured_courses():
    q = Course.query.filter_by(is_active=True).order_by(Course.rating.desc(), Course.students_count.desc()).limit(6).all()
    return jsonify([c.to_dict() for c in q])

@courses_bp.route('/courses/<int:cid>', methods=['GET'])
def get_course(cid):
    c = Course.query.get_or_404(cid)
    return jsonify(c.to_dict())

@courses_bp.route('/courses', methods=['POST'])
def create_course():
    data = request.get_json() or {}
    c = Course(**{k:v for k,v in data.items() if k in Course().__dict__})
    db.session.add(c); db.session.commit()
    return jsonify(c.to_dict()), 201

@courses_bp.route('/courses/<int:cid>', methods=['PUT'])
def update_course(cid):
    c = Course.query.get_or_404(cid)
    data = request.get_json() or {}
    for k,v in data.items():
        if hasattr(c, k):
            setattr(c, k, v)
    db.session.commit()
    return jsonify(c.to_dict())

@courses_bp.route('/courses/<int:cid>', methods=['DELETE'])
def delete_course(cid):
    c = Course.query.get_or_404(cid)
    c.is_active = False
    db.session.commit()
    return jsonify({"success": True})
