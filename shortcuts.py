# Biblioteca simples para simplificar algumas funções das libs pyautogui, pyperclip e time.

# Importações.
import pyautogui
import pyperclip
import time

# Copia um conteúdo de texto.
def copy(content):
    return pyperclip.copy(content)

# Pressiona teclas em número desejado de vezes.
def press(times, *key):
    i = 0

    while (i < times):
        pyautogui.hotkey(*key)
        i += 1

# Aguarda n segundos.
def wait(seconds):
    return time.sleep(seconds)