import statistics

empresa1 = [1000,6000,1200,8000,1400]

empresa2 = [5000,4000,3000,2000,7000]

empresa3 = [1200,1300,8000,3000,15000]

empresa4 = [1400,1750,2000,4500,5900]

def analisar_empresa(salarios):
    print('Media', statistics.mean(salarios))
    print('Moda', statistics.mode(salarios))
    print('Mediana', statistics.median(salarios))
    print('Desvio', statistics.stdev(salarios))
    print()

print('empresa 1')
analisar_empresa(empresa1)

print('empresa 2')
analisar_empresa(empresa2)

print('empresa 3')
analisar_empresa(empresa3)

print('empresa 4')
analisar_empresa(empresa4)