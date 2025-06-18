
class CalculadoraSalarial:
    
    def __init__(self, salario, dias_no_mes, horasTrabalhadas, feriasPorDias):
        self.salario = salario
        self.dias_no_mes = dias_no_mes
        self.horastrabalhadas = horasTrabalhadas
        self.feriasPorDias = feriasPorDias
        

    def calcularSalarioHora(self):
        
        resultadoSalarioHora = self.salario/self.horastrabalhadas
        
        return resultadoSalarioHora
    
    
    def calcularSalarioDia(self):
        
        resultadoSalarioPorDia = self.salario/self.dias_no_mes
        
        return resultadoSalarioPorDia
      

    def calcularFerias(self):

        resultadoFerias = self.salario+(self.salario/3)
        
        return resultadoFerias
    

    def calcularFeriasPorDias(self):
        
        resultadoFeriasPorDias = self.calcularFerias() / self.feriasPorDias # AJUSTAR O CALCULO POR DIAS 
        
        return resultadoFeriasPorDias
