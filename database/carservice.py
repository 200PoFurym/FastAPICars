from database.models import Cars, CategoryCars
from datetime import datetime
from database import get_db

def get_all_cars():
    db = next(get_db())
    cars = db.query(Cars).all()
    return cars

def register_car(name, year, quantity, e_power, type):
    db = next(get_db())
    checker = db.query(Cars).filter_by(name=name).first()
    if checker:
        checker.quantity += quantity
        return checker.quantity
    else:
        new_car = Cars(name=name, year=year, quantity=quantity, e_power=e_power, type=type, datetime=datetime.now())
        db.add(new_car)
        db.commit()
        return f'{new_car.name} Успешно добавлена!'