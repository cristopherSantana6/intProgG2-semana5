Algoritmo sin_titulo
	definir dia, mes, año Como Entero
	definir dia_act, mes_act, año_act Como Entero
	dia_act= 22
	mes_act= 4
	año_act= 2025
	leer dia
	leer mes
	leer año
	definir dias_transc Como Entero
	definir mes_transc Como Entero
	definir año_transc Como Entero
	
	año_transc= año_act -año
	
	mes_transc= mes_act-mes
	
	dias_transc= dia_act - dia
	
	si año_transc > 0 Entonces
		suma_dias = 365* año_transc
	FinSi
	
	si mes_transc > 0 Entonces
		suma_dias = suma_dias + (30+mes_transc)
		
	FinSi
	
	si dias_transc > 0 Entonces
		suma_dias= suma_dias+dias_transc
	FinSi
	
	escribir dias_transc
	escribir mes_transc
	escribir año_transc
	escribir suma_dias
	si suma_dias<=30 Entonces
		Escribir 'ok'
	FinSi
	
	
	
	
	
	
FinAlgoritmo
