import numpy as np #importa a lib numpy

#função responsavel por calcular os valores da matriz
def calculate(lst):
    #garante que há 9 valores na matriz
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")

    #cria a matriz com os inputs da função
    matriz = np.array(lst).reshape(3, 3)

    #calcula cada valor de linha, coluna e total da matriz usando os metodos do numpy
    calculations = {
        'mean': [
            matriz.mean(axis=0).tolist(),
            matriz.mean(axis=1).tolist(),
            matriz.mean().item()
        ],
        'variance': [
            matriz.var(axis=0).tolist(),
            matriz.var(axis=1).tolist(),
            matriz.var().item()
        ],
        'standard deviation': [
            matriz.std(axis=0).tolist(),
            matriz.std(axis=1).tolist(),
            matriz.std().item()
        ],
        'max': [
            matriz.max(axis=0).tolist(),
            matriz.max(axis=1).tolist(),
            matriz.max().item()
        ],
        'min': [
            matriz.min(axis=0).tolist(),
            matriz.min(axis=1).tolist(),
            matriz.min().item()
        ],
        'sum': [
            matriz.sum(axis=0).tolist(),
            matriz.sum(axis=1).tolist(),
            matriz.sum().item()
        ]
    }

    return calculations
