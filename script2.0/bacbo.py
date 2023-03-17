import datetime
import requests
import telebot
import time
import json

class WebScraper:
    
    def __init__(self):
        # EDIT!
        self.game = "Bac bo"
        self.token = 'TOKEN DO BOT'
        self.chatid = 'CHAT ID'
        self.url_API = 'http://189.1.172.198:63000/bac-bo'
        self.gales = 2
        self.protection = True
        self.link = '[Clique aqui!](https://www.instagram.com/mscodex/)'
        
        
        # MAYBE EDIT!
        self.win_results = 0
        self.empate_results = 0
        self.loss_results = 0
        self.max_hate = 0
        # 
        self.win_hate = 0


        # NO EDIT!
        self.count = 0
        self.analisar = True
        self.direction_color = 'None'
        self.message_delete = False
        self.bot = telebot.TeleBot(token=self.token, parse_mode='MARKDOWN')
        self.date_now = str(datetime.datetime.now().strftime("%d/%m/%Y"))
        self.check_date = self.date_now

    def restart(self):
        if self.date_now != self.check_date:           
            print('Reiniciando bot!')
            self.check_date = self.date_now
            
            self.bot.send_sticker(
                self.chatid, sticker='CAACAgEAAxkBAAEBbJJjXNcB92-_4vp2v0B3Plp9FONrDwACvgEAAsFWwUVjxQN4wmmSBCoE')
            self.results()

            #ZERA OS RESULTADOS
            self.win_results = 0
            self.loss_results = 0
            self.empate_results = 0
            self.max_hate = 0
            self.win_hate = 0
            time.sleep(10)

            self.bot.send_sticker(
                self.chatid, sticker='CAACAgEAAxkBAAEBPQZi-ziImRgbjqbDkPduogMKzv0zFgACbAQAAl4ByUUIjW-sdJsr6CkE')
            self.results()
            return True
        else:
            return False

    def results(self):

        if self.win_results + self.empate_results + self.loss_results != 0:
            a = 100 / (self.win_results + self.empate_results + self.loss_results) * self.win_results + self.empate_results
        else:
            a = 0
        self.win_hate = (f'{a:,.2f}%')


        self.bot.send_message(chat_id=self.chatid, text=(f'''

► PLACAR GERAL = ✅{self.win_results} | 🟡{self.empate_results} | 🚫{self.loss_results} 
► Consecutivas = {self.max_hate}
► Assertividade = {self.win_hate}
    
    '''))
        return
       
    def alert_sinal(self):
        message_id = self.bot.send_message(
            self.chatid, text='''
⚠️ ANALISANDO, FIQUE ATENTO!!!
''').message_id
        self.message_ids = message_id
        self.message_delete = True
        return
    
    def alert_gale(self):
        self.message_ids = self.bot.send_message(self.chatid, text=f'''⚠️ Vamos para o {self.count}ª GALE''').message_id
        self.message_delete = True
        return

    def delete(self):
        if self.message_delete == True:
            self.bot.delete_message(chat_id=self.chatid,
                                    message_id=self.message_ids)
            self.message_delete = False
      
    def send_sinal(self):
        self.analisar = False
        self.bot.send_message(chat_id=self.chatid, text=(f'''

🎲 *ENTRADA CONFIRMADA!*

🎰 Apostar no {self.direction_color}
🟡 Proteger o empate (Meio) 
🔁 Fazer até {self.gales} gales

📱 *{self.game}* '''f'{self.link}''''

    '''))
        return

    def martingale(self, result):

        if result == "WIN":
            print(f"WIN")
            self.win_results += 1
            self.max_hate += 1
            self.bot.send_sticker(self.chatid, sticker='CAACAgEAAxkBAAEBuhtkFBbPbho5iUL3Cw0Zs2WBNdupaAACQgQAAnQVwEe3Q77HvZ8W3y8E')
            # self.bot.send_message(chat_id=self.chatid, text=(f'''✅✅✅ WIN ✅✅✅'''))
        
        elif result == "LOSS":
            self.count += 1
            
            if self.count > self.gales:
                print(f"LOSS")
                self.loss_results += 1
                self.max_hate = 0
                self.bot.send_sticker(self.chatid, sticker='CAACAgEAAxkBAAEBuh9kFBbVKxciIe1RKvDQBeDu8WfhFAACXwIAAq-xwEfpc4OHHyAliS8E')
                # self.bot.send_message(chat_id=self.chatid, text=(f'''🚫🚫🚫 LOSS 🚫🚫🚫'''))

            else:
                print(f"Vamos para o {self.count}ª gale!")
                self.alert_gale()
                return
            
        elif result == "EMPATE":
            print(f"EMPATE")
            self.empate_results += 1
            self.max_hate += 1
            self.bot.send_sticker(self.chatid, sticker='CAACAgEAAxkBAAEBuiNkFBbYDjGessfawWa3v9i4Kj35sgACQAUAAmq0wEejZcySuMSbsC8E')
            # self.bot.send_message(chat_id=self.chatid, text=(f'''✅✅✅ EMPATE ✅✅✅'''))

        self.count = 0
        self.analisar = True
        self.results()
        self.restart()
        return

    def check_results(self, results):

        if results == 'V' and self.direction_color == '🔴':
            self.martingale('WIN')
            return
        elif results == 'V' and self.direction_color == '🔵':
            self.martingale('LOSS')
            return


        if results == 'A' and self.direction_color == '🔵':
            self.martingale('WIN')
            return
        elif results == 'A' and self.direction_color == '🔴':
            self.martingale('LOSS')
            return

     
        if results == 'E' and self.protection == True:
            self.martingale('EMPATE')
            return              
        elif results == 'E' and self.protection == False:
            self.martingale('LOSS')
            return

    def start(self):
        check = []
        while True:
            try:
                self.date_now = str(datetime.datetime.now().strftime("%d/%m/%Y"))

                results = []
                time.sleep(1)

                response = requests.get(self.url_API)
                json_data = json.loads(response.text)
                for i in json_data['results']:
                    results.append(i)

                if check != results:
                    check = results
                    self.delete()
                    self.estrategy(results)
                
            except:
                print("ERROR - 404!")
                continue

    def estrategy(self, results):
        print(results[0:10])

        if self.analisar == False:
            self.check_results(results[0])
            return

        # EDITAR ESTRATÉGIAS
        elif self.analisar == True:

            if results[0:1] == ['V']:
                print('sinal azul')
                self.direction_color = '🔵'
                self.send_sinal()
                return

            if results[0:1] == ['A']:
                print('sinal vermelho')
                self.direction_color = '🔴'
                self.send_sinal()
                return


scraper = WebScraper()
scraper.start()