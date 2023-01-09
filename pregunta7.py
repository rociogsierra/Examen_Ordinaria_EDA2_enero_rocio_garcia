
def recorrer_lista(lista, elemento):  
    contador = 0 
    for elem in lista:
        if elem == elemento:
         return lista[:contador]
        else:
            contador += 1

    return -1


lista = ["casco", "muñeco", "pista", "mirar", "sable laser", "comer"]
elemento = "sable laser"
elementos_recorridos = recorrer_lista(lista, elemento)

if elementos_recorridos == -1:
    print(f"El elemento {elemento} no se ha encontrado en la lista")
else:
    print(f"Los elementos recorridos hasta encontrar el elemento {elemento} son: {elementos_recorridos}")