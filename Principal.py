__author__ = 'Alejandra Campos Contreras'

from MemoriaDinamica import *

Butic = ['labial','perfume', 'jeans', 'rubor', 'blusas', 'sombras']
precios = [150, 400, 600, 159, 58, 300, 230]
matricula = [10,50,66,15,678,999,33,700,50]


listas = MemoriaDinamica(Butic)
listas.imprimirLista()
listas.ordenarLista()
listas.imprimirLista()
listas.agregarelementoarray('tennis')
listas.imprimirLista()
listas.agregarelementoarray('brochas')
listas.imprimirLista()
listas.agregarelementoarray('zapatillas')
listas.imprimirLista()
listas.eliminarElemento('sombras')
listas.imprimirLista()
listas.agregarelementoarray('aretes')
listas.imprimirLista()

lista1 = MemoriaDinamica(precios)
lista1.imprimirLista()
lista1.agregarelementoarray(89)
lista1.imprimirLista()

listas2 = MemoriaDinamica(matricula)
listas2.imprimirLista()
listas2.agregarelementoarray(234)
listas2.imprimirLista()
listas2.ordenarLista()
listas2.imprimirLista()
listas2.eliminarElemento
listas2.imprimirLista()
