# Create a new user
new_user = User(email="bobby@tabl.es")
db.session.add(new_user)
db.session.commit()  # QUIZ❓: What does this do?

# Fetch Bobby
bobby = db.session.query(User).get(1)
print(vars(bobby))

# Confirm Bobby
bobby.confirmed_at = dt.utcnow()
db.session.commit()
