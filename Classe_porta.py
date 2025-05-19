from cfg import * 
from sala1 import * 
from Classe_Interact import * 

class PortaInterativa(ObjetoInterativo):
    def __init__(self, x, y, width, height, codigo, assets):
        super().__init__(x, y, width, height, "Pressione E para inserir o código", tipo='porta')
        self.codigo = codigo
        self.codigo_digitado = ""
        self.is_unlocked = False
        self.mensagem_erro = ""
        self.tempo_erro = 0
        self.input_ativo = False
        self.texto = "Pressione E para inserir o código"
