import pyautogui
import time

def pegar_coord():
	pyautogui.alert('Para pegar o X e o Y\nClique em OK')
	time.sleep(2)
	item = pyautogui.position()

	pyautogui.alert('X e Y pegos com sucesso!')

	return item


x = pegar_coord()
print(f'X = {x[0]}\nY = {x[1]}')