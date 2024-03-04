from pydantic import BaseModel
#pip install fastapi
class User(BaseModel):
    name: str
    email: str
    age: int
#O Pydantic irá automaticamente aplicar as regras de validação e garantir que os dados estejam corretos.
input("Aperte enter para ver o tipo de User")
print(type(User))
user_data = {
    "name": "John Doe",
    "email": "johndoe@example.com",
    "age": 25
}
input("Aperte enter para ver o tipo de user-data")
print(type(user_data))
user_data = {
    "name": "John Doe",
    "email": "johndoe@example.com",
    "age": 25
}
user = User(**user_data)
input("Aperte enter para ver o tipo de User")
print(type(user))

input("Aperte enter para ver os dados de User")
print(user.model_dump())
#user.dict()
#dict(user)
#

#-----------------------------------------------------
input("Aperte enter para iniciar a segunda parte")
class Funcionario(BaseModel):
    nome:str
    funcao:str
    registro: int
    setor:str

funcionario_data={
    'nome':'Carolina',
    'funcao':'Gerente',
    'registro':2754,
    'setor':'Telemarketing'
}

funcionaria=Funcionario(**funcionario_data)
input("Aperte Enter para imprimir os dados da funcionaria")
print(dict(funcionaria))