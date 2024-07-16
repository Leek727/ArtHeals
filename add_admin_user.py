from app.models import User
from app import app, db
import sqlalchemy as sa

input("Enter to continue")

app.app_context().push()

results = db.session.query(User).filter().all()
print(f"Current users: {results}")

db.session.query(User).filter().delete()
db.session.commit()

u = User(username="admin")
u.set_password(str(input("Enter pwd: ")))
db.session.add(u)
db.session.commit()

print(db.session.query(User).filter(User.username=="admin").all())