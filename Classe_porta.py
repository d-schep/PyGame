from cfg import * 
from sala1 import * 
from Classe_Interact import * 

class PortaInterativa(ObjetoInterativo):
    def __init__(self, x, y, width, height, codigo, assets):
        super().__init__(x, y, width, height, "E", tipo='porta')
        self.codigo = codigo
        self.codigo_digitado = ""
        self.is_unlocked = False
        self.mensagem_erro = ""
        self.tempo_erro = 0
        self.input_ativo = False
        self.texto = "E"
        self.linha_atual = 0
        self.linhas_codigo = codigo.split('\n')
        self.linhas_digitadas = [""] * len(self.linhas_codigo)
        self.last_key_time = 0
        self.key_delay = 200

    def update(self, jogador):
        # Verifica se o jogador está perto
        dist_x = abs(self.rect.centerx - jogador.rect.centerx)
        dist_y = abs(self.rect.centery - jogador.rect.centery)
        
        # Define uma distância máxima para interação
        self.pode_interagir = dist_x < 100 and dist_y < 100

    def desenhar_pista(self, screen):
        if self.pode_interagir or self.input_ativo:
            fonte = pygame.font.Font(None, 36)
            
            # Desenha o fundo da interface de senha
            if self.input_ativo:
                # Fundo semi-transparente mais escuro para melhor visibilidade
                s = pygame.Surface((400, 250))  # Aumentado para acomodar múltiplas linhas
                s.set_alpha(200)
                s.fill((0, 0, 0))
                screen.blit(s, (LARGURA//2 - 200, ALTURA//2 - 125))
                
                # Título
                titulo = fonte.render("Digite a senha:", True, (255, 255, 255))
                screen.blit(titulo, (LARGURA//2 - titulo.get_width()//2, ALTURA//2 - 100))
                
                # Campos de senha - mostrando os caracteres digitados
                y_offset = ALTURA//2 - 50
                for i, linha in enumerate(self.linhas_codigo):
                    # Desenha o campo de entrada
                    pygame.draw.rect(screen, (50, 50, 50), (LARGURA//2 - 100, y_offset, 200, 40))
                    
                    # Desenha o texto digitado ou cursor
                    if i == self.linha_atual:
                        texto = self.linhas_digitadas[i] if self.linhas_digitadas[i] else "_"
                        cor = (0, 255, 0)  # Verde para a linha atual
                    else:
                        texto = self.linhas_digitadas[i] if self.linhas_digitadas[i] else "_"
                        cor = (150, 150, 150)  # Cinza para outras linhas
                    
                    texto_surface = fonte.render(texto, True, cor)
                    screen.blit(texto_surface, (LARGURA//2 - texto_surface.get_width()//2, y_offset + 10))
                    y_offset += 50
                
                # Instruções
                instrucoes = fonte.render("Pressione ENTER para confirmar", True, (200, 200, 200))
                screen.blit(instrucoes, (LARGURA//2 - instrucoes.get_width()//2, y_offset + 10))
                
                # Instrução para sair
                instrucao_sair = fonte.render("Pressione X para sair", True, (200, 200, 200))
                screen.blit(instrucao_sair, (LARGURA//2 - instrucao_sair.get_width()//2, y_offset + 50))
            else:
                # Desenha o texto "E" centralizado acima da porta
                texto = fonte.render(self.texto, True, (255, 255, 255))
                texto_rect = texto.get_rect(centerx=self.rect.centerx, bottom=self.rect.top - 10)
                screen.blit(texto, texto_rect)

            if self.mensagem_erro and time.time() - self.tempo_erro < 2:
                texto_erro = fonte.render(self.mensagem_erro, True, (255, 0, 0))
                screen.blit(texto_erro, (LARGURA//2 - texto_erro.get_width()//2, ALTURA//2 - 150))

    def handle_keypress(self, event):
        if not self.input_ativo or self.is_unlocked:
            return

        current_time = pygame.time.get_ticks()
        if current_time - self.last_key_time < self.key_delay:
            return

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # Adiciona saída com X
                self.input_ativo = False
                self.linhas_digitadas = [""] * len(self.linhas_codigo)
                self.linha_atual = 0
                return
            elif event.key == pygame.K_RETURN:
                # Verifica se todas as linhas foram preenchidas
                if all(linha for linha in self.linhas_digitadas):
                    # Verifica se o código está correto
                    if "\n".join(self.linhas_digitadas) == self.codigo:
                        self.is_unlocked = True
                        self.input_ativo = False
                        self.texto = "E"
                    else:
                        self.mensagem_erro = "Código inválido. Tente novamente."
                        self.tempo_erro = time.time()
                        self.linhas_digitadas = [""] * len(self.linhas_codigo)
                        self.linha_atual = 0
                else:
                    self.mensagem_erro = "Preencha todas as linhas"
                    self.tempo_erro = time.time()
            elif event.key == pygame.K_BACKSPACE:
                if self.linhas_digitadas[self.linha_atual]:
                    self.linhas_digitadas[self.linha_atual] = self.linhas_digitadas[self.linha_atual][:-1]
            elif event.key == pygame.K_TAB:
                # Move para a próxima linha
                self.linha_atual = (self.linha_atual + 1) % len(self.linhas_codigo)
            elif event.unicode.isalpha() and len(self.linhas_digitadas[self.linha_atual]) < 20:
                self.linhas_digitadas[self.linha_atual] += event.unicode.upper()
