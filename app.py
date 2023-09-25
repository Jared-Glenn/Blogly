"""Blogly application."""

from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post, Tag
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "shhhhhh"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
app.app_context().push()
db.create_all()


@app.route('/')
def home():
    """Main blog page. Shows list of all users on site."""
    
    users = User.query.all()
    posts = Post.query.all()
    tags = Tag.query.all()
    
    return render_template("index.html", users=users, posts=posts, tags=tags)


@app.route('/users')
def users():
    """Main blog page. Shows list of all users on site."""
    
    users = User.query.all()
    posts = Post.query.all()
    
    return render_template("index.html", users=users, posts=posts)


################## USERS #####################

# New Users

@app.route('/users/new')
def new_user():
    """Form for adding new users."""
    
    return render_template("new_user.html")


@app.route('/users/new', methods=["POST"])
def add_user():
    """Add the new user and redirect to the user's page."""
    
    first_name = request.form["first-name"]
    last_name = request.form["last-name"]
    image_url = request.form["image-url"]
    
    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()
    
    return redirect(f"/users/{new_user.id}")

# User Info

@app.route('/users/<u_id>')
def user_page(u_id):
    """Page template for each individual user."""
    
    user = User.query.get(u_id)
    posts = Post.query.filter_by(user_id=u_id).all()
    
    return render_template("user.html", user=user, posts=posts)

# Edit User

@app.route('/users/<user_id>/edit', methods=["GET"])
def edit_user(user_id):
    """Edit an individual user."""
    
    user = User.query.get(user_id)
    
    return render_template("edit_user.html", user=user)


@app.route('/users/<user_id>/edit', methods=["POST"])
def apply_edit(user_id):
    """Edit an individual user."""
    
    user_to_edit = User.query.get_or_404(user_id)
    
    user_to_edit.first_name = request.form["first-name"]
    user_to_edit.last_name = request.form["last-name"]
    user_to_edit.image_url = request.form["image-url"]
    
    db.session.commit()
    
    return redirect(f"/users/{user_id}")

# Delete User

@app.route('/users/<user_id>/delete')
def delete_page(user_id):
    """Delete a certain user."""
    
    user_to_delete = User.query.get_or_404(user_id)
    
    db.session.delete(user_to_delete)
    db.session.commit()
    
    return redirect("/users")


################## POSTS #####################

# Add Post for User

@app.route('/users/<user_id>/posts/new')
def show_post_form(user_id):
    """Show the form for making a new post."""
    
    user_to_post = User.query.get_or_404(user_id)
    
    return render_template("post_form_page.html", user=user_to_post)


@app.route('/users/<user_id>/posts/new', methods=["POST"])
def create_post(user_id):
    """Add a post for a user."""
    
    post_title = request.form["post-title"]
    post_content = request.form["post-content"]
    
    created = datetime.now()
    
    new_post = Post(title=post_title, content=post_content, created_at=created, user_id=user_id)
    db.session.add(new_post)
    db.session.commit()
    
    return redirect(f"/posts/{new_post.id }")

# Display Post

@app.route('/posts/<post_id>')
def show_post(post_id):
    """Show a post."""
    
    post = Post.query.get_or_404(post_id)
    user = User.query.get_or_404(post.user_id)
    
    return render_template("post.html", post=post, user=user)

# Edit Post

@app.route('/posts/<post_id>/edit')
def show_post_edit_form(post_id):
    """Show the form for editing a post."""
    
    post = Post.query.get(post_id)
    
    return render_template("edit_post.html", post=post)


@app.route('/posts/<post_id>/edit', methods=["POST"])
def apply_post_edit(post_id):
    """Edit an individual user."""
    
    post_to_edit = Post.query.get_or_404(post_id)
    
    post_to_edit.title = request.form["post-title"]
    post_to_edit.content = request.form["post-content"]
    
    db.session.commit()
    
    return redirect(f"/posts/{post_id}")


# Delete Post

@app.route('/posts/<post_id>/delete')
def delete_post(post_id):
    """Delete an individual post."""
    
    post_to_delete = Post.query.get_or_404(post_id)
    user = User.query.get_or_404(post_to_delete.user_id)
    
    db.session.delete(post_to_delete)
    db.session.commit()
    
    return redirect(f"/users/{user.id}")


################## POSTS #####################

# List all tags.

@app.route('/tags')
def tags_list():
    """List all tags."""
    
    tags = Tag.query.all()
    
    return render_template("tag_list.html", tags=tags)


# Show tag info.

@app.route('/tags/<tag_id>')
def show_tag_detail(tag_id):
    pass


# Make a new tag.

@app.route('/tags/new')
def new_tag_form():
    pass


@app.route('/tags/new', methods=['POST'])
def create_new_tag():
    pass


# Edit a tag.

@app.route('/tags/<tag_id>/edit')
def edit_tag_form(tag_id):
    pass


@app.route('/tags/<tag_id>/edit', methods=['POST'])
def edit_tag(tag_id):
    pass


# Delete a tag.

@app.route('/tags/<tag_id>/delete', methods=['POST'])
def delete_tag(tag_id):
    pass


if __name__ == '__main__':
    app.run()