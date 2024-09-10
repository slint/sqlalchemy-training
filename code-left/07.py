def use_quota(email, units):
    user = db.session.query(User).filter(User.email == email).one()
    user.profile.quota -= units

def apply_vip_status(email):
    user = db.session.query(User).filter(User.email == email).one()
    if user.profile.quota > 15:
        info = user.profile.system_info
        info["vip"] = True
        user.profile.system_info = info

# Bobby uses 32 units of his quota (originally 42)
with db.session.begin_nested():
    use_quota("bobby@tabl.es", 32)
    apply_vip_status("bobby@tabl.es")
db.session.commit()

