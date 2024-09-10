# SQLAlchemy v1.x

# Query many users
all_users = (db.session
    .query(User)  # SELECT
    .filter(      # WHERE
        User.created >= dt(2024, 3, 1),
        User.email.endswith('@cern.ch'),
    )
    .order_by(User.created.desc())
    .limit(10)
).all()

# Insert a new user
db.session.add(User(...))
db.session.commit()

# Fetch a single user
user = db.session.query(User).filter_by(email="...").one()

# Update the user
user.confirmed_at = dt.utcnow()
db.session.commit()

# Delete a user
db.session.delete(user)
db.session.commit()
