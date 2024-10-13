from pydantic import BaseModel
from typing import List

class Fruit(BaseModel):
    name: str = "apple"
    sugar: float = 12

    class Config:
        shemas_extra = {
            "example": {
                "name": "Manzana",
                "sugar": 23.4,
            }
        }

class UpdateFruit(BaseModel):
    id: int 
    name: str 
    sugar: float 

    class Config:
        shemas_extra = {
            "example": {
                "id" : 1,
                "name": "Manzana",
                "sugar": 23.4,
            }
        }

class ListFruits(BaseModel):
    fruits: List[Fruit]

    class Config:
        shemas_extra = {
            "example": {
                "fruits":[
                    {
                        "id": 1,
                        "name": "Manzana",
                        "sugar": 23.4,
                    },
                    {
                        "id": 1,
                        "name": "Pera",
                        "sugar": 23.4,
                    }
                ]

            }
        }
