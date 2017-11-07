# Calcule e mostre:
# O modelo do carro mais econômico;
# Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.

# Comparativo de Consumo de Combustível

# Veículo 1 Nome: fusca Km por litro: 7
# Veículo 2 Nome: gol Km por litro: 10
# Veículo 3 Nome: uno Km por litro: 12.5
# Veículo 4 Nome: Vectra Km por litro: 9
# Veículo 5 nome: Peugeout Km por litro: 14.5

carros = ['Fusca', 'Gol', 'Uno', 'Vectra', 'Peugeout']
consumos = [7, 10, 12.5, 9, 14.5]
distancia = 1000
gasolina = 2.25

for c in range(0, len(carros)):
    litrosGastos = distancia / consumos[c]
    valorGasto = litrosGastos * gasolina
    print("""RELATORIO FINAL
{} - {}           -    {} -  {:.2f} litros - R$ {:.2f}""".format(c + 1, carros[c], consumos[c], litrosGastos, valorGasto))
