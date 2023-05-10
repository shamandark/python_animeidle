import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '6121461069:AAGmETgcEglJEhXc-ytSQ9ccXS9d0Gbme4I'

bot = telebot.TeleBot(TOKEN)


# Função para criar a mensagem de boas-vindas
def mensagem_boas_vindas():
    return "Bem vindo ao AnimeIdle, para começar digite /Menu e envie, Bom divertimento!!!"


# Função para criar o menu principal
def menu_principal():
    menu = InlineKeyboardMarkup(row_width=7)
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z', '0123']
    botoes = [InlineKeyboardButton(f'{letra}', callback_data=f'letra_{letra}') for letra in letras]
    menu.add(*botoes)
    return menu


# Função para criar o submenu
def submenu_letra(letra):
    submenu = InlineKeyboardMarkup(row_width=1)
    opcoes = []
    if letra == 'A':
        opcoes = [
            ('Akame ga kill', 'https://t.me/animeidle_A/3'),
            ('Akudama Drive', 'https://t.me/animeidle_A/28/29'),
			('Arifureta From Commonplace to World s Strongest', 'https://t.me/animeidle_A/42/43'),
			('Aiyou de Mishi', 'https://t.me/animeidle_A/70/71'),
            ('FALE_CONOSCO', 'https://t.me/faleconoscoanimeidle'),
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3')
        ]
    elif letra == 'B':
        opcoes = [
            ('Blue Lock', 'https://t.me/animes_letra_B/2/3'),
            ('Boku no Hero Academia', 'https://t.me/animes_letra_B/28/29'),
            ('Boku no Kokoro no Yabai Yatsua', 'https://t.me/animes_letra_B/31/32'),
            ('Benriya Saitou san Isekai ni Iku', 'https://t.me/animes_letra_B/38/39'),
			('Banana Fish', 'https://t.me/animes_letra_B/166'),
            ('FALE_CONOSCO', 'https://t.me/faleconoscoanimeidle'),
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3')
        ]
    elif letra == 'C':
        opcoes = [
            ('Chainsaw Man', 'https://t.me/animes_letra_C/15'),
            ('FALE_CONOSCO', 'https://t.me/faleconoscoanimeidle'),
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3')
        ]
    elif letra == 'D':
        opcoes = [
            ('Dead Mount Death Play', 'https://t.me/animes_letra_D/53/55'),
			('Darwin s Game', 'https://t.me/animes_letra_D/60/61'),
            ('Dr Stone', 'https://t.me/animes_letra_D/10'),
			('Deatte 5-byou de Battle', 'https://t.me/animes_letra_D/73/74'),
            ('FALE_CONOSCO', 'https://t.me/faleconoscoanimeidle'),
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3')
        ]
    elif letra == 'E':
        opcoes = [
            ('Engage Kiss', 'https://t.me/animes_letra_E/2/3'),
            ('FALE_CONOSCO', 'https://t.me/faleconoscoanimeidle'),
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3')
        ]
    elif letra == 'F':
        opcoes = [
            ('Fuufu Ijou Koibito Miman', 'https://t.me/animes_letra_F/2/3'),
			('Fate/Stay Night: Unlimited Blade Works', 'https://t.me/animes_letra_F/16/17'),
			('Fire Force', 'https://t.me/animes_letra_F/43/44'),
            ('FALE_CONOSCO', 'https://t.me/faleconoscoanimeidle'),
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3')
        ]
    elif letra == 'G':
        opcoes = [
            ('Gleipnir', 'https://t.me/animes_letra_G/2/3'),
			('Gotoubun no Hanayome', 'https://t.me/animes_letra_G/17/18'),
			('Goblin Slayer', 'https://t.me/animes_letra_G/19/20'),
            ('FALE_CONOSCO', 'https://t.me/faleconoscoanimeidle'),
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3')
        ]
    elif letra == 'H':
        opcoes = [
            ('High School of the Dead', 'https://t.me/animes_letra_H/2/3'),
			('Horimiya', 'https://t.me/animes_letra_H/4/5'),
			('Hyouka', 'https://t.me/animes_letra_H/16'),
            ('FALE_CONOSCO', 'https://t.me/faleconoscoanimeidle'),
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3')
        ]
    elif letra == 'I':
        opcoes = [
            ('Isekai Nonbiri Nouka', 'https://t.me/animeidle_I/3'),
            ('Harem in the Labyrinth of Another World', 'https://t.me/animeidle_I/16/17'),
			('Isekai Ojisan', 'https://t.me/animeidle_I/30/31'),
            ('FALE_CONOSCO', 'https://t.me/faleconoscoanimeidle'),
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3')
        ]
    elif letra == 'J':
        opcoes = [
            ('Jigokuraku Hells Paradise', 'https://t.me/animes_letra_J/8/11'),
			('Jujutsu Kaisen', 'https://t.me/animes_letra_J/16'),
            ('FALE_CONOSCO', 'https://t.me/faleconoscoanimeidle'),
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3')
        ]
    elif letra == 'K':
        opcoes = [
            ('Kimetsu no Yaiba', 'https://t.me/animes_letra_K/2'),
            ('Kage no Jitsuryokusha ni Naritakute', 'https://t.me/animes_letra_K/128/129'),
            ('Kakkou no Iinazuke', 'https://t.me/animes_letra_K/81/82'),
            ('KamiKatsu Atividades Divinas em um Mundo sem Deuses', 'https://t.me/animes_letra_K/74/75'),
            ('Kaifuku Jutsushi no Yarinaoshi', 'https://t.me/animes_letra_K/109/110'),
            ('FALE_CONOSCO', 'https://t.me/faleconoscoanimeidle'),
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3')
        ]
    elif letra == 'L':
        opcoes = [
            ('Lycoris Recoil', 'https://t.me/animes_letra_L/2/3'),
            ('FALE_CONOSCO', 'https://t.me/faleconoscoanimeidle'),
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3')
        ]
    elif letra == 'M':
        opcoes = [
            ('My Home Hero', 'https://t.me/animes_letra_M/21/22'),
            ('Mamahaha no Tsurego ga Moto Kano datta', 'https://t.me/animes_letra_M/8'),
            ('MASHLE MAGIC AND MUSCLES', 'https://t.me/animes_letra_M/28/30'),
            ('FALE_CONOSCO', 'https://t.me/faleconoscoanimeidle'),
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3')
        ]
    elif letra == 'N':
        opcoes = [
            ('No Game No Life', 'https://t.me/animes_letra_N/4/5'),
            ('FALE_CONOSCO', 'https://t.me/faleconoscoanimeidle'),
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3')
        ]
    elif letra == 'O':
        opcoes = [
            ('Oshi no Ko', 'https://t.me/animes_letra_O/2/3'),
            ('Otome Game Sekai wa Mob ni Kibishii Sekai desu', 'https://t.me/animes_letra_O/10/11'),
            ('One Punch Man', 'https://t.me/animes_letra_O/24/25'),
			('OreGairu Yahari Ore no Seishun Love Comedy wa Machigatteiru', 'https://t.me/animes_letra_O/50'),
            ('FALE_CONOSCO', 'https://t.me/faleconoscoanimeidle'),
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3')
        ]
    elif letra == 'P':
        opcoes = [
            ('Paripi Koumei', 'https://t.me/animes_letra_P/2/3'),
            ('FALE_CONOSCO', 'https://t.me/faleconoscoanimeidle'),
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3')
        ]
    elif letra == 'Q':
        opcoes = [
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3'),
            ('FALE_CONOSCO', 'https://t.me/faleconoscoanimeidle'),
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3')
        ]
    elif letra == 'R':
        opcoes = [
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3'),
            ('FALE_CONOSCO', 'https://t.me/faleconoscoanimeidle'),
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3')
        ]
    elif letra == 'S':
        opcoes = [
            ('Spy x Family', 'https://t.me/animes_letra_S/2'),
            ('Saikyou Onmyouji no Isekai Tenseiki', 'https://t.me/animes_letra_S/28'),
            ('Summer Time Rendering', 'https://t.me/animes_letra_S/42/43'),
            ('Sword Art Online', 'https://t.me/animes_letra_S/69/70'),
			('Shield Hero', 'https://t.me/animes_letra_S/121/122'),
            ('FALE_CONOSCO', 'https://t.me/faleconoscoanimeidle'),
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3')
        ]
    elif letra == 'T':
        opcoes = [
            ('Tomodachi Game', 'https://t.me/animes_letra_T/2/3'),
            ('Tokyo Revengers', 'https://t.me/animes_letra_T/6/7'),
            ('Tengoku Daimakyo Ilusão Celestial', 'https://t.me/animes_letra_T/45/46'),
            ('Tensei shitara Ken Deshita', 'https://t.me/animes_letra_T/47/54'),
			('Tower of God', 'https://t.me/animes_letra_T/69'),
			('The God of High School', 'https://t.me/animes_letra_T/71'),			
            ('FALE_CONOSCO', 'https://t.me/faleconoscoanimeidle'),
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3')
        ]
    elif letra == 'U':
        opcoes = [
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3'),
            ('FALE_CONOSCO', 'https://t.me/faleconoscoanimeidle'),
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3')
        ]
    elif letra == 'V':
        opcoes = [
            ('Vanitas no Carte', 'https://t.me/animes_letra_V/2/3'),
			('Vinland Saga', 'https://t.me/animes_letra_V/28/29'),
            ('FALE_CONOSCO', 'https://t.me/faleconoscoanimeidle'),
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3')
        ]
    elif letra == 'W':
        opcoes = [
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3'),
            ('FALE_CONOSCO', 'https://t.me/faleconoscoanimeidle'),
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3')
        ]
    elif letra == 'X':
        opcoes = [
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3'),
            ('FALE_CONOSCO', 'https://t.me/faleconoscoanimeidle'),
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3')
        ]
    elif letra == 'Y':
        opcoes = [
            ('Yuusha ga Shinda!', 'https://t.me/animes_letra_Y/2/3'),
			('Yamada-kun to Lv999 no Koi wo Suru', 'https://t.me/animes_letra_Y/9/10'),
            ('FALE_CONOSCO', 'https://t.me/faleconoscoanimeidle'),
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3')
        ]
    elif letra == 'Z':
        opcoes = [
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3'),
            ('FALE_CONOSCO', 'https://t.me/faleconoscoanimeidle'),
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3')
        ]
    elif letra == '0123':
        opcoes = [
            ('86: Eighty-Six', 'https://t.me/animes_letra_0123/2/4'),
            ('FALE_CONOSCO', 'https://t.me/faleconoscoanimeidle'),
            ('CONHEÇA NOSSO CANAL DE FILMES', 'https://t.me/idlemovies3')

        ]

    botoes = [InlineKeyboardButton(opcao[0], url=opcao[1]) for opcao in opcoes]
    submenu.add(*botoes)
    submenu.add(InlineKeyboardButton('Voltar', callback_data='voltar'))
    return submenu


# Função para tratar a seleção da opção no submenu
def selecionar_opcao(call):
    opcao = call.data.split('_')[1]
    bot.answer_callback_query(callback_query_id=call.id)
    bot.send_message(call.message.chat.id, f'Você selecionou a opção {opcao}')


# Função para tratar o callback do menu principal
@bot.callback_query_handler(func=lambda call: call.data.startswith('letra'))
def callback_menu_principal(call):
    letra = call.data.split('_')[1]
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text=f'Você selecionou a letra {letra}. Selecione uma opção:',
                          reply_markup=submenu_letra(letra))


# Função para tratar o callback do submenu para voltar ao menu principal
@bot.callback_query_handler(func=lambda call: call.data == 'voltar')
def voltar(call):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text='Selecione uma letra:', reply_markup=menu_principal())


# Função para tratar a seleção da opção no submenu
def selecionar_opcao(call):
    opcao = call.data.split('_')[1]
    bot.answer_callback_query(callback_query_id=call.id)
    bot.send_message(call.message.chat.id, f'Você selecionou a opção {opcao}')


# Função para tratar o callback do menu principal
@bot.callback_query_handler(func=lambda call: call.data.startswith('letra'))
def callback_menu_principal(call):
    letra = call.data.split('_')[1]
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text=f'Você selecionou a letra {letra}. Selecione uma opção:',
                          reply_markup=submenu_letra(letra))


# Função para tratar o callback do submenu para voltar ao menu principal
@bot.callback_query_handler(func=lambda call: call.data == 'voltar')
def voltar(call):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text='Selecione uma letra:', reply_markup=menu_principal())


# Função para tratar a seleção da opção no submenu
def selecionar_opcao(call):
    opcao = call.data.split('_')[1]
    bot.answer_callback_query(callback_query_id=call.id)
    bot.send_message(call.message.chat.id, f'Você selecionou a opção {opcao}')


# Função para tratar o callback do menu principal
@bot.callback_query_handler(func=lambda call: call.data.startswith('letra'))
def callback_menu_principal(call):
    letra = call.data.split('_')[1]
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text=f'Você selecionou a letra {letra}. Selecione uma opção:',
                          reply_markup=submenu_letra(letra))


# Função para tratar o callback do submenu para voltar ao menu principal
@bot.callback_query_handler(func=lambda call: call.data == 'voltar')
def voltar(call):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text='Selecione uma letra:',
                          reply_markup=menu_principal())


# Função para enviar o menu principal quando o comando /menu for utilizado
@bot.message_handler(commands=['menu'])
def enviar_menu(message):
    bot.send_message(message.chat.id, 'Selecione uma letra:', reply_markup=menu_principal())


def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
   Bem vindo ao Animedle, para começar digite /menu e envie, Bom divertimento!!!
Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)


bot.polling(none_stop=True, interval=0, timeout=180)

bot.polling()

