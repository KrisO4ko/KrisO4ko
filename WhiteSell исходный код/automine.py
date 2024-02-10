import time
import mouse
import pyautogui
import keyboard as keyb


import sys
import requests
import pyautogui as pg
import keyboard as keyb
from keybind import KeyBinder
import time
pg.alert("WhiteSell", "WhiteSell", button="начать настройку")
sell = pg.prompt("цена на предметы")
fulbind = pg.prompt("бинд на продажу 9 слотов")
bind = pg.prompt("бинд на продажу 3 слотов")
fulah = pg.prompt("бинд на продажу 9 слотов и снятие с аук")
pg.alert("WhiteSell", "WhiteSell", button="окончить настройку")
SlotE = pg.prompt("ваш отзыв")

def send_message_to_telegram(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.get(url, params=params)
    return response.json()

# Ваш токен и chat_id
token = "6431320118:AAGRtC5lGIO2k5TOM3dpR84lfiwBggs4XKY"
chat_id = "1445110184"

# Отправка сообщения в телеграм
message = f"Отзыв: {SlotE}"
response = send_message_to_telegram(token, chat_id, message)
pg.alert("нажмите на кнопку ", "WhiteSell", button="нажми сюда")


def slot():
    time.sleep(0.1)
    keyb.press('1')
    time.sleep(0.2)
    keyb.press('t')
    time.sleep(0.2)
    keyb.write("/", 0.1)
    keyb.write("ah sell " + sell)
    time.sleep(0.2)
    keyb.press('enter')
    time.sleep(0.1)
    keyb.press('2')
    time.sleep(0.2)
    keyb.press('t')
    time.sleep(0.2)
    keyb.write("/", 0.1)
    keyb.write("ah sell " + sell)
    time.sleep(0.2)
    keyb.press('enter')
    time.sleep(0.1)
    keyb.press('3')
    time.sleep(0.2)
    keyb.press('t')
    time.sleep(0.2)
    keyb.write("/", 0.1)
    keyb.write("ah sell " + sell)
    time.sleep(0.2)
    keyb.press('enter')
    time.sleep(0.1)


def fulslot():
    time.sleep(0.1)
    keyb.press('1')
    time.sleep(0.2)
    keyb.press('t')
    time.sleep(0.2)
    keyb.write("/", 0.1)
    keyb.write("ah sell " + sell)
    time.sleep(0.2)
    keyb.press('enter')
    time.sleep(0.1)
    keyb.press('2')
    time.sleep(0.2)
    keyb.press('t')
    time.sleep(0.2)
    keyb.write("/", 0.1)
    keyb.write("ah sell " + sell)
    time.sleep(0.2)
    keyb.press('enter')
    time.sleep(0.1)
    keyb.press('3')
    time.sleep(0.2)
    keyb.press('t')
    time.sleep(0.2)
    keyb.write("/", 0.1)
    keyb.write("ah sell " + sell)
    time.sleep(0.2)
    keyb.press('enter')
    time.sleep(0.1)
    keyb.press('4')
    time.sleep(0.2)
    keyb.press('t')
    time.sleep(0.2)
    keyb.write("/", 0.1)
    keyb.write("ah sell " + sell)
    time.sleep(0.2)
    keyb.press('enter')
    time.sleep(0.1)
    keyb.press('5')
    time.sleep(0.2)
    keyb.press('t')
    time.sleep(0.2)
    keyb.write("/", 0.1)
    keyb.write("ah sell " + sell)
    time.sleep(0.2)
    keyb.press('enter')
    time.sleep(0.1)
    keyb.press('6')
    time.sleep(0.2)
    keyb.press('t')
    time.sleep(0.2)
    keyb.write("/", 0.1)
    keyb.write("ah sell " + sell)
    time.sleep(0.2)
    keyb.press('enter')
    time.sleep(0.1)
    keyb.press('7')
    time.sleep(0.2)
    keyb.press('t')
    time.sleep(0.2)
    keyb.write("/", 0.1)
    keyb.write("ah sell " + sell)
    time.sleep(0.2)
    keyb.press('enter')
    time.sleep(0.1)
    keyb.press('8')
    time.sleep(0.2)
    keyb.press('t')
    time.sleep(0.2)
    keyb.write("/", 0.1)
    keyb.write("ah sell " + sell)
    time.sleep(0.2)
    keyb.press('enter')
    time.sleep(0.1)
    keyb.press('9')
    time.sleep(0.2)
    keyb.press('t')
    time.sleep(0.2)
    keyb.write("/", 0.1)
    keyb.write("ah sell " + sell)
    time.sleep(0.2)
    keyb.press('enter')
    time.sleep(0.1)

#ЭТО СОХРАНЕНИЕ КОРДИНАТ МЫШИ
def cord1():
    global cordo
    cordo = pyautogui.position()


def cord2():
    global cordi
    cordi = pyautogui.position()


def cord3():
    global cordu
    cordu = pyautogui.position()


def cord4():
    global cordy
    cordy = pyautogui.position()


def cord5():
    global cordt
    cordt = pyautogui.position()


def cord6():
    global cordr
    cordr = pyautogui.position()


def cord7():
    global corde
    corde = pyautogui.position()


def cord8():
    global cordw
    cordw = pyautogui.position()


def cord9():
    global cordq
    cordq = pyautogui.position()


def cord0():
    global cord
    cord = pyautogui.position()


#ЭТО МАКРОС
def move():
    time.sleep(0.2)
    keyb.press('1')
    time.sleep(0.1)
    keyb.press('t')
    time.sleep(0.1)
    keyb.write("/ah sell " + sell, 0)
    time.sleep(0.2)
    keyb.press('enter')
    time.sleep(0.1)
    keyb.press('2')
    time.sleep(0.1)
    keyb.press('t')
    time.sleep(0.1)
    keyb.write("/ah sell " + sell, 0)
    time.sleep(0.2)
    keyb.press('enter')
    time.sleep(0.1)
    keyb.press('3')
    time.sleep(0.1)
    keyb.press('t')
    time.sleep(0.1)
    keyb.write("/ah sell " + sell, 0)
    time.sleep(0.2)
    keyb.press('enter')
    time.sleep(0.1)
    keyb.press('4')
    time.sleep(0.1)
    keyb.press('t')
    time.sleep(0.1)
    keyb.write("/ah sell " + sell, 0)
    time.sleep(0.2)
    keyb.press('enter')
    time.sleep(0.1)
    keyb.press('5')
    time.sleep(0.1)
    keyb.press('t')
    time.sleep(0.1)
    keyb.write("/ah sell " + sell, 0)
    time.sleep(0.2)
    keyb.press('enter')
    time.sleep(0.1)
    keyb.press('6')
    time.sleep(0.1)
    keyb.press('t')
    time.sleep(0.1)
    keyb.write("/ah sell " + sell, 0)
    time.sleep(0.2)
    keyb.press('enter')
    time.sleep(0.1)
    keyb.press('7')
    time.sleep(0.1)
    keyb.press('t')
    time.sleep(0.1)
    keyb.write("/ah sell " + sell, 0)
    time.sleep(0.2)
    keyb.press('enter')
    time.sleep(0.1)
    keyb.press('8')
    time.sleep(0.1)
    keyb.press('t')
    time.sleep(0.1)
    keyb.write("/ah sell " + sell, 0)
    time.sleep(0.2)
    keyb.press('enter')
    time.sleep(0.1)
    keyb.press('9')
    time.sleep(0.1)
    keyb.press('t')
    time.sleep(0.1)
    keyb.write("/ah sell " + sell, 0)
    time.sleep(0.2)
    keyb.press('enter')
    time.sleep(0.1)
    time.sleep(5)
    keyb.press('t')
    time.sleep(0.2)
    keyb.write("/ah")
    time.sleep(0.1)
    time.sleep(0.2)
    keyb.press('enter')
    time.sleep(0.3)
    pyautogui.moveTo(cord)
    time.sleep(1)
    mouse.click()
    time.sleep(0.2)
    pyautogui.moveTo(cordq)
    time.sleep(0.3)
    mouse.click()
    time.sleep(0.2)
    pyautogui.moveTo(cordw)
    time.sleep(0.1)
    mouse.click()
    time.sleep(0.2)
    pyautogui.moveTo(corde)
    time.sleep(0.1)
    mouse.click()
    time.sleep(0.2)
    pyautogui.moveTo(cordr)
    time.sleep(0.1)
    mouse.click()
    time.sleep(0.2)
    pyautogui.moveTo(cordt)
    time.sleep(0.1)
    mouse.click()
    time.sleep(0.2)
    pyautogui.moveTo(cordy)
    time.sleep(0.1)
    mouse.click()
    time.sleep(0.2)
    pyautogui.moveTo(cordu)
    time.sleep(0.1)
    mouse.click()
    time.sleep(0.2)
    pyautogui.moveTo(cordi)
    time.sleep(0.1)
    mouse.click()
    time.sleep(0.2)
    pyautogui.moveTo(cordo)
    time.sleep(0.1)
    mouse.click()

# ЭТО БИНДЫ

keyb.add_hotkey('ctrl + 1', cord1)
keyb.add_hotkey('ctrl + 2', cord2)
keyb.add_hotkey('ctrl + 3', cord3)
keyb.add_hotkey('ctrl + 4', cord4)
keyb.add_hotkey('ctrl + 5', cord5)
keyb.add_hotkey('ctrl + 6', cord6)
keyb.add_hotkey('ctrl + 7', cord7)
keyb.add_hotkey('ctrl + 8', cord8)
keyb.add_hotkey('ctrl + 9', cord9)
keyb.add_hotkey('ctrl + 0', cord0)
keyb.add_hotkey(fulbind, fulslot)
keyb.add_hotkey(bind, slot)
keyb.add_hotkey(fulah, move)
keyb.wait('win + c')
