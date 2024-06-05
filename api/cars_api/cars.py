from fastapi import APIRouter
from database.carservice import get_all_cars, register_car

car_router = APIRouter(prefix='/car', tags=['API for cars'])

@car_router.post('/register-car')
async def register(name: str, year: int, quantity: int, e_power: str, type: str):
    reg = register_car(name, year, quantity, e_power, type)
    return reg

@car_router.get('/all_cars')
async def all_cars():
    return get_all_cars()