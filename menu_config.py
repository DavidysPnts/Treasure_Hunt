import pygame
from pygame.locals import *
from sys import exit

def carregar_imagens(largura, altura):
    imagens = {}
    imagens['seta'] = pygame.image.load('assets/imagens/seta.png')
    imagens['seta'] = pygame.transform.scale(imagens['seta'], (int(largura*0.15), int(altura*0.15)))
    
    imagens['logo'] = pygame.image.load('assets/imagens/logo_jogo.png')
    imagens['logo'] = pygame.transform.scale(imagens['logo'], (largura//10, altura//10 + 10))
    
    imagens['fundo_config'] = pygame.image.load('assets/imagens/fundo_config1.png')
    imagens['fundo_config'] = pygame.transform.scale(imagens['fundo_config'], (largura, altura))
    
    imagens['pergaminho'] = pygame.image.load('assets/imagens/pergaminho.png')
    return imagens

def criar_texto(fonte, texto, cor=(0,0,0)):
    return fonte.render(texto, True, cor)

def menu_dificuldade(tela, pergaminho, fonte, espacamentox, altura):
    config_texto = criar_texto(fonte, "Dificuldade:")
    facil_texto = criar_texto(fonte, "Fácil")
    medio_texto = criar_texto(fonte, "Médio")
    dificil_texto = criar_texto(fonte, "Difícil")

    ax, ay = config_texto.get_size()
    but_dif_y = facil_texto.get_size()[1]
    but_dif1_x = facil_texto.get_size()[0]
    but_dif2_x = medio_texto.get_size()[0]
    but_dif3_x = dificil_texto.get_size()[0]

    botão_facil = pygame.Rect(ax + espacamentox, altura*0.2, but_dif1_x, but_dif_y)
    botão_medio = pygame.Rect(ax + espacamentox*2, altura*0.2, but_dif2_x, but_dif_y)
    botão_dificil = pygame.Rect(ax + espacamentox*3, altura*0.2, but_dif3_x, but_dif_y)

    textura_botao = pygame.transform.scale(pergaminho, (ax+70, ay+45))
    tela.blit(textura_botao, (0.03* tela.get_width(), altura*0.17))

    pygame.draw.rect(tela, (0,200,0), botão_facil, 20)
    pygame.draw.rect(tela, (200,200,0), botão_medio, 20)
    pygame.draw.rect(tela, (200,0,0), botão_dificil, 20)

    tela.blit(config_texto, (0.07* tela.get_width(), altura*0.2))
    tela.blit(facil_texto, (ax + espacamentox, altura*0.2))
    tela.blit(medio_texto, (ax + espacamentox*2, altura*0.2))
    tela.blit(dificil_texto, (ax + espacamentox*3, altura*0.2))

    return botão_facil, botão_medio, botão_dificil

def menu_volume(tela, pergaminho, fonte, espacamentox, espacamentoy, altura):
    config_texto = criar_texto(fonte, "Volume:")
    v0 = criar_texto(fonte, "0%")
    v50 = criar_texto(fonte, "50%")
    v100 = criar_texto(fonte, "100%")

    bx, by = config_texto.get_size()
    textura_botao = pygame.transform.scale(pergaminho, (bx+70, by+45))
    tela.blit(textura_botao, (0.05* tela.get_width(), altura*0.17 + espacamentoy))

    botão_volume_0 = pygame.Rect(bx + 20 + espacamentox, altura*0.2+espacamentoy, v0.get_size()[0], by)
    botão_volume_50 = pygame.Rect(bx + espacamentox*2, altura*0.2+espacamentoy, v50.get_size()[0], by)
    botão_volume_100 = pygame.Rect(bx + espacamentox*3, altura*0.2+espacamentoy, v100.get_size()[0], by)

    pygame.draw.rect(tela,(255,255,255),botão_volume_0,20)
    pygame.draw.rect(tela,(255,255,255),botão_volume_50,20)
    pygame.draw.rect(tela,(255,255,255),botão_volume_100,20)

    tela.blit(config_texto, (0.07* tela.get_width(), altura*0.2+espacamentoy))
    tela.blit(v0, (bx+20 + espacamentox, altura*0.2+espacamentoy))
    tela.blit(v50, (bx + espacamentox*2, altura*0.2+espacamentoy))
    tela.blit(v100, (bx + espacamentox*3, altura*0.2+espacamentoy))

    return botão_volume_0, botão_volume_50, botão_volume_100

def menu_nomes(tela, pergaminho, fonte, jogador1_nome, jogador2_nome, espacamentox, espacamentoy, altura):
    config_texto = criar_texto(fonte, "Trocar nome:")
    cx, cy = config_texto.get_size()
    textura_botao = pygame.transform.scale(pergaminho, (cx+70, cy+45))
    tela.blit(textura_botao, (0.06*tela.get_width(), altura*0.17 + espacamentoy*2))
    tela.blit(config_texto, (0.07* tela.get_width(), altura*0.2+espacamentoy*2))

    nome1_texto = criar_texto(fonte, jogador1_nome)
    nome2_texto = criar_texto(fonte, jogador2_nome)

    largura = tela.get_width()
    pygame.draw.rect(tela, (220,220,220), (cx + espacamentox, altura*0.2+espacamentoy*2, largura//5, cy), 20)
    pygame.draw.rect(tela, (220,220,220), (cx + espacamentox*3, altura*0.2+espacamentoy*2, largura//5, cy), 20)

    tela.blit(nome1_texto, (cx + espacamentox, altura*0.2+espacamentoy*2))
    tela.blit(nome2_texto, (cx + espacamentox*3, altura*0.2+espacamentoy*2))

    botão_nome_jogador1 = pygame.Rect(cx + espacamentox, altura*0.2+espacamentoy*2, largura//5, cy)
    botão_nome_jogador2 = pygame.Rect(cx + espacamentox*3, altura*0.2+espacamentoy*2, largura//5, cy)

    return botão_nome_jogador1, botão_nome_jogador2

def menu_config(tela, jogador1_nome="Jogador 1", jogador2_nome="Jogador 2"):
    largura, altura = tela.get_size()
    imagens = carregar_imagens(largura, altura)

    y_logo= altura - 0.13 * altura
    x_logo= largura - 0.1 * largura
    espacamentoy= altura * 0.15
    espacamentox= altura * 0.15  

    tela.blit(imagens['fundo_config'], (0,0))
    tela.blit(imagens['logo'], (x_logo, y_logo))
    seta_rect = imagens['seta'].get_rect(topleft=(largura*0.02,altura*0.02))
    tela.blit(imagens['seta'], (largura*0.02,altura*0.02))

    fonte_config = pygame.font.SysFont('gabriola',largura//30,False,False)

    bot_dif = menu_dificuldade(tela, imagens['pergaminho'], fonte_config, espacamentox, altura)
    bot_vol = menu_volume(tela, imagens['pergaminho'], fonte_config, espacamentox, espacamentoy, altura)
    bot_nome = menu_nomes(tela, imagens['pergaminho'], fonte_config, jogador1_nome, jogador2_nome, espacamentox, espacamentoy, altura)

    return seta_rect, *bot_dif, *bot_nome, *bot_vol

def dificuldade(nivel):
    if nivel == 'facil':  
        return 4, 170
    elif nivel == 'medio':
        return 6, 113.33333333333
    elif nivel == 'dificil':
        return 8, 85
    return 0, 0
