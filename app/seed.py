import sys
import os
import csv
import random

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../'))

from app import create_app, db
from app.models import Episode, Guest, Appearance

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Use correct path
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'seed.csv')

    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            episode_date = row['Show']
            episode_number = int(row['YEAR'])  # Not ideal, but using as placeholder

            guest_name = row['Raw_Guest_List']
            guest_occupation = row['GoogleKnowlege_Occupation']
            rating = random.randint(1, 5)

            # Create or find episode
            episode = Episode.query.filter_by(date=episode_date, number=episode_number).first()
            if not episode:
                episode = Episode(date=episode_date, number=episode_number)
                db.session.add(episode)

            # Create or find guest
            guest = Guest.query.filter_by(name=guest_name).first()
            if not guest:
                guest = Guest(name=guest_name, occupation=guest_occupation)
                db.session.add(guest)

            db.session.commit()  # ensure IDs exist

            # Add appearance
            appearance = Appearance(
                episode_id=episode.id,
                guest_id=guest.id,
                rating=rating
            )
            db.session.add(appearance)

        db.session.commit()
        print("✅ Database seeded successfully!")
