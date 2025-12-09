import numpy as np

#vê se classificamos o ponto errado ou certo
def Loss(theta, position, label):
    aux = np.dot(theta, position)
    aux = aux * label

    return aux

"""
    Algoritmo do modelo
    -wall -> ponto que separa os grupos
    -size -> quantos exemplos tomar no data_set
        - se size = 0, usa todo o dataset
    -T -> número máximo de iterações
    -data -> dataset de entrada
    -theta -> pesos iniciais
    -lr -> learning rate
    -aux -> vetor de bias
"""
def Perceptron(T, theta, lr, data, size, wall):
    #pegando a matriz de dados pro caso 3D;
    if (size == 100):
        data = data.to_numpy().T
        #adicionando a parte do bias;
        aux = np.full(150,1)
        data = np.vstack((data, aux))

    #Lógica principal do Perceptron;
    for t in range(T):
        flag = 0
        for i in range(size):
            #diferencia as classes;
            if (i >= wall):
                y = -1
            else:
                y = 1    

            if (Loss(theta,data[:,i],y) <= 0):
                theta = theta + y * lr * data[:,i]
                flag = 1

        #saber quando o modelo para de aprender;
        if (flag == 0):
            print (f'fim do treino no ciclo {t}')
            break

    return theta