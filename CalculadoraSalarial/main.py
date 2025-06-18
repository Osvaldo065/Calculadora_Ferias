from Calculadora import CalculadoraSalarial
from decimal import Decimal

if __name__ == '__main__':
    
    #Mensagem de aprensentação
    print("\nSeja Bem vindo ao Calculate whit Dias!")
    
    print("\n O que você deseja calcular?")
    print("\nSelecione um das opções abaixo:")
    print("[1] - Calcular salário por dia")
    print("[2] - Calcular salário por hora")
    print("[3] - Calcular valor das férias")
    print("[4] - Sair")
    
    opcao = int(input("Digite sua opção: "))
    
    match opcao:
        
        case 1:
            salario = Decimal(input("\nInforme o seu salário:"))
            dias_no_mes = int(input("\nDigite os dias trabalhados no mês: "))
            calculadora = CalculadoraSalarial(salario, 0, dias_no_mes, 0)
            salarioPorDia = calculadora.calcularSalarioDia()
            print(f"Seu salário por dia é: R${salarioPorDia}")
            
        case 2:
            salario = Decimal(input("\nInforme o seu salário:"))
            horasTrabalhadas = int(input("\nDigite suas horas trabalhadas no mês:"))
            calculadora = CalculadoraSalarial(salario, horasTrabalhadas, 0, 0)
            salarioPorHora = calculadora.calcularSalarioHora()
            print(f"Seu salário por hora é: R${salarioPorHora}")
        
        case 3:
            salario = Decimal(input("\nInforme o seu salário:"))
            feriasPorDias = int(input("\nQuantidade de dias de férias: "))
            calculadora = CalculadoraSalarial(salario, 0, 0, feriasPorDias)
            valorFeriasPorDias = calculadora.calcularFeriasPorDias()
            print(f"O valor das suas férias são de: R${valorFeriasPorDias}")
            
        case 4:
            print("Saindo...")
        
        case _:
            print("Opção invalida")
            

    
    

    
    
    

