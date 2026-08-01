import statistics

def media(nota):
    return statistics.mean(notas)

def moda(notas):
    return statistics.mode(notas)

def desvio(notas):
    return statistics.stdev(notas)

def menor(notas):
    return min(notas)

def maior(notas):
    return max(notas)

notas = [6, 7, 8, 4, 3, 2]

print('media', media(notas))
print('moda', moda(notas))
print('desvio padrao', desvio(notas))
print('menor nota', menor(notas))
print('maior nota', maior(notas))