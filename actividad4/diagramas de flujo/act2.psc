Algoritmo sin_titulo
	definir dia, mes, a�o Como Entero
	definir dia_act, mes_act, a�o_act Como Entero
	dia_act= 22
	mes_act= 4
	a�o_act= 2025
	leer dia
	leer mes
	leer a�o
	definir dias_transc Como Entero
	definir mes_transc Como Entero
	definir a�o_transc Como Entero
	
	a�o_transc= a�o_act -a�o
	
	mes_transc= mes_act-mes
	
	dias_transc= dia_act - dia
	
	si a�o_transc > 0 Entonces
		suma_dias = 365* a�o_transc
	FinSi
	
	si mes_transc > 0 Entonces
		suma_dias = suma_dias + (30+mes_transc)
		
	FinSi
	
	si dias_transc > 0 Entonces
		suma_dias= suma_dias+dias_transc
	FinSi
	
	escribir dias_transc
	escribir mes_transc
	escribir a�o_transc
	escribir suma_dias
	si suma_dias<=30 Entonces
		Escribir 'ok'
	FinSi
	
	
	
	
	
	
FinAlgoritmo
