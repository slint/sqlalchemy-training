class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    confirmed_at = db.Column(db.DateTime)
    created = db.Column(db.DateTime, default=dt.utcnow)







class UserProfile(db.Model):
    __tablename__ = 'user_profile'

    user_id = db.Column(db.Integer, db.ForeignKey(User.id), primary_key=True)
    user = db.relationship(User, backref='profile')

    full_name = db.Column(db.String, nullable=False)
    quota = db.Column(db.Integer, default=0)
    system_info = db.Column(db.JSON)
