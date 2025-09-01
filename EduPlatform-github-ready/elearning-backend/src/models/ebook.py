from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from .user import db

class Ebook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, default="")
    author = db.Column(db.String(120))
    price = db.Column(db.Float, default=0.0)
    category = db.Column(db.String(80))
    rating = db.Column(db.Float, default=0.0)
    pages = db.Column(db.Integer, default=0)
    file_url = db.Column(db.String(255))
    cover_image_url = db.Column(db.String(255))
    preview_url = db.Column(db.String(255))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id, "title": self.title, "description": self.description,
            "author": self.author, "price": self.price, "category": self.category,
            "rating": self.rating, "pages": self.pages, "file_url": self.file_url,
            "cover_image_url": self.cover_image_url, "preview_url": self.preview_url,
            "is_active": self.is_active
        }
