

# Exercise 1: Reescribe el programa del cálculo del salario para darle al empleado
#1.5 veces la tarifa horaria para todas las horas trabajadas que excedan de 40.

horas = int(input('¿Introduce las horas trabajas?'))
tarifa = int(input('¿Introduce la tarifa por hora?'))

sueldo = horas*tarifa


if horas > 40:
    sueldo = (horas*1.5)*tarifa
    print('Sueldo por horas trabajadas',sueldo)
else :
    print(sueldo)