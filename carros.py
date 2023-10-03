class Carro:
    def __init__(self, marca, modelo, ano, preco, vendido):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        self.vendido = vendido
    
    def exibir_informações(self):
        return f'marca: {self.marca}, modelo: {self.modelo}, ano: {self.ano}, preco: {self.preco}, vendido: {self.vendido}'
    
veiculo1 = Carro('toyota', 'corolla', 2009, 2500, True)
veiculo2 = Carro('ford', 'fusion', 2022, 2000, False)
veiculo3 = Carro('wolks', 'gol', 2003, 1000, True)

if veiculo1.vendido:
    print("Veículo 1 está vendido")
else:
    print("Veículo 1 não está vendido")
if veiculo2.vendido:
    print("Veículo 2 está vendido")
else:
    print("Veículo 2 não está vendido")
if veiculo3.vendido:
    print("Veículo 3 está vendido")
else:
    print("Veículo 3 não está vendido")



print(veiculo1.exibir_informações())
print(veiculo2.exibir_informações())
print(veiculo3.exibir_informações())


   
        

    #marca = [Toyota, Ford, BMW]
    #modelo = [corolla, camaro, gol]
    #ano = [1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
   
