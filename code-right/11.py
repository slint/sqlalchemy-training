# SQLAlchemy v2.x

# Query many users (new `select()`, `execute()` syntax and `scalars()`)
all_users = db.session.execute(
    db
    .select(User.email, User.profile.quota)
    .where(
        User.created >= dt(2024, 3, 1),
        User.email.endswith('@cern.ch'),
    )
    .order_by(User.created.desc())
    .limit(10)
).scalars()

all_users[0].email  # the editor will autocomplete the columns

# Insert a new user (no change)
db.session.add(User(...))
db.session.commit()

# Fetch a single user (new `select()` syntax and `scalar_one()`)
user = db.session.execute(db.select(User).filter_by(email="...")).scalar_one()

# Update the user (no change)
user.confirmed_at = dt.utcnow()
db.session.commit()

# Delete a user (no change)
db.session.delete(user)
db.session.commit()
