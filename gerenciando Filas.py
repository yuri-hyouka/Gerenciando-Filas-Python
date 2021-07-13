
def main():
    print("Simulação de duas filas de banco")
    
    qtdClientes = input("Qual a quantidade de clientes na fila ? ")
        
    #print(qtdClientes)
    
    n = qtdClientes
    opers = leiaOperacoes()
    
    simule(n, opers)

def leiaOperacoes(): 
    
    listaOperacoes = [] 
    print("")

    print("Digite a sequência de operações a ser feitas: ")
    print("F para adicionar um cliente na fila 1 ")
    print("G para adicionar um cliente na fila 2 ")
    print("A para atender cliente na fila 1 ")
    print("B para atender cliente na fila 2 ")
    print("S para sair da simulação ")
    print("")
    
    while True:
      elemento = input().upper()
      if elemento != 'F' and elemento != 'G' and elemento != 'A' and elemento != 'B' and elemento != 'S':
        print("Operação Informada Inválida !")
        continue
      listaOperacoes.append(elemento)
      if elemento == 'S':
        break  
    
    return listaOperacoes

def simule(n, opers):

    n = int(n)
    
    if n % 2 != 0:      # Verificando se o número é impar
      fila1 = n//2      # usando a função parte inteira para capturar a divsão inteira. 
      fila2 = n//2 + 1  # Atribuindo o valo da divisao inteira + 1 para a fila 2.
    else: # Resultado par
      fila1 = n/2
      fila2 = n/2
      
    
    #Criando a Fila 1
    lst_fila = list(range(1, fila1+1))

    #Criando a Fila 2
    lst_fila2 = list(range(fila1+1, fila1+fila2+1))
    
    print("")
    print("Existem " , fila1 , "clientes na fila 1.")
    print(lst_fila)
    
    print("")
    print("Existem " , fila2 , "clientes na fila 2.")
    print(lst_fila2)
    print("")
    
    # CAPTURANDO O ULTIMO ELEMENTO INSERIDO NA LISTA
    tamanho = len(lst_fila2) 
    ultima_posicao = lst_fila2[tamanho - 1]
    ultimo_valor_inserido = ultima_posicao + 1 
    primeira_volta = 1
    
    # VARIAVEL DE CONTROLE DA PRIMEIRA VOLTA DO CLIENTE ATENDIDO
    posicao_a_remover = 0
    primeira_volta_atendido = 1
    
    #print(opers)
    for operacao in opers:
      if operacao == 'F':
        if primeira_volta == 1:
          lst_fila.append(ultimo_valor_inserido)
          ultimo_valor_inserido = ultimo_valor_inserido
          primeira_volta = 0
        else:          
          lst_fila.append(ultimo_valor_inserido + 1) 
          ultimo_valor_inserido = ultimo_valor_inserido + 1    
        
        print("==> OPERAÇÃO F")
        print("")
        print("Existem ", len(lst_fila), " clientes na fila1")
        print("Fila1 atual: ", lst_fila)
        print("")
        print("Existem ", len(lst_fila2), " clientes na fila2")
        print("Fila2 atual: ", lst_fila2)
        print("")         
        
      if operacao == 'G':
        if primeira_volta == 1:
          lst_fila2.append(ultimo_valor_inserido)
          ultimo_valor_inserido = ultimo_valor_inserido
          primeira_volta = 0
        else:          
          lst_fila2.append(ultimo_valor_inserido + 1)
          ultimo_valor_inserido = ultimo_valor_inserido + 1  
          
        print("==> OPERAÇÃO G")
        print("")
        print("Existem ", len(lst_fila), " clientes na fila1")
        print("Fila1 atual: ", lst_fila)
        print("")
        print("Existem ", len(lst_fila2), " clientes na fila2")
        print("Fila2 atual: ", lst_fila2)
        print("") 
        
      if operacao == 'A':
        if primeira_volta_atendido == 1:
          cliente = lst_fila[posicao_a_remover]
          del lst_fila[posicao_a_remover]
          posicao_a_remover = posicao_a_remover
          primeira_volta_atendido = 0
        else:
          cliente = lst_fila[posicao_a_remover]         
          del lst_fila[posicao_a_remover] 
          posicao_a_remover = posicao_a_remover
          
        print("==> OPERAÇÃO A")
        print(" Cliente ",cliente," atendido.")  
        print("")
        print("Existem ", len(lst_fila), " clientes na fila1")
        print("Fila1 atual: ", lst_fila)
        print("")
        print("Existem ", len(lst_fila2), " clientes na fila2")
        print("Fila2 atual: ", lst_fila2)
        print("")  
        
      if operacao == 'B':
        if primeira_volta_atendido == 1:
          cliente = lst_fila2[posicao_a_remover] 
          del lst_fila2[posicao_a_remover]
          posicao_a_remover = posicao_a_remover
          primeira_volta_atendido = 0
        else:
          cliente = lst_fila2[posicao_a_remover]         
          del lst_fila2[posicao_a_remover] 
          posicao_a_remover = posicao_a_remover

        print("==> OPERAÇÃO B")
        print(" Cliente ",cliente," atendido.")  
        print("")
        print("Existem ", len(lst_fila), " clientes na fila1")
        print("Fila1 atual: ", lst_fila)
        print("")
        print("Existem ", len(lst_fila2), " clientes na fila2")
        print("Fila2 atual: ", lst_fila2)
        print("") 
        
      if operacao == 'S':
        break
    
main()