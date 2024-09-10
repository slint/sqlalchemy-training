# Create a new user
new_user = User(email="bobby@tabl.es")
db.session.add(new_user)
db.session.commit()

# Fetch Bobby back
bobby = db.session.query(User).get(new_user.id)

print(vars(bobby))  # QUIZ❓: What values do we get here?
...

# Confirm Bobby
bobby.confirmed_at = dt.utcnow()
db.session.commit()

# Add a profile to Bobby
full_name = input("Enter Bobby Tables' full name:")
profile = UserProfile(user_id=bobby.id, full_name=full_name, system_info={})
db.session.add(profile)
db.session.commit()

# QUIZ❓: Is the code above secure?

# Store some system info about Bobby
bobby.profile.system_info["vip"] = False
db.session.commit()
