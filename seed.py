from models import db, connect_db, User, Post, Tag, PostTag
from app import app

# Create all tables

db.drop_all()
db.create_all()

# If table isn't empty, empty it.

User.query.delete()
Post.query.delete()
Tag.query.delete()

# Add users
jared = User(first_name="Jared", last_name="Glenn", image_url="https://scontent-den4-1.xx.fbcdn.net/v/t1.6435-1/87663753_10221059310328399_1388140843180752896_n.jpg?stp=dst-jpg_p200x200&_nc_cat=106&ccb=1-7&_nc_sid=7206a8&_nc_ohc=E4hSzCMEi0YAX92sEMk&_nc_ht=scontent-den4-1.xx&cb_e2o_trans=t&oh=00_AfAhyO6taWV04aImPoPdDYzlKj7GJsZmzkqmDdge7T8Keg&oe=6532D2DC")
beka = User(first_name="Beka", last_name="Glenn", image_url="https://scontent-den4-1.xx.fbcdn.net/v/t1.6435-9/77198748_2518515914850354_7458161304495194112_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=liWiZFnvDk0AX8OaMWY&_nc_ht=scontent-den4-1.xx&cb_e2o_trans=t&oh=00_AfBAzY4kOZkfq7nOdE-JhRBJ07IBHWovMy56psETiu-zbw&oe=6532DEDB")
ethan = User(first_name="Ethan", last_name="Glenn", image_url="https://upload.wikimedia.org/wikipedia/en/e/e7/Steve_%28Minecraft%29.png?20220417165835")
ellie = User(first_name="Ellie", last_name="Glenn", image_url="https://www.brooklinebooksmith.com/sites/brooklinebooksmith.com/files/9780763665104.spt_.1.jpg")

# Add posts
hookie = Post(title="Hookie", content="Lookie lookie, I got Hookie!", user_id=1)
im_amazing = Post(title="I'm Amazing!", content="Seriously, have you noticed how amazing I am? I'm really a heck of a guy, and I wish I would let everyone know. Anyways, I'm amazing, and I'm glad you're taking a moment to think about it and I hope you really take that to heart.", user_id=1)
future = Post(title="Back to the Future", content="Whoa! This is heavy, Doc!", user_id=1)

# Add tags
quote = Tag(name="Quote")
brag = Tag(name="Brag")

db.session.add(jared)
db.session.add(beka)
db.session.add(ethan)
db.session.add(ellie)

db.session.add(hookie)
db.session.add(im_amazing)
db.session.add(future)

db.session.add(quote)
db.session.add(brag)

db.session.commit()

# Add post-tags
hookie_tag = PostTag(post_id=1, tag_id=1)
im_amazing_tag = PostTag(post_id=2, tag_id=2)
future_tag = PostTag(post_id=3, tag_id=1)

db.session.add(hookie_tag)
db.session.add(im_amazing_tag)
db.session.add(future_tag)

# Commit

db.session.commit()