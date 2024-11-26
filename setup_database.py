from werkzeug.security import generate_password_hash
from models import db, User, Item, Bid
from app import app

def seed_database():
    """Seed the database with test data."""
    # Create test users with password hashes
    user1 = User(name="Alice", email="alice@example.com", password_hash=generate_password_hash("password123"))
    user2 = User(name="Bob", email="bob@example.com", password_hash=generate_password_hash("securepass456"))
    db.session.add_all([user1, user2])

    # Create test items
    item1 = Item(name="Antique Vase", description="A rare antique vase.", starting_bid=50.0)
    item2 = Item(name="Vintage Clock", description="A vintage grandfather clock.", starting_bid=100.0)
    db.session.add_all([item1, item2])

    db.session.commit()
    print("Database seeded with test data!")

def setup_database():
    """Ensure the database is created."""
    with app.app_context():
        db.create_all()  # Create tables
        print("Database created successfully!")
        seed_database()  # Seed with test data

if __name__ == "__main__":
    setup_database()
