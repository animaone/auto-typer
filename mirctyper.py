import window_searcher
import ctypes
import win32gui
import win32con
import win32api
import time
import win32ui
import win32clipboard

#imported functions
#========================================================
keybd_event = win32api.keybd_event
MapVirtualKeyA = ctypes.windll.user32.MapVirtualKeyA
FindWindow = win32gui.FindWindow
SetForegroundWindow = win32gui.SetForegroundWindow
SendMessage = win32gui.SendMessage
GetKeyState = win32api.GetKeyState
#========================================================



#==============================================================
v_key = ord('V')

def send_paste():
	win32api.keybd_event(win32con.VK_CONTROL , 0, 0, 0)	
	
	keybd_event(v_key, 0, 0, 0)
	time.sleep(0.1)
	keybd_event(v_key, 0, win32con.KEYEVENTF_KEYUP, 0)	
	
	win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)

def doNormalKey(key):
	keybd_event(key, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
	time.sleep(0.01)
	keybd_event(key,0, win32con.KEYEVENTF_KEYUP,0)
	
def doUpperCaseKey(key):
	win32api.keybd_event(win32con.VK_LSHIFT , 0, 0, 0)		
	
	keybd_event(key, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
	time.sleep(0.01)
	keybd_event(key,0, win32con.KEYEVENTF_KEYUP,0)	
		
	win32api.keybd_event(win32con.VK_LSHIFT , 0, win32con.KEYEVENTF_KEYUP, 0)
		
def processkey(key):
	if key == "/":
		doNormalKey(193)
		
	if key == "=":
		doNormalKey(187)
		
	if key == ".":
		doNormalKey(190)
		
	if key == " ":
		doNormalKey(ord(" "))
		
	if key == ':':
		doUpperCaseKey(191)
		
	if key == "?":
		doUpperCaseKey(193)
		
def dokey(key):
	krange = ord(key)
	
	isinrange = ((krange >= 65 and krange <= 90)or(krange >= 97 and krange <= 122))
	
	capslock_state = GetKeyState(win32con.VK_CAPITAL)
	
	if capslock_state == 0:
		can_up = key.isupper() and isinrange
	else:
		can_up = key.islower() and isinrange
	
	if can_up:
		win32api.keybd_event(win32con.VK_LSHIFT , 0, 0, 0)
	
	if isinrange:
		key = key.upper()	
		key = ord(key)
		
		doNormalKey(key)
		
	else:
		processkey(key)
		
	if can_up:
		win32api.keybd_event(win32con.VK_LSHIFT , 0, win32con.KEYEVENTF_KEYUP, 0)
		
	

def sendkeys(keys,send_return):
	for k in keys:
		dokey(k)
	#r.clipboard_clear()
	#time.sleep(1)
	#r.clipboard_append(keys)
	#send_paste()
	
	if send_return:
		win32api.keybd_event(win32con.VK_RETURN , 0, 0, 0)	
		win32api.keybd_event(win32con.VK_RETURN , 0, win32con.KEYEVENTF_KEYUP, 0)
#===============================================================

targetwindow = "mIRC"

#START AUTO-TYPING
def doTyping():
	the_text = open("text.txt").read().split("\n")
	
	text_index = 0
	text_max = len(the_text) - 1
	while True:
		if text_index > text_max:
			text_index = 0
		window = win32ui.GetForegroundWindow()
		windowtext = window.GetWindowText()
		
		if not windowtext.__contains__(targetwindow):
			exit(0)
			
		print the_text[text_index]
		window_searcher.send_line(the_text[text_index])
		
			
		text_index +=1
		
		time.sleep(0.7)
			
	
while True:
	time.sleep(0.5)
	window = win32ui.GetForegroundWindow()
	windowtext = window.GetWindowText()
	
	if windowtext.__contains__(targetwindow):
		doTyping()


