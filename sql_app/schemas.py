from typing import List, Optional
from datetime import date, datetime
from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import DateTime
# from enum import Enum


class Food_data(BaseModel):
    food_name : str
    food_category : str
    food_price : float
    food_quantity : int


class Food(Food_data):
    food_id : int
   

    class Config:
        orm_mode = True


class Customer(BaseModel):
    id : int
    name : str

    class Config:
        orm_mode = True


class Order(BaseModel):
    id: int
    food_id: int 
    customer_id : int  
    status : Optional[str] = "Order Created"

    class Config:
        orm_mode = True

class Check_reservation(BaseModel):
    slot : int
    r_date : date  # r_date represents Reservation date 

class Do_reservation(Check_reservation):
    customer_id : int
    table_id : int


class Reservation(Check_reservation):
    id: int
    
    class Config:
        orm_mode = True

class Add_table(BaseModel):
    name: str
    seat : int

class Table(Add_table):
    id: int


    class Config:
        orm_mode = True

class Feedback_data(BaseModel):
    customer_id : int
    order_id :int
    rate : int
    comment : str 

class Feedback(Feedback_data):
    id: int

    class Config:
        orm_mode = True


# class Update_status(str, Enum):
#     Order_placed = "Order placed"
#     Order_under_process = "Order under process"
#     Order_served = "Order served"
#     # Order_fail = "Order Fail"


# class Status(BaseModel):
#     id : int
#     name : str

#     class Config:
#         orm_mode = True



# class ItemBase(BaseModel):
#     title: str  
#     description: Optional[str] = None


# class ItemCreate(ItemBase):
#     pass


# class Item(ItemBase):
#     id: int
#     owner_id: int

#     class Config:
#         orm_mode = True


# class UserBase(BaseModel):
#     email: str


# class UserCreate(UserBase):
#     password: str


# class User(UserBase):
#     id: int
#     is_active: bool
#     items: List[Item] = []

#     class Config:
#         orm_mode = True