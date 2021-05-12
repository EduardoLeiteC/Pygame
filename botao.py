import pygame

class Button():
    
    def __init__(self, configuracoesDoJogo, screen, mensagem):
        # Inicializa os atributos do botão
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Define as dimensões e propriedades
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont("arial", 38)
        
        # Constrói o objeto rect do botão e o centraliza
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # Prepara a mensagem do botão
        self.prep_msg(mensagem)
        
    def prep_msg(self, mensagem):
        # Transforma a mensagem em imagem no centro do botão
        self.msg_image = self.font.render(mensagem, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    
    def draw_button(self):
        # Desenha um botão branco com a mensagem
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        