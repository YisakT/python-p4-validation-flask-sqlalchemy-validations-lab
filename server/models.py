# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import validates
# db = SQLAlchemy()

# class Author(db.Model):
#     __tablename__ = 'authors'
#     # Add validations and constraints 

#     id = db.Column(db.Integer, primary_key=True)
#     name= db.Column(db.String, unique=True, nullable=False)
#     phone_number = db.Column(db.String)
#     created_at = db.Column(db.DateTime, server_default=db.func.now())
#     updated_at = db.Column(db.DateTime, onupdate=db.func.now())

#     def __repr__(self):
#         return f'Author(id={self.id}, name={self.name})'
    
#     @validates('name')
#     def validates_name(self,key,value):
#         if value == "":
#             raise ValueError("Name can not be empty")
#         return value
#     @validates('phone_number')
#     def validates_phone_number(self,key,phone_number):
#         if len(phone_number) != 10:
#             raise ValueError("Phone number must have 10 digits.")
#         else:
#             return phone_number

# class Post(db.Model):
#     __tablename__ = 'posts'
#     # Add validations and constraints 

#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String, nullable=False)
#     content = db.Column(db.String)
#     category = db.Column(db.String)
#     summary = db.Column(db.String)
#     created_at = db.Column(db.DateTime, server_default=db.func.now())
#     updated_at = db.Column(db.DateTime, onupdate=db.func.now())

#     @validates('content')
#     def validate_content(sefl,key,content):
#         if len(content) <= 250:
#             raise ValueError("Content can not be 250 characters long")
#         else:
#             return content
#     @validates('summary')
#     def validate_summary(sefl,key,summary):
#         if len(summary) >= 250:
#             raise ValueError("Summary must be less than 250 characters long")
#         else:
#             return summary
        
#     @validates("category")
#     def validate_category(self,key,category):
#         if category  not in ["Fiction","Non-Fiction"]:
#             raise ValueError("Catagory must be Fiction or Non-Fiction")
#         return category
    
#     @validates('title')
#     def validates_title(self,key,title):
#         if title not in ["Won't Believe","Secret","Top","Guess"]:
#             raise ValueError("Title is not click bait.")
#         return title
    

#     def __repr__(self):
#         return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'
    
    @validates('name')
    def validates_name(self, key, value):
        if not value:
            raise ValueError("Name cannot be empty")
        return value
    
    @validates('phone_number')
    def validates_phone_number(self, key, phone_number):
        if len(phone_number) != 10 or not phone_number.isdigit():
            raise ValueError("Phone number must have 10 digits and only contain numbers.")
        return phone_number

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('content')
    def validate_content(self, key, content):
        if len(content) <= 250:
            raise ValueError("Content must be at least 250 characters long")
        return content

    @validates('summary')
    def validate_summary(self, key, summary):
        if len(summary) >= 250:
            raise ValueError("Summary must be less than 250 characters long")
        return summary
        
    @validates('category')
    def validate_category(self, key, category):
        if category not in ["Fiction", "Non-Fiction"]:
            raise ValueError("Category must be 'Fiction' or 'Non-Fiction'")
        return category
    
    @validates('title')
    def validate_title(self,key,title):
        clickbait_words = ["Won't Believe","Secret","Top","Guess"]
        if title not in clickbait_words:
            raise ValueError("title not a click bait")
        return title

    
    def __repr__(self):
        return f'Post(id={self.id}, title={self.title}, content={self.content}, summary={self.summary})'