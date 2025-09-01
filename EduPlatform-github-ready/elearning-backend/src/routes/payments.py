from flask import Blueprint, request, jsonify
from ..models.user import db
from ..models.course import Course
from ..models.ebook import Ebook
from ..models.enrollment import Enrollment, Purchase
import uuid

payments_bp = Blueprint('payments', __name__)

@payments_bp.route('/payments/process-course', methods=['POST'])
def process_course_payment():
    data = request.get_json() or {}
    for f in ['user_id','course_id','payment_method','amount']:
        if f not in data: return jsonify({'error': f'Campo {f} é obrigatório'}), 400
    user_id = data['user_id']; course_id = data['course_id']; amount = float(data['amount'])
    course = Course.query.get_or_404(course_id)
    exists = Enrollment.query.filter_by(user_id=user_id, course_id=course_id, is_active=True).first()
    if exists: return jsonify({'error':'Usuário já está inscrito neste curso'}), 400

    payment_id = str(uuid.uuid4())
    enrollment = Enrollment(user_id=user_id, course_id=course_id, progress=0.0)
    course.students_count = (course.students_count or 0) + 1
    db.session.add(enrollment); db.session.commit()

    return jsonify({'success': True, 'payment_id': payment_id, 'enrollment': {
        'user_id': user_id, 'course_id': course_id
    }}), 201

@payments_bp.route('/payments/process-ebook', methods=['POST'])
def process_ebook_payment():
    data = request.get_json() or {}
    for f in ['user_id','ebook_id','payment_method','amount']:
        if f not in data: return jsonify({'error': f'Campo {f} é obrigatório'}), 400
    user_id = data['user_id']; ebook_id = data['ebook_id']; amount = float(data['amount'])
    ebook = Ebook.query.get_or_404(ebook_id)
    exists = Purchase.query.filter_by(user_id=user_id, ebook_id=ebook_id, is_active=True).first()
    if exists: return jsonify({'error':'Usuário já comprou este ebook'}), 400

    payment_id = str(uuid.uuid4())
    purchase = Purchase(user_id=user_id, ebook_id=ebook_id, price_paid=amount)
    db.session.add(purchase); db.session.commit()

    return jsonify({'success': True, 'payment_id': payment_id, 'download_url': ebook.file_url}), 201

@payments_bp.route('/payments/statistics', methods=['GET'])
def get_payment_statistics():
    from sqlalchemy import func
    course_revenue = db.session.query(func.sum(Course.price * Course.students_count)).filter(Course.is_active==True).scalar() or 0
    ebook_revenue = db.session.query(func.sum(Purchase.price_paid)).filter(Purchase.is_active==True).scalar() or 0
    total_enrollments = Enrollment.query.filter_by(is_active=True).count()
    total_purchases = Purchase.query.filter_by(is_active=True).count()
    return jsonify({
        'total_revenue': float(course_revenue + ebook_revenue),
        'course_revenue': float(course_revenue),
        'ebook_revenue': float(ebook_revenue),
        'total_enrollments': total_enrollments,
        'total_purchases': total_purchases,
        'total_transactions': total_enrollments + total_purchases
    })
