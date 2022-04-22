#Calificaciones con def

def calif_if(a):
    if a <= 1 and a >0.9:
        return ('Sobresaliente')
    elif a <= 1 and a >0.8:
        print('Notable')
    elif a <= 1 and a >0.7:
        print('Bien')
    elif a <= 1 and a >0.6:
        print('Suficiente')
    elif a <= 1 and a >0.0:
        print('Insuficiente')
    else :
        print('Numero incorrecto')

calif_if(0.88)
calif_if(10)
calif_if(0.65)
calif_if(0.72)
print('La nota que obtuvo fue',calif_if(0.94))
