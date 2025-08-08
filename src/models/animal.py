class Animal:
    def __init__(self, id:int, name:str, type:str , age:int ):
        self.id = id
        self.name = name
        self.type = type
        self.age = age

    def serializer(self):
        return{
        "id": self.id,
        "name": self.name,
        "type": self.type,
        "age": self.age
        }

