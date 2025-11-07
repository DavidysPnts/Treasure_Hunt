import pygame
import random
import cores
from sys import exit

def init():
    pygame.init()
    fonte = pygame.font.SysFont('8-bit-hud.ttf', 30)
    return fonte

def musica(volume):
    pygame.mixer.music.load('assets/sons/musica_de_fundo.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(volume)

def sons(volume):
    som_tesouro = pygame.mixer.Sound('assets/sons/smw_coin.wav')
    som_tesouro.set_volume(volume)

    som_buraco = pygame.mixer.Sound('assets/sons/smw_firework.wav')
    som_buraco.set_volume(volume)

    som_cavando = pygame.mixer.Sound('assets/sons/cavando.wav')
    som_cavando.set_volume(volume)
    
    return som_tesouro, som_buraco, som_cavando

def tela_criar(XLINHAS, TAM_CELULA ,MARGEM):
    largura = XLINHAS * TAM_CELULA + 2 * MARGEM
    altura = (XLINHAS + 1) * TAM_CELULA + 2 * MARGEM
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Treasure Hunt')
    return tela

def load_imagens(TAM_CELULA):
    imagens = {}

    grama = pygame.image.load('assets/imagens/grama.png')
    imagens["grama"] = pygame.transform.scale(grama, (TAM_CELULA - 2, TAM_CELULA - 2))

    tesouro = pygame.image.load('assets/imagens/tesouro1.png')
    imagens["tesouro"] = pygame.transform.scale(tesouro, (TAM_CELULA - 2, TAM_CELULA - 2))

    buraco = pygame.image.load('assets/imagens/buraco1.png')
    imagens["buraco"] = pygame.transform.scale(buraco, (TAM_CELULA - 2, TAM_CELULA - 2))

    barro = pygame.image.load('assets/imagens/barro.png')
    imagens["barro"] = pygame.transform.scale(barro, (TAM_CELULA -2 , TAM_CELULA -2))
    return imagens


def desenho_tabuleiro(tela, XLINHAS, TAM_CELULA, imagens, MARGEM):
    tela.fill(cores.verde_grama_escuro)

    for i in range(XLINHAS):
        for j in range(XLINHAS):
            x = MARGEM + TAM_CELULA * i
            y = MARGEM + TAM_CELULA * j
            pygame.draw.rect(tela, cores.preto, (x, y, TAM_CELULA, TAM_CELULA), 1)
            tela.blit(imagens["grama"], (x+1 , y+1))

def conteudo_tab(XLINHAS):
    conteudo_celula = [[None for _ in range(XLINHAS)] for _ in range(XLINHAS)]

    num_tesouros = 0
    while num_tesouros < int(0.20 * (XLINHAS ** 2) + 1):
        i = random.randint(0, XLINHAS - 1)
        j = random.randint(0, XLINHAS - 1)
        if conteudo_celula[i][j] is None:
            conteudo_celula[i][j] = 'X'
            num_tesouros += 1

    num_buracos = 0
    while num_buracos < int(0.10 * (XLINHAS ** 2) + 1):
        i = random.randint(0, XLINHAS - 1)
        j = random.randint(0, XLINHAS - 1)
        if conteudo_celula[i][j] is None:
            conteudo_celula[i][j] = 'Y'
            num_buracos += 1
            
    for i in range(XLINHAS):
        for j in range(XLINHAS):
            if conteudo_celula[i][j] is None:
                tvizinhos = 0
                if i > 0 and conteudo_celula[i - 1][j] == 'X':
                    tvizinhos += 1
                if i < XLINHAS - 1 and conteudo_celula[i + 1][j] == 'X':
                    tvizinhos += 1
                if j > 0 and conteudo_celula[i][j - 1] == 'X':
                    tvizinhos += 1
                if j < XLINHAS - 1 and conteudo_celula[i][j + 1] == 'X':
                    tvizinhos += 1
                conteudo_celula[i][j] = str(tvizinhos)

    return conteudo_celula, num_tesouros

def placar(tela, fonte, jogador1, jogador2, turno, XLINHAS, TAM_CELULA, MARGEM, nome_jogador1, nome_jogador2):
    pygame.draw.rect(tela, cores.verde_grama_escuro, (0, MARGEM + TAM_CELULA * XLINHAS, XLINHAS * TAM_CELULA + 2 * MARGEM, TAM_CELULA))
    placar = fonte.render(f'{nome_jogador1}: {jogador1} | {nome_jogador2}: {jogador2} | Vez de {nome_jogador1 if turno == 1 else nome_jogador2}', True, cores.preto)
    tela.blit(placar, (MARGEM + TAM_CELULA / 2, MARGEM + (TAM_CELULA * XLINHAS) + 30))

def revelar_celula(tela, fonte, conteudo_celula, i, j, TAM_CELULA, imagens, MARGEM):
    x = MARGEM + TAM_CELULA * i + 1
    y = MARGEM + TAM_CELULA * j + 1
    tela.blit(imagens['barro'], (x+1, y+1))
    
    if conteudo_celula[i][j] == 'X':
        tela.blit(imagens["tesouro"], (x + 1, y + 1))
    elif conteudo_celula[i][j] == 'Y':
        tela.blit(imagens["buraco"], (x + 1, y + 1))
    else:
        texto = fonte.render(conteudo_celula[i][j], True, cores.preto)
        tela.blit(texto, (x + 0.4 * TAM_CELULA, y + 0.4 * TAM_CELULA))

def tela_final(tela, fonte, jogador1, jogador2, XLINHAS, TAM_CELULA, MARGEM, nome_jogador1, nome_jogador2):
    pygame.draw.rect(tela, cores.verde_grama_escuro, (0, MARGEM + TAM_CELULA * XLINHAS, XLINHAS * TAM_CELULA + 2 * MARGEM, TAM_CELULA))
    
    if jogador1 > jogador2:
        texto = (f'{nome_jogador1}: {jogador1} | {nome_jogador2}: {jogador2} | O {nome_jogador1} Ganhou!')
    elif jogador2 > jogador1:
        texto = (f'{nome_jogador1}: {jogador1} | {nome_jogador2}: {jogador2} | O {nome_jogador2} Ganhou!')
    else:
        texto = (f'{nome_jogador1}: {jogador1} | {nome_jogador2}: {jogador2} | Empate!')

    texto_reinicio = fonte.render('Pressione R para reiniciar', True, cores.preto)
    texto_menu = fonte.render('Pressione ESC para voltar ao menu', True, cores.preto)
    texto = fonte.render(texto, True, cores.preto)
    tela.blit(texto, (MARGEM + (TAM_CELULA / 2) - 15, MARGEM + (TAM_CELULA * XLINHAS) + 20))
    tela.blit(texto_reinicio, (MARGEM + (TAM_CELULA / 2) - 15, MARGEM + (TAM_CELULA * XLINHAS) + 50))
    tela.blit(texto_menu, (MARGEM + (TAM_CELULA / 2) - 15, MARGEM + (TAM_CELULA * XLINHAS) + 75))

def main(tam_celula, xlinhas, jogador1_nome, jogador2_nome, volume):
    fonte = init()
    musica(volume)
    som_tesouro, som_buraco, som_cavando = sons(volume)
    
    TAM_CELULA = tam_celula
    XLINHAS = xlinhas
    MARGEM = 10
    
    tela = tela_criar(XLINHAS, TAM_CELULA, MARGEM)
    imagens = load_imagens(TAM_CELULA)
    desenho_tabuleiro(tela, XLINHAS, TAM_CELULA, imagens, MARGEM)
    conteudo_celula, num_tesouros = conteudo_tab(XLINHAS)
    
    celula_revelada = [[False for i in range(XLINHAS)] for j in range(XLINHAS)]
    jogo_acabou = False
    jogador1 = 0
    jogador2 = 0
    turno = 1
    tesouros_abertos = 0

    while True:
        if jogo_acabou:
            tela_final(tela, fonte, jogador1, jogador2, XLINHAS, TAM_CELULA, MARGEM, jogador1_nome, jogador2_nome)
        else:    
            placar(tela, fonte, jogador1, jogador2, turno, XLINHAS, TAM_CELULA, MARGEM, jogador1_nome, jogador2_nome)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                pygame.mixer.music.stop()
                return

            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_r:
                jogador1 = jogador2 = tesouros_abertos = 0
                turno = 1
                jogo_acabou = False

                desenho_tabuleiro(tela, XLINHAS, TAM_CELULA, imagens, MARGEM)
                conteudo_celula, num_tesouros = conteudo_tab(XLINHAS)
                celula_revelada = [[False for _ in range (XLINHAS)] for _ in range (XLINHAS)]
                continue

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if jogo_acabou:
                    continue

                mouse_x, mouse_y = evento.pos
                celula_x = int((mouse_x - MARGEM) // TAM_CELULA)
                celula_y = int((mouse_y - MARGEM) // TAM_CELULA)
                
                if celula_x < 0 or celula_x >= XLINHAS or celula_y < 0 or celula_y >= XLINHAS:
                    continue
                
                if not celula_revelada[celula_x][celula_y]:
                    celula_revelada[celula_x][celula_y] = True
                    som_cavando.play()
                    
                    if conteudo_celula[celula_x][celula_y] == 'X':
                        som_tesouro.play()
                        tesouros_abertos += 1
                        if turno == 1:
                            jogador1 += 100
                        else:
                            jogador2 += 100
                    elif conteudo_celula[celula_x][celula_y] == 'Y':
                        som_buraco.play()
                        if turno == 1 and jogador1 > 0:
                            jogador1 -= 50
                        elif turno == 2 and jogador2 > 0:
                            jogador2 -= 50
                    
                    if turno == 1:
                        turno = 2
                    else:
                        turno = 1
                    
                    revelar_celula(tela, fonte, conteudo_celula, celula_x, celula_y, TAM_CELULA, imagens, MARGEM)
                    
                    if tesouros_abertos == num_tesouros:
                        jogo_acabou = True
                        tela_final(tela, fonte, jogador1, jogador2, XLINHAS, TAM_CELULA, MARGEM, jogador1_nome, jogador2_nome)
                    
        pygame.display.update()