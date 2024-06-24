#!/usr/bin/env python3
# server/seed.py

import datetime
from app import app
from models import db, Employee, Review, Onboarding

def seed_database():
    with app.app_context():
        try:
            # Delete all existing rows in tables
            Employee.query.delete()
            Review.query.delete()
            Onboarding.query.delete()

            # Add Employee instances to database
            uri = Employee(name="Uri Lee", hire_date=datetime.datetime(2022, 5, 17))
            tristan = Employee(name="Tristan Tal", hire_date=datetime.datetime(2020, 1, 30))
            db.session.add_all([uri, tristan])
            db.session.commit()

            # Add Review instances to database with 1..many relationship
            uri_2023 = Review(year=2023, summary="Great web developer!")
            tristan_2021 = Review(year=2021, summary="Good coding skills, often late to work")
            tristan_2022 = Review(year=2022, summary="Strong coding skills, takes long lunches")
            tristan_2023 = Review(year=2023, summary="Awesome coding skills, dedicated worker")
            db.session.add_all([uri_2023, tristan_2021, tristan_2022, tristan_2023])
            db.session.commit()

            # Add Onboarding instances to database with 1..1 relationship
            uri_onboarding = Onboarding(orientation=datetime.datetime(2023, 3, 27))
            tristan_onboarding = Onboarding(
                orientation=datetime.datetime(2020, 1, 20, 14, 30), forms_complete=True
            )
            db.session.add_all([uri_onboarding, tristan_onboarding])
            db.session.commit()

            print("Database seeding completed successfully.")

        except Exception as e:
            db.session.rollback()
            print(f"Error occurred during database seeding: {str(e)}")

if __name__ == "__main__":
    seed_database()
