from models.cliente import Cliente
from models.conta import Conta

mayco: Cliente = Cliente(
    'Mayco Maximino', 'Maycoa9@gmail.com', '712.047.794-30', '13/11/2001')

print(mayco)

contaM: Conta = Conta(mayco)

# print(contaM)
