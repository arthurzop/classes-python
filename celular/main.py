from celular import celular

cel1 = celular('Samsumg', 'Galaxy S20', 2500, 'Android', '11in')

print(f'Marca: {cel1.marca}')
print(f'Modelo: {cel1.modelo}')
print(f'Preço: {cel1.preco}')
print(f'Sistema Operacional: {cel1.so}')
print(f'Tamanho de tela: {cel1.tela} \n')

cel1.ligar()
cel1.desligar()
cel1.telefonar()
cel1.jogar()