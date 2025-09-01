from .models.user import db, User
from .models.course import Course
from .models.ebook import Ebook
from .main import app

def seed_database():
    with app.app_context():
        db.drop_all(); db.create_all()

        users = [User(username='admin', email='admin@eduplatform.com')]
        db.session.add_all(users)

        courses = [
            Course(title='React.js Completo', description='Do básico ao avançado', instructor='João Silva', price=199.0, category='Programação', rating=4.8, students_count=1200, duration_hours=12),
            Course(title='Design UX/UI Moderno', description='Interfaces modernas', instructor='Maria Santos', price=149.0, category='Design', rating=4.9, students_count=856, duration_hours=10),
            Course(title='Marketing Digital', description='Cresça seu negócio', instructor='Pedro Costa', price=99.0, category='Marketing', rating=4.7, students_count=2100, duration_hours=8),
            Course(title='Python para Data Science', description='Análise e ML', instructor='Ana Oliveira', price=249.0, category='Data Science', rating=4.8, students_count=934, duration_hours=15),
            Course(title='JavaScript Avançado', description='ES6+ e além', instructor='Carlos Mendes', price=179.0, category='Programação', rating=4.6, students_count=1500, duration_hours=14),
            Course(title='Photoshop Profissional', description='Edição e design', instructor='Lucia Ferreira', price=129.0, category='Design', rating=4.7, students_count=678, duration_hours=9),
        ]
        db.session.add_all(courses)

        ebooks = [
            Ebook(title='JavaScript Moderno', description='Guia completo JS', author='Tech Expert', price=29.0, category='Tecnologia', rating=4.9, pages=320, file_url='/files/javascript-moderno.pdf', cover_image_url='/images/js-ebook.jpg', preview_url='/previews/js-preview.pdf'),
            Ebook(title='Design Thinking', description='Inovação e resolução', author='Creative Mind', price=39.0, category='Design', rating=4.8, pages=280, file_url='/files/design-thinking.pdf', cover_image_url='/images/design-ebook.jpg', preview_url='/previews/design-preview.pdf'),
            Ebook(title='Growth Hacking', description='Estratégias de crescimento', author='Marketing Pro', price=25.0, category='Marketing', rating=4.7, pages=250, file_url='/files/growth-hacking.pdf', cover_image_url='/images/growth-ebook.jpg', preview_url='/previews/growth-preview.pdf'),
            Ebook(title='Python para Iniciantes', description='Introdução prática', author='Code Master', price=35.0, category='Programação', rating=4.6, pages=400, file_url='/files/python-iniciantes.pdf', cover_image_url='/images/python-ebook.jpg', preview_url='/previews/python-preview.pdf'),
            Ebook(title='Liderança Digital', description='Liderança na era digital', author='Business Leader', price=45.0, category='Negócios', rating=4.5, pages=300, file_url='/files/lideranca-digital.pdf', cover_image_url='/images/leadership-ebook.jpg', preview_url='/previews/leadership-preview.pdf'),
        ]
        db.session.add_all(ebooks)

        db.session.commit()
        print("✅ Base populada!")

if __name__ == '__main__':
    seed_database()
