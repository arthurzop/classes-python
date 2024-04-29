from conta import conta

conta1 = conta('arthur', '12345','corrente', '20/11/2000', 'Santander')

print(f'Nome:      {conta1.nome}')
print(f'Senha:     {conta1.senha}')
print(f'Tipo:      {conta1.tipo}')
print(f'Data de Nascimento:  {conta1.data}')
print(f'Banco:        {conta1.banco} \n')


conta1.sacar()
conta1.depositar()
