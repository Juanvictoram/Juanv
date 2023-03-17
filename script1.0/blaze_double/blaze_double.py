import datetime
import time


class utils:
    
    def get_data(self):
        self.now = str(datetime.datetime.now().strftime("%d/%m/%Y"))
        self.checknow = self.now
        self.nowtime = int(datetime.datetime.now().strftime("%H"))

    def send_sinal(self):
        print("Sinal enviado...")
        self.bot.send_message(chat_id=self.user_id, text=(f'''
🎲 *ENTRADA CONFIRMADA!*

🎰 Apostar no {self.direction_color}
⚪️ Proteger branco. 
🔁 Fazer até 2 gales

📱 *{self.name}*
'''))
        return

    def alert(self):
        message_id = self.bot.send_message(
            self.user_id, text='''
    ⚠️ Vamos para o %iª GALE ⚠️
            ''' % (self.entrada_atual)).message_id
        self.message_ids = message_id
        self.message_delete = True
        return

    def alert_sinal(self):
        message_id = self.bot.send_message(
            self.user_id, text='''
⚠️ ANALISANDO, FIQUE ATENTO!!!
''').message_id
        self.message_ids = message_id
        self.message_delete = True
        return

    def delet(self):
        if self.message_delete == True:
            self.bot.delete_message(chat_id=self.user_id,
                                message_id=self.message_ids)
            self.message_delete = False

    def results(self):
        if self.win_results + self.loss_results != 0:
            a = 100 / (self.win_results + self.loss_results) * self.win_results
        else:
            a = 0

        self.win_hate = (f'{a:,.2f}%')
        self.bot.send_message(chat_id=self.user_id, text=(f'''
📊 RESULTADO GERAL 
           ✅{self.win_results} VS 🚫{self.loss_results} 

► Win sem gale =  {self.win_semgale}
► Win 1ª gale  =  {self.win_gale1}
► Win 2ª gale  =  {self.win_gale2}
► Consecutivas = {self.max_hate}
► Assertividade = {self.win_hate}

👨🏾‍💻
    '''))
        return

    def restart(self):
        if self.now != self.checknow:
            print('Reload')
            self.bot.send_sticker(
                self.user_id, sticker='CAACAgEAAxkBAAEBbJJjXNcB92-_4vp2v0B3Plp9FONrDwACvgEAAsFWwUVjxQN4wmmSBCoE')
            utils.get_data(self)
            self.checknowtime = self.nowtime
            utils.results(self)

            self.win_results = 0
            self.loss_results = 0
            self.win_semgale = 0
            self.win_gale1 = 0
            self.win_gale2 = 0
            self.max_hate = 0
            self.empate_results = 0

            time.sleep(10)
            self.bot.send_sticker(
                self.user_id, sticker='CAACAgEAAxkBAAEBPQZi-ziImRgbjqbDkPduogMKzv0zFgACbAQAAl4ByUUIjW-sdJsr6CkE')
            utils.get_data(self)
            self.checknowtime = self.nowtime
            utils.results(self)
            return True
        else:
            return False

    def reset(self):
        self.analise_open = 0
        self.analisar = 0
        self.entrada_atual = 0

        if not utils.restart(self):
            utils.results(self)
        return

    def martingale(self):
        if self.result == 'B':
            if self.entrada_atual == 0:
                self.max_hate += 1
                self.win_results += 1
                self.empate_results += 1
                self.empate_semgale += 1
                self.win_semgale += 1
                self.bot.send_message(chat_id=self.user_id, text=(f'''
    ⚪️⚪️⚪️ BRANCO ⚪️⚪️⚪️
        {self.empate_results}ª BRANCO DO DIA!!!
    '''))
                utils.reset(self)
                return

            if self.entrada_atual == 1:
                self.max_hate += 1
                self.win_results += 1
                self.empate_results += 1
                self.empate_gale1 += 1
                self.win_gale1 += 1
                self.bot.send_message(chat_id=self.user_id, text=(f'''
    ⚪️⚪️⚪️ BRANCO ⚪️⚪️⚪️
        {self.empate_results}ª BRANCO DO DIA!!!
    '''))
                utils.reset(self)
                return

            if self.entrada_atual == 2:
                self.max_hate += 1
                self.win_results += 1
                self.empate_results += 1
                self.empate_gale2 += 1
                self.win_gale1 += 1
                self.bot.send_message(chat_id=self.user_id, text=(f'''
    ⚪️⚪️⚪️ BRANCO ⚪️⚪️⚪️
        {self.empate_results}ª BRANCO DO DIA!!!
    '''))
                utils.reset(self)
                return

        if self.result == 'V' and self.direction_color == '🔴':
            if self.entrada_atual == 0:
                self.win_results += 1
                self.max_hate += 1
                self.win_semgale += 1
                self.bot.send_message(chat_id=self.user_id, text=(f'''
✅✅✅ GREEN!!! ✅✅✅
(🔴)'''))
                utils.reset(self)
                return

            if self.entrada_atual == 1:
                self.win_results += 1
                self.max_hate += 1
                self.win_gale1 += 1
                self.bot.send_message(chat_id=self.user_id, text=(f'''
✅✅✅ GREEN!!! ✅✅✅
(⚫️🔴)'''))
                utils.reset(self)
                return

            if self.entrada_atual == 2:
                self.win_results += 1
                self.max_hate += 1
                self.win_gale2 += 1
                self.bot.send_message(chat_id=self.user_id, text=(f'''
✅✅✅ GREEN!!! ✅✅✅
(⚫️⚫️🔴)'''))
                utils.reset(self)
                return

        if self.result == 'P' and self.direction_color == '⚫️':
            if self.entrada_atual == 0:
                self.win_results += 1
                self.max_hate += 1
                self.win_semgale += 1
                self.bot.send_message(chat_id=self.user_id, text=(f'''
✅✅✅ GREEN!!! ✅✅✅
(⚫️)'''))
                utils.reset(self)
                return

            if self.entrada_atual == 1:
                self.win_results += 1
                self.max_hate += 1
                self.win_gale1 += 1
                self.bot.send_message(chat_id=self.user_id, text=(f'''
✅✅✅ GREEN!!! ✅✅✅
(🔴⚫️)'''))
                utils.reset(self)
                return

            if self.entrada_atual == 2:
                self.win_results += 1
                self.max_hate += 1
                self.win_gale2 += 1
                self.bot.send_message(chat_id=self.user_id, text=(f'''
✅✅✅ GREEN!!! ✅✅✅
(🔴🔴⚫️)'''))
                utils.reset(self)
                return

        if self.result == 'P' and self.direction_color == '🔴':
            if self.entrada_atual == 0:
                self.entrada_atual += 1
                utils.alert(self)
                return

            if self.entrada_atual == 1:
                self.entrada_atual += 1
                utils.alert(self)
                return

            if self.entrada_atual == 2:
                self.loss_results += 1
                self.bot.send_message(chat_id=self.user_id, text=(f'''
Loss🚫'''))
                utils.reset(self)
                self.max_hate = 0
                return

        if self.result == 'V' and self.direction_color == '⚫️':
            if self.entrada_atual == 0:
                self.entrada_atual += 1
                utils.alert(self)
                return

            if self.entrada_atual == 1:
                self.entrada_atual += 1
                utils.alert(self)
                return

            if self.entrada_atual == 2:
                self.loss_results += 1
                self.bot.send_message(chat_id=self.user_id, text=(f'''
Loss🚫'''))
                utils.reset(self)
                self.max_hate = 0
                return

    def estrategy(self, finalcor):
        lista = []

        for i in finalcor:
            if i >= 1 and i <= 7:
                lista.append("V")
            elif i >= 8 and i <= 17:
                lista.append("P")
            else:
                lista.append("B")


        if self.analisar == 1:
            self.result = lista[0]
            utils.martingale(self)
            return
        
        elif self.analisar == 0:
            if lista[0:3] == ['V', 'V', 'P']:
                self.direction_color = '⚫️'
                self.analisar = 1
                utils.send_sinal(self)
                return

            if lista[0:3] == ['P', 'P', 'V']:
                self.direction_color = '🔴'
                self.analisar = 1
                utils.send_sinal(self)
                return

            if lista[0:2] == ['V', 'P']:
                utils.alert_sinal(self)
                return

            if lista[0:2] == ['P', 'V']:
                utils.alert_sinal(self)
                return


