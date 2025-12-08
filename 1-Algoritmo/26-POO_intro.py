####

class Veiculo:
    def movimentar(self):
        print("E Deslocamento")

    def __init__(self, modelo, fabricante):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_registro = None

    def set_num_reg(self, registro):
        self.__num_registro = registro

    def get_fab_mod(self):
        print(f'Modelo: {self.__modelo}, Fabricante: {self.__fabricante}.')

    def get_num_reg(self):
        return self.__num_registro

class Carro(Veiculo):
    # Método __init__ será herdado
    def movimentar(self):
        print(f'Carro andando')


class Moto(Veiculo):
    def movimentar(self):
        print(f'Moto andando em duas rodas')


class Aviao(Veiculo):
    def movimentar(self):
        print('Avião Voando')
    def __init__(self, fabricante, modelo, categoria):
        self.__cat = categoria
        # super ==> super classe pegando o init de veiculo pra evitar repetição de codigo
        super().__init__(fabricante, modelo)

    def get_categoria(self):
            return self.__cat



if __name__=='__main__':
    meu_veiculo = Veiculo('GM', 'Cadillac Escalade')
    meu_veiculo.set_num_reg('1233400-4444')
    meu_veiculo.get_fab_mod()
    print(f'Registro: {meu_veiculo.get_num_reg()}')
    meu_veiculo.movimentar()

    meu_carro = Carro('Volkswagen', 'Polo')
    meu_carro.get_fab_mod()
    meu_carro.movimentar()

    minha_mota = Moto('Meu toba', 'Seu toba')
    minha_mota.get_fab_mod()
    minha_mota.movimentar()

    meu_aviao = Aviao('Boeing', '747', 'Comercial')
    print(f'Categoria: {meu_aviao.get_categoria()}')
    meu_aviao.get_fab_mod()
    meu_aviao.movimentar()