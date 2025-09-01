from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from .user import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, default="")
    instructor = db.Column(db.String(120))
    price = db.Column(db.Float, default=0.0)
    category = db.Column(db.String(80))
    rating = db.Column(db.Float, default=0.0)
    students_count = db.Column(db.Integer, default=0)
    duration_hours = db.Column(db.Integer, default=0)
    image_url = db.Column(db.String(255))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id, "title": self.title, "description": self.description,
            "instructor": self.instructor, "price": self.price, "category": self.category,
            "rating": self.rating, "students_count": self.students_count,
            "duration_hours": self.duration_hours, "image_url": self.image_url,
            "is_active": self.is_active
        }
