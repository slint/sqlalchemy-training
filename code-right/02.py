users = (db.session
    .query(   # SELECT
        User.email,
        User.created,
     )        # FROM users (implicit)
    .filter(  # WHERE
        User.created >= dt(2024, 3, 1),
        User.email.endswith('@cern.ch'),
    )
    .order_by(User.created.desc())  # ORDER BY
    .limit(10)                      # LIMIT
).all()
