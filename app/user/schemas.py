from pydantic import BaseModel

class UseBase(BaseModel):
    name: str
    number_phone: str
    emai: str

class User_Login(UseBase):
    password: str
    class Config():
        orm_mode=True