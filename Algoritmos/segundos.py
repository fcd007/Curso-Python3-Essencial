segundos = input("Por favor, entre com o número de segundos que deseja converter:")
segundos = int(segundos)
a = segundos // 86400
segundos_parcial = segundos % 86400
b = segundos_parcial // 3600
segundos_parcial = segundos_parcial % 3600
c = segundos_parcial // 60
d = segundos_parcial % 60
print(a, "dias,",b,"horas,",c,"minutos e",d,"segundos.")