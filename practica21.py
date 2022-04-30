'''
Practica 21
Utilizando la librería PYAUTOGUI, generar una buena broma (conocidas como prank) en la que el programa de Python 
tome el control ya sea del ratón o del teclado o de ambos, para confundir al usuario... 
(Este será calificado como los deportes de apreciación, clavados, patinaje artístico, gimnasia, entre más mejor la broma, 
más calificación se obtendrá =P) si en algún punto de su existencia toman como interesante el usar FORMAT C:, pues, 
consideren ser pasado por la guillotinización =D
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''
#correr en el spyder porque en vs no respeta el tiempo que tarda
import pyautogui

print(pyautogui.position())
pyautogui.hotkey('win')
pyautogui.typewrite('https://matias.ma/nsfw/')
pyautogui.hotkey('enter')
pyautogui.click(x=960, y=540, clicks=1, interval=1, button='left')
pyautogui.hotkey('ctrl','n')
pyautogui.hotkey('ctrl','shift','j')
pyautogui.typewrite('while(true) {alert("Pongame 10!!")}')
pyautogui.hotkey('enter')
pyautogui.hotkey('win')
pyautogui.typewrite('cmd')
pyautogui.hotkey('enter')
pyautogui.typewrite('shutdown /s')
pyautogui.PAUSE = 2.5
pyautogui.typewrite('ahhhhhhhhhhhhhhh que dijo')
pyautogui.hotkey('enter')
pyautogui.typewrite('exit')
pyautogui.hotkey('enter')
