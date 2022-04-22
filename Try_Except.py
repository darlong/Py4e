

# Exercise 1: Reescribe el programa del cálculo del salario para darle al empleado
#1.5 veces la tarifa horaria para todas las horas trabajadas que excedan de 40.
try:
    horas = int(input('¿Introduce las horas trabajas?'))
except: 
    print('Error, por favor introducir un numero')
    
try:
    tarifa = int(input('¿Introduce la tarifa por hora?'))
except:
    print('Error, por favor introducir un numero')


if horas > 40:
    sueldoplus = horas* (tarifa*1.5)
    print('Sueldo por horas trabajadas',sueldoplus)
else :
    sueldo = horas*tarifa
    print('Sueldo por horas trabajadas',sueldo)