"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)
    

class User(db.Model):
    """User."""
    
    __tablename__= 'users'
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(50),
                           nullable=False)
    last_name = db.Column(db.String(50),
                          nullable=False)
    image_url = db.Column(db.String(1000),
                          nullable=False)
    
    def __repr__(self):
        """Show info about user."""
        
        u = self
        return f"<User {u.id} {u.first_name} {u.last_name} {u.image_url}>"


class Post(db.Model):
    """Post."""
    
    __tablename__= 'posts'
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.String(200),
                      nullable=False)
    content = db.Column(db.String(),
                        nullable=False)
    created_at = db.Column(db.DateTime(timezone=True))
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'),
                        nullable=False)
    tags = db.relationship('Tag',
                           secondary='posts_tags',
                           backref='posts1')
    
    def __repr__(self):
        """Show info about the post."""
        
        p = self
        return f"<Post {p.id} {p.title} {p.content} {p.created_at} {p.user_id} {p.tags}>"
    

class Tag(db.Model):
    """Tag."""
    
    __tablename__ = 'tags'
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(50),
                     nullable=False,
                     unique=True)
    posts = db.relationship('Post',
                            secondary='posts_tags',
                            backref='tags1')
    
    def __repr__(self):
        """Show info about tags."""
        
        t = self
        return f"<Tag {t.id} {t.name} {t.posts}>"
    

class PostTag(db.Model):
    
    __tablename__ = 'posts_tags'
    
    post_id = db.Column(db.Integer,
                        db.ForeignKey('posts.id'),
                        primary_key=True)
    tag_id = db.Column(db.Integer,
                       db.ForeignKey('tags.id'),
                       primary_key=True)
    
    def __repr__(self):
        """Show info from intersection table on posts and tags."""
        
        pt = self
        return f"<Tag {pt.post_id} {pt.tag_id}>"