# -*- coding: utf-8 -*-
import os

API_TOKEN = os.environ['TG_BOT_TOKEN']

DATABASE_NAME = "tg_bot_requests.sqlite"

MAX_TEXT_LENGTH = 250
HELP_COMMAND_RESPONCE_TEXT = '''Қалайсың {0}?
* Диграф негізіндегі нұсқамен аудару үшін /1 сосын мәтініңді тер
* Апостроф негізіндегі нұсқамен аудару үшін /2 сосын мәтініңді тер
* KazakGrammar нұсқасымен аудару үшін /3 сосын мәтініңді тер

Как дела {0}?
* набери /1 и свой текст для варианта на основе диграфов
* набери /2 и свой текст для варианта на основе апострофов
* набери /3 и свой текст для варианта проекта KazakGrammar'''

SHORT_CONTENT_RESPONCE_TEXT = "{0}, Мынаны қолмен де аудара салсаң болатын еді ғой | {0}, мог бы и сам это сделать"
EMPTY_CONTENT_RESPONCE_TEXT = "{0}, мен нені аударам сонда? | {0}, мне же нечего конвертировать"
EMPTY_CONTENT_RESPONCE_TEXT2 = "Мәтінді теруді ұмытпа | Передай мне текст"
DEFAULT_RESPONCE_TEXT = "Қойсайшы ойнамай, {}. Сындырасың ғой"
LONG_CONTENT_RESPONCE_TEXT = "{1}, мәтін өте ұзын, мен тек {0} ғана аудара аламын | {1}, слишком длинный текст. Я могу конвертировать лишь {0}"
NO_KAZ_CONTENT_RESPONCE_TEXT = "{0}, ұмытпасаң, мен қазақшадан аударамын ғой | {0}, если ты не забыл, Я конвертирую с казахского языка"
FEEDBACK_COMMAND_RESPONCE_TEXT = "Telegram: @armandyne, e-mail: armanndyne@gmail.com"
