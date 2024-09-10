# somewhat optimized version
user_profiles = (
    db.session.query(UserProfile)
    .join(User, User.id == UserProfile.user_id)
    .filter(
        db.func.date_part('year', User.created) == 2024,
    )
    .order_by(UserProfile.quota.desc())
    .limit(10)
)

for profile in user_profiles.yield_per(1000):
    if profile.system_info['vip']:
        total_vip_quota += profile.quota


# hyper-optimized version
total_vip_quota = (
    db.session.query(func.sum(UserProfile.quota))
    .join(User, User.id == UserProfile.user_id)
    .filter(
        db.func.date_part('year', User.created) == 2024,
        UserProfile.system_info['vip'] == True,
    )
    .order_by(UserProfile.quota.desc())
    .limit(10)
).scalar()
