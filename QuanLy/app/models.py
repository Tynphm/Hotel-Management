from sqlalchemy import Column, Integer, Float, String, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app import db, app
from enum import Enum as RoleEnum
import hashlib
from flask_login import UserMixin



class UserRole(RoleEnum):
    ADMIN = 1
    USER = 2


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    avatar = Column(String(255),
                    default='https://png.pngtree.com/png-clipart/20220111/original/pngtree-flat-hotel-logoicon-graphic-icon-png-image_7085107.png')
    user_role = Column(Enum(UserRole), default=UserRole.USER)


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    image = Column(String(512), nullable=True)
    price = Column(Float, default=0)
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()

        existing_user = User.query.filter_by(username='admin').first()
        if not existing_user:

            u = User(
                name='admin',
                username='admin',
                password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
                user_role=UserRole.ADMIN
            )
            db.session.add(u)
            db.session.commit()

    with app.app_context():
        hotel1 = Category(name='Simple')
        hotel2 = Category(name='Couple')
        hotel3 = Category(name='Traditional')

        db.session.add_all([hotel1, hotel2, hotel3])
        db.session.commit()

        products = [{
            "name": "Phòng Vip 1",
            "price": 17000000,
            "image": "https://saigon.newworldhotels.com/wp-content/uploads/sites/18/2014/05/NWSGN-Club-King-Room-021-1024x704.jpg",
            "category_id": 1
        }, {
            "name": "Phòng Vip 2",
            "price": 37000000,
            "image": "https://saigon.newworldhotels.com/wp-content/uploads/sites/18/2024/08/Deluxe-with-Balcony793-535-1.png",
            "category_id": 2
        }, {
            "name": "Phòng suite",
            "price": 24000000,
            "image": "https://saigon.newworldhotels.com/wp-content/uploads/sites/18/2014/05/NWSGN-Premier-King-Room1-1024x704.jpg",
            "category_id": 1
        }, {
            "name": "Phòng Deluxe",
            "price": 37000000,
            "image": "https://saigon.newworldhotels.com/wp-content/uploads/sites/18/2014/05/Deluxe-Suite-Living-Room-793x535.jpg",
            "category_id": 2
        }, {
            "name": "Phòng Couple",
            "price": 17000000,
            "image": "https://saigon.newworldhotels.com/wp-content/uploads/sites/18/2014/05/NWSGN-Director-Suite-Living-Room.jpg",
            "category_id": 1
        }, {
            "name": " Phòng Tripple ",
            "price": 37000000,
            "image": "https://saigon.newworldhotels.com/wp-content/uploads/sites/18/2024/08/Deluxe-with-Balcony793-535-3.png",
            "category_id": 2
        }, {
            "name": "Phòng Vip 1",
            "price": 17000000,
            "image": "https://saigon.newworldhotels.com/wp-content/uploads/sites/18/2014/05/NWSGN-Club-King-Room-021-1024x704.jpg",
            "category_id": 1
        }, {
            "name": "Phòng Vip 2",
            "price": 37000000,
            "image": "https://saigon.newworldhotels.com/wp-content/uploads/sites/18/2024/08/Deluxe-with-Balcony793-535-1.png",
            "category_id": 2
        }, {
            "name": "Phòng suite",
            "price": 24000000,
            "image": "https://saigon.newworldhotels.com/wp-content/uploads/sites/18/2014/05/NWSGN-Premier-King-Room1-1024x704.jpg",
            "category_id": 1
        }, {
            "name": "Phòng Deluxe",
            "price": 37000000,
            "image": "https://saigon.newworldhotels.com/wp-content/uploads/sites/18/2014/05/Deluxe-Suite-Living-Room-793x535.jpg",
            "category_id": 2
        }, {
            "name": "Phòng Couple",
            "price": 17000000,
            "image": "https://saigon.newworldhotels.com/wp-content/uploads/sites/18/2014/05/NWSGN-Director-Suite-Living-Room.jpg",
            "category_id": 1
        }, {
            "name": " Phòng Tripple ",
            "price": 37000000,
            "image": "https://saigon.newworldhotels.com/wp-content/uploads/sites/18/2024/08/Deluxe-with-Balcony793-535-3.png",
            "category_id": 2
        }]

        for p in products:
            existing_product = Product.query.filter_by(name=p["name"]).first()
            if not existing_product:
             p = Product(**p)
             db.session.add(p)

        db.session.commit()