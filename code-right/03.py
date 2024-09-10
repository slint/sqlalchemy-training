members = (db.session.query(
        User.email,
        sa.case(
            {CommunityMember.role == 'owner': 'Owner'},
            else_='Member'
        ).label('community_role'),
        db.func.date_part('year', CommunityMember.created).label('joined_year'),
    )
    .join(CommunityMember, User.id == CommunityMember.user_id)
    .filter(
        User.email.endswith('@cern.ch'),
        CommunityMember.created.between(
          dt(2018, 1, 1),
          db.func.now() - db.func.interval('1 month'),
        ),
    )
).all()
