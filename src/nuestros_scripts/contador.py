file = open('train.csv', 'r')

cantidades = [0,0,0,0,0,0,0,0,0,0]

c = 0
for line in file:
    if c == 0:
        c = 1 # el primero es un label.
        continue
    partes = line.split(",")
    cantidades[int(partes[0])] = cantidades[int(partes[0])] +1

file.close()

print cantidades

sum = 0
for i in cantidades:
    sum = i + sum

porcentajes = [0,0,0,0,0,0,0,0,0,0]
for i in range(0, 10):
    porcentajes[i] = 100*(float(cantidades[i])/sum)


print porcentajes
