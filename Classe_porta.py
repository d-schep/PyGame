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
    def desenhar_pista(self, screen):
        if self.pode_interagir or self.input_ativo:
            fonte = pygame.font.Font(None, 36)
            
            # Desenha o fundo da interface de senha
            if self.input_ativo:
                # Fundo semi-transparente mais escuro para melhor visibilidade
                s = pygame.Surface((400, 150))
                s.set_alpha(200)  # Aumentei a opacidade
                s.fill((0, 0, 0))
                screen.blit(s, (LARGURA//2 - 200, ALTURA//2 - 75))
                
                # Título
                titulo = fonte.render("Digite a senha:", True, (255, 255, 255))
                screen.blit(titulo, (LARGURA//2 - titulo.get_width()//2, ALTURA//2 - 50))
                
                # Campo de senha - mostrando os caracteres digitados
                pygame.draw.rect(screen, (50, 50, 50), (LARGURA//2 - 100, ALTURA//2, 200, 40))  # Campo maior
                if self.codigo_digitado:
                    senha_surface = fonte.render(self.codigo_digitado, True, (0, 255, 0))  # Texto em verde
                else:
                    senha_surface = fonte.render("_", True, (0, 255, 0))  # Cursor quando vazio
                screen.blit(senha_surface, (LARGURA//2 - senha_surface.get_width()//2, ALTURA//2 + 10))
                
                # Instruções
                instrucoes = fonte.render("Pressione ENTER para confirmar", True, (200, 200, 200))
                screen.blit(instrucoes, (LARGURA//2 - instrucoes.get_width()//2, ALTURA//2 + 50))
            else:
                texto = fonte.render(self.texto, True, (255, 255, 255))
                screen.blit(texto, (LARGURA//2 - texto.get_width()//2, ALTURA - 50))

            if self.mensagem_erro and time.time() - self.tempo_erro < 2:
                texto_erro = fonte.render(self.mensagem_erro, True, (255, 0, 0))
                screen.blit(texto_erro, (LARGURA//2 - texto_erro.get_width()//2, ALTURA//2 - 100))
