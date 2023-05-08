from positional_list import PositionalList
users_list = PositionalList()

def __init__(self,name,surname,dayOfBirthday,id,gender,fiscalCode):
    self.name = name
    self.surname = surname
    self.dayOfBirthday = dayOfBirthday
    self.id = id
    self.gender = gender
    self.fiscalCode = fiscalCode

def create_user(name, surname, dayOfBirthday, id, gender, fiscalCode):
    user = (name, surname, dayOfBirthday, id, gender, fiscalCode)
    users_list.add_last(user)
    return user









