# 1. Fetch all users (👉 how many users are there in total?)
users = db.session.query(User).all()

# 2. Sort users by quota
users_by_quota = sorted(users, key=lambda u: u.profile.quota, reverse=True)
# 3. Get top 10 users by quota
top_10_users_by_quota = users_by_quota[:10]

# 4. Calculate total quota of VIP users
total_vip_quota = 0
for user in top_10_users_by_quota:
    # 5. Filter VIP users (👉 can the conditions for this become complex?)
    if user.profile.system_info["vip"]:
        total_vip_quota += user.profile.quota

# 👉 how often will this code run? can we maybe cache this?
print(total_vip_quota)
