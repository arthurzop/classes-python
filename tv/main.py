from tv import tv

tv1 = tv('Samsung', 'HD D-LED', 1196, '32in', 'Preta', True)

print(f'Marca:      {tv1.marca}')
print(f'Modelo:     {tv1.modelo}')
print(f'Preço:      {tv1.preco}')
print(f'Polegadas:  {tv1.tela}')
print(f'Cor:        {tv1.cor}')
print(f'Smart:      {tv1.smart} \n')

tv1.ligar()
tv1.desligar()
tv1.mudar()