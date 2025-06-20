
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
      

    def calcularTercoFerias(self):

        resultadoTercoFerias = self.salario/3 # Calcula o terço de férias
        
        return resultadoTercoFerias
    

    def calcularFeriasPorDias(self):
        
        resultadoFeriasPorDias = self.calcularTercoFerias()  + ((self.salario/self.feriasPorDias)*self.feriasPorDias)
        
        return resultadoFeriasPorDias
