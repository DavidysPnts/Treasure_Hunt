import pygame
from pygame.locals import *
from sys import exit
from menu_config import menu_config, dificuldade
from caca_ao_tesouro import main
import os

def ajuste_diretorio():
    DIR_BASE = os.path.dirname(os.path.abspath(__file__))
    os.chdir(DIR_BASE)
    return DIR_BASE

def desenhar_menu(tela):
    mensagem_menu1 = "Jogar"
    mensagem_menu2 = "Configuração"
    mensagem_menu3 = "Sair"

    botao_largura, botao_altura = textura_botão.get_size()

    espacamento = altura // 20
    total_altura = botao_altura * 2 + espacamento
    inicio_y = (altura - total_altura) // 2

    botao_x = (largura - botao_largura) // 2
    botao1_y = inicio_y
    botao2_y = inicio_y + botao_altura + espacamento
    botao3_y = inicio_y + 2 * (botao_altura + espacamento)

    tela.blit(fundo, (0, 0))
    tela.blit(logo, (0, 0))
    tela.blit(textura_botão, (botao_x, botao1_y))
    tela.blit(textura_botão, (botao_x, botao2_y))
    tela.blit(textura_botão, (botao_x, botao3_y))

    texto_formatado_menu1 = fonte_menu.render(mensagem_menu1, True, (0,0,0))
    texto_formatado_menu2 = fonte_menu.render(mensagem_menu2, True, (0, 0, 0))
    texto_formatado_menu3 = fonte_menu.render(mensagem_menu3, True, (0, 0, 0))

    texto1_rect = texto_formatado_menu1.get_rect(center=(botao_x + botao_largura // 2, botao1_y + botao_altura // 2))
    texto2_rect = texto_formatado_menu2.get_rect(center=(botao_x + botao_largura // 2, botao2_y + botao_altura // 2))
    texto3_rect = texto_formatado_menu3.get_rect(center=(botao_x + botao_largura // 2, botao3_y + botao_altura // 2))

    tela.blit(texto_formatado_menu1, texto1_rect)
    tela.blit(texto_formatado_menu2, texto2_rect)
    tela.blit(texto_formatado_menu3, texto3_rect)

    global botão_jogar
    botão_jogar = pygame.Rect(botao_x, botao1_y, botao_largura, botao_altura)
    global botão_configuração
    botão_configuração = pygame.Rect(botao_x, botao2_y, botao_largura, botao_altura)
    global botão_sair
    botão_sair = pygame.Rect(botao_x, botao3_y, botao_largura, botao_altura)

def carregar_recursos():
    global fundo, logo, textura_botão
    fundo = pygame.image.load('assets//imagens//fundo_menu.png')
    logo = pygame.image.load('assets//imagens//logo_jogo.png')
    textura_botão = pygame.image.load('assets//imagens//pergaminho.png')

def config_inicial():
    global largura, altura, fonte_menu, tela
    global jogador1_nome, jogador2_nome
    global seta_rect, botão_facil, botão_medio, botão_dificil, botão_nome_jogador1, botão_nome_jogador2
    global nivel, volume, estado_atual

    largura = 800
    altura = 800

    fundo_scaled = pygame.transform.scale(fundo, (largura, altura))
    logo_scaled = pygame.transform.scale(logo, (100, 100))
    textura_scaled = pygame.transform.scale(textura_botão, (largura//5, altura//10))

    globals()['fundo'] = fundo_scaled
    globals()['logo'] = logo_scaled
    globals()['textura_botão'] = textura_scaled

    fonte_menu = pygame.font.SysFont('gabriola', largura//40, False, False)

    tela = pygame.display.set_mode((largura, altura))
    desenhar_menu(tela)

    nivel = 'facil'
    volume = 1.0

    seta_rect = pygame.Rect(0, 0, 0, 0)
    botão_facil = pygame.Rect(0, 0, 0, 0)
    botão_medio = pygame.Rect(0, 0, 0, 0)
    botão_dificil = pygame.Rect(0, 0, 0, 0)
    botão_nome_jogador1 = pygame.Rect(0, 0, 0, 0)
    botão_nome_jogador2 = pygame.Rect(0, 0, 0, 0)

    jogador1_nome = "Jogador 1"
    jogador2_nome = "Jogador 2"

    estado_atual = 'menu_principal'

def loop_principal():
    global estado_atual, nivel, volume, jogador1_nome, jogador2_nome
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if estado_atual == 'menu_principal':
                    if botão_jogar.collidepoint(pygame.mouse.get_pos()):
                        xlinhas, tam_celula = dificuldade(nivel)
                        main(tam_celula, xlinhas, jogador1_nome, jogador2_nome, volume)

                        desenhar_menu(tela)
                        estado_atual == 'menu_principal'
                    if botão_configuração.collidepoint(pygame.mouse.get_pos()):
                        seta_rect,botão_facil,botão_medio,botão_dificil,botão_nome_jogador1,botão_nome_jogador2,botão_volume_0,botão_volume_50,botão_volume_100 = menu_config(tela, jogador1_nome, jogador2_nome)
                        estado_atual = 'menu_config'
                    if botão_sair.collidepoint(pygame.mouse.get_pos()):
                        pygame.quit()
                        exit()
                if estado_atual == 'menu_config':
                    if seta_rect.collidepoint(pygame.mouse.get_pos()):
                        desenhar_menu(tela)
                        estado_atual = 'menu_principal'
                    if botão_facil.collidepoint(pygame.mouse.get_pos()):
                        nivel = 'facil'
                        print("Dificuldade selecionada: Fácil")
                    if botão_medio.collidepoint(pygame.mouse.get_pos()):
                        nivel = 'medio'
                        print("Dificuldade selecionada: Médio")
                    if botão_dificil.collidepoint(pygame.mouse.get_pos()):
                        nivel = 'dificil'
                        print("Dificuldade selecionada: Difícil")
                    if botão_volume_0.collidepoint(pygame.mouse.get_pos()):
                        volume = 0.0
                        print("Volume definido para 0%")
                    if botão_volume_50.collidepoint(pygame.mouse.get_pos()):
                        volume = 0.5
                        print("Volume definido para 50%")
                    if botão_volume_100.collidepoint(pygame.mouse.get_pos()):
                        volume = 1.0
                        print("Volume definido para 100%")

                    if botão_nome_jogador1.collidepoint(pygame.mouse.get_pos()):
                        novo_nome = ""
                        ativo = True
                        while ativo:
                            for e in pygame.event.get():
                                if e.type == QUIT:
                                    pygame.quit()
                                    exit()
                                if e.type == KEYDOWN:
                                    if e.key == K_RETURN:
                                        if novo_nome.strip() != "":
                                            jogador1_nome = novo_nome
                                        ativo = False
                                    elif e.key == K_BACKSPACE:
                                        novo_nome = novo_nome[:-1]
                                    else:
                                        if len(novo_nome) < 15:
                                            novo_nome += e.unicode
                            tela.fill((255,255,255))
                            menu_config(tela, novo_nome if novo_nome else jogador1_nome, jogador2_nome)
                            fonte_input = pygame.font.SysFont('arial', largura//50, True, False)
                            texto_input = fonte_input.render("" + novo_nome, True, (0,0,0))
                            tela.blit(texto_input, (largura//10, altura//1.2))
                            pygame.display.update()

                    elif botão_nome_jogador2.collidepoint(pygame.mouse.get_pos()):
                        novo_nome = ""
                        ativo = True
                        while ativo:
                            for e in pygame.event.get():
                                if e.type == QUIT:
                                    pygame.quit()
                                    exit()
                                if e.type == KEYDOWN:
                                    if e.key == K_RETURN:
                                        if novo_nome.strip() != "":
                                            jogador2_nome = novo_nome
                                        ativo = False
                                    elif e.key == K_BACKSPACE:
                                        novo_nome = novo_nome[:-1]
                                    else:
                                        if len(novo_nome) < 15:
                                            novo_nome += e.unicode
                            tela.fill((255,255,255))
                            menu_config(tela, jogador1_nome, novo_nome if novo_nome else jogador2_nome)
                            fonte_input = pygame.font.SysFont('arial', largura//50, True, False)
                            texto_input = fonte_input.render("" + novo_nome, True, (0,0,0))
                            tela.blit(texto_input, (largura//10, altura//1.2))
                            pygame.display.update()

            if event.type == QUIT:
                pygame.quit()
                exit()
        pygame.display.update()

if __name__ == '__main__':
    pygame.init()
    DIR_BASE = ajuste_diretorio()
    carregar_recursos()
    config_inicial()
    loop_principal()
