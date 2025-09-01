from datetime import datetime
from .user import db

class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    enrolled_at = db.Column(db.DateTime, default=datetime.utcnow)
    progress = db.Column(db.Float, default=0.0)
    completed_at = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean, default=True)

class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    ebook_id = db.Column(db.Integer, db.ForeignKey('ebook.id'), nullable=False)
    purchased_at = db.Column(db.DateTime, default=datetime.utcnow)
    price_paid = db.Column(db.Float, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
