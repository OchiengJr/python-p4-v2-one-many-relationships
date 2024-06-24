from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Define custom metadata with naming convention for foreign keys
metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

# Create SQLAlchemy instance with custom metadata
db = SQLAlchemy(metadata=metadata)


class Employee(db.Model):
    """Employee model for storing employee information."""

    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    hire_date = db.Column(db.Date)

    def __repr__(self):
        return f"<Employee {self.id}, {self.name}, {self.hire_date}>"


class Onboarding(db.Model):
    """Onboarding model for tracking employee onboarding process."""

    __tablename__ = "onboardings"

    id = db.Column(db.Integer, primary_key=True)
    orientation = db.Column(db.DateTime)
    forms_complete = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Onboarding {self.id}, {self.orientation}, {self.forms_complete}>"


class Review(db.Model):
    """Review model for storing employee performance reviews."""

    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    summary = db.Column(db.String)

    def __repr__(self):
        return f"<Review {self.id}, {self.year}, {self.summary}>"
