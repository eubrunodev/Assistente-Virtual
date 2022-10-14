import time
import pyautogui
import pyperclip
from pynput.mouse import Button, Controller

mouse = Controller()

def espera(tempo):
    time.sleep(tempo)

def criar_email():
    navegadorX = 217
    navegadorY = 747
    pyautogui.click(navegadorX, navegadorY)
    espera(2)

    newPageX = 250
    newPageY = 10
    pyautogui.click(newPageX, newPageY)

    espera(2)
    pyautogui.click(782, 280)  # clica no google

    espera(3)
    pesquisaX = 470
    pesquisaY = 290
    pyautogui.click(pesquisaX, pesquisaY)

    espera(2)
    pyautogui.write('temp mail')
    pyautogui.press('enter')

    espera(4)
    tempMailX = 162
    tempMailY = 309
    pyautogui.click(tempMailX, tempMailY)

    espera(15)
    copiarEmailX = 897
    copiarEmaiY = 270
    pyautogui.click(copiarEmailX, copiarEmaiY)

    espera(5)
    cadastrar_email()

def cadastrar_email(): # cadastra o email na Stell Series
    steelX = 320
    steelY = 743
    pyautogui.click(steelX, steelY)

    # parte de inserir o email no app da SteelSeries
    espera(4)
    criarContaX = 1064
    criarContaY = 502
    pyautogui.click(criarContaX, criarContaY)
    espera(3)
    digitarEmailX = 987
    digitarEmailY = 353
    pyautogui.click(digitarEmailX, digitarEmailY)

    espera(2)
    pyautogui.write(pyperclip.paste())
    espera(2)

    # Parte de inserir uma senha e clicar em aceito e cadastrar
    digitarSenhaX = 984
    digitarSenhaY = 439
    pyautogui.click(digitarSenhaX, digitarSenhaY)
    pyautogui.write("glockzada123")
    espera(2)

    digitarNovamenteX = 974
    digitarNovamenteY = 530
    pyautogui.click(digitarNovamenteX, digitarNovamenteY)
    pyautogui.write("glockzada123")

    espera(3)
    aceitarX = 949
    aceitarY = 581
    pyautogui.click(aceitarX, aceitarY)

    espera(3)
    botaoCriarX = 1082
    botaoCriarY = 707
    pyautogui.click(botaoCriarX, botaoCriarY)

    espera(15)
    verificar_email()

def verificar_email(): # verifica o email pelo TEMP MAIL
    navegadorX = 217
    navegadorY = 747
    pyautogui.click(navegadorX, navegadorY)
    espera(2)

    abrirEmailX = 1018
    abrirEmailY = 695
    pyautogui.click(abrirEmailX, abrirEmailY)
    espera(2)

    scrollX = 1356
    scrollY = 140
    pyautogui.moveTo(scrollX, scrollY)
    espera(3)

    pyautogui.drag(xOffset=0, yOffset=130, duration=1)
    espera(2)

    botaoVerificarX = 670
    botaoVerificarY = 589
    pyautogui.click(botaoVerificarX, botaoVerificarY)

    espera(20)
    emailSiteX = 331
    emailSiteY = 419
    pyautogui.click(emailSiteX, emailSiteY)
    pyautogui.write(pyperclip.paste())

    espera(3)
    senhaSiteX = 445
    senhaSiteY = 489
    pyautogui.click(senhaSiteX, senhaSiteY)
    pyautogui.write("glockzada123")

    espera(3)
    logarX = 399
    logarY = 556
    pyautogui.click(logarX, logarY)

    espera(15)
    gerar_link()


def gerar_link(): # clica para pegar o link na stell e copia do navegador LEMBRAR DE FECHAR A STELL E LIMPAR OS CACHE
    steelX = 320
    steelY = 743
    pyautogui.click(steelX, steelY)
    espera(2)

    giveawayX = 118
    giveawayY = 371
    pyautogui.click(giveawayX, giveawayY)
    espera(3)

    pyautogui.moveTo(1359, 247) # move pra barrinha da steel series
    espera(2)
    pyautogui.drag(xOffset=0, yOffset=250, duration=1)

    espera(2)
    learnMoreX = 1150
    learnMoreY = 623
    pyautogui.click(learnMoreX, learnMoreY)

    espera(3)
    gerarX = 522
    gerarY = 61
    pyautogui.click(gerarX, gerarY)

    espera(3)
    gerarConfirmX = 670
    gerarConfirmY = 537
    pyautogui.click(gerarConfirmX, gerarConfirmY)

    espera(3)
    fecharNitroX = 892
    fecharNitroY = 190
    pyautogui.click(fecharNitroX, fecharNitroY)

    espera(20)
    cadastrar_link()

def cadastrar_link(): # cadastra o link no H$ PANEL
    linkNavegadorX = 444
    linkNavegadorY = 51
    pyautogui.click(linkNavegadorX, linkNavegadorY)
    mouse.click(Button.right)
    espera(1)
    pyautogui.click(487, 129)

    # fecha a página do link de nitro do navegador
    espera(2)
    fecharPagX = 619
    fecharPagY = 13
    pyautogui.click(fecharPagX, fecharPagY)

    # PARTE DO CADASTRO DO LINK NO H$ PANEL:
    espera(3)
    newLinkX = 292
    newLinkY = 503
    pyautogui.click(newLinkX, newLinkY)

    espera(2)
    digitarLinkX = 275
    digitarLinkY = 478
    pyautogui.click(digitarLinkX, digitarLinkY)
    pyautogui.write(pyperclip.paste())
    espera(1)
    pyautogui.click(265, 524)  # botao de save do panel
    espera(3)
    pyautogui.click(593, 171)  # clica em voltar para o inicio

def desconectar_conta():
    pass

def excluir_conta():
    # DELETANDO A CONTA DA STEEL NO SITE
    pyautogui.moveTo(1354, 205)  # move pra barrinha da steel series
    espera(2)
    pyautogui.drag(xOffset=0, yOffset=130, duration=1)

    espera(1)
    profileX = 148
    profileY = 298
    pyautogui.click(profileX, profileY)
    espera(2)
    pyautogui.moveTo(1357, 182)  # move pra barrinha da steel series
    pyautogui.drag(xOffset=0, yOffset=200, duration=1)

    espera(2)
    deletarX = 408
    deletaY = 431
    pyautogui.click(deletarX, deletaY)

    espera(2)
    confirmDeleteX = 509
    confirmDeleteY = 701
    pyautogui.click(confirmDeleteX, confirmDeleteY)

    espera(2)
    pyautogui.click(221, 13)  # clica para fechar a pagina

    # EXCLUINDO O EMAIL TEMPORARIO
    newPageX = 250
    newPageY = 10
    pyautogui.click(newPageX, newPageY)

    espera(2)
    pyautogui.click(782, 280)  # clica no google

    espera(3)
    pesquisaX = 470
    pesquisaY = 290
    pyautogui.click(pesquisaX, pesquisaY)

    espera(2)
    pyautogui.write('temp mail')
    pyautogui.press('enter')

    espera(4)
    tempMailX = 162
    tempMailY = 309
    pyautogui.click(tempMailX, tempMailY)

    espera(4)
    pyautogui.click(956, 530)  # clica em excluir email
def limpar_cookies(): # LIMPA OS COKI DO %APPDATA%
    pass
def gerar():
    criar_email()

#teste
pyautogui.alert('Gerador de Link de Discord Nitro 4 meses\n\nClique em "OK" e não mexa mais no computador!')
espera(2)
#gerar()

# Button.right
# link gerado no teste: https://discord.com/billing/promotions/GSeXPKaBJxzb4Q7NqSaG3jUD
# link gerado no teste 2: https://discord.com/billing/promotions/GXC5ceCwbnmwTxjBbKFse8ug
