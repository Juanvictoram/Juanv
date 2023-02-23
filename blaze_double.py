import telebot


token_bot = "TOKEN DO BOT"
chat_id = "CHAT ID DO CANAL\GRUPO"
bot = telebot.TeleBot(token_bot)

bot.send_message(chat_id, text="Online")

analise_open = False
entrada_atual = 0
max_gale = int(input("Quantos martingale: "))

def reset():
    global analise_open
    global entrada_atual

    analise_open = False
    entrada_atual = 0

    return

def win():
    bot.send_message(chat_id, text=f'''
WIN
    ''')
    reset()
    return

def loss():
    bot.send_message(chat_id, text=f'''
LOSS
    ''')
    reset()
    return

def branco():
    bot.send_message(chat_id, text=f'''
BRANCO
    ''')
    reset()
    return

def martingale():
    global entrada_atual
    entrada_atual += 1

    if entrada_atual <= max_gale:
        bot.send_message(chat_id, text=f'''
Vamos para o gale {entrada_atual}
    ''')
    
    else:
        loss()
        reset()

    return

def send_result(resultado, color):
    if resultado[0] >= 1 and resultado[0] <= 7 and color == "🟥":
        win()
        return

    elif resultado[0] >= 1 and resultado[0] <= 7 and color == "⬛️":
        martingale()
        return
    
    elif resultado[0] >= 8 and resultado[0] <= 14 and color == "⬛️":
        win()
        return

    elif resultado[0] >= 8 and resultado[0] <= 14 and color == "🟥":
        martingale()
        return
    
    else:
        branco()    
    return

def send_sinal(color):
    bot.send_message(chat_id, text=f'''
Sinal ENVIADO   
ENTRAR: {color}
    ''')

    return

def estrategy(resultado):
    global analise_open
    global color_sinal

    lista_ultimas_cores = []
    
    for i in resultado:
        if i >= 1 and i <= 7:
            cor = "V"
            lista_ultimas_cores.append(cor)
        elif i >= 8 and i <= 14:
            cor = "P"
            lista_ultimas_cores.append(cor)
        else:
            cor = "B"
            lista_ultimas_cores.append(cor)
    
    print(lista_ultimas_cores)

    if analise_open == True:
        send_result(resultado, color_sinal)
    else:
        if lista_ultimas_cores[0:3] == ["P", "P", "V"]:
            color_sinal = "🟥"
            send_sinal(color_sinal)
            analise_open = True

        if lista_ultimas_cores[0:3] == ["V", "V", "P"]:
            color_sinal = "⬛️"
            send_sinal(color_sinal)
            analise_open = True

