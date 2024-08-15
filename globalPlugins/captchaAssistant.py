import mouseHandler
import ui
import winUser
import wx
import globalPluginHandler
import scriptHandler
import addonHandler
import api
import sys
import os
import threading

# for purpose of import pyautogui
sys.path.append(os.path.dirname(__file__))
import pyautogui
sys.path.remove(os.path.dirname(__file__))

# addonHandler.initTranslation()
pyautogui.FAILSAFE=False

def reportMousePosition(x=None, y=None):
	# The coordinates are keywords so specific position can be announced if needed.
	cursorPos = winUser.getCursorPos()
	if x is None:
		x = cursorPos[0]
	if y is None:
		y = cursorPos[1]
	ui.message("{0}, {1}".format(x, y))

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self, *args, **kwargs):
		super(GlobalPlugin,self).__init__(*args, **kwargs)
		self.thread=None

	@scriptHandler.script(
		description="移动鼠标从屏幕左上角到右下角，耗时五秒",
		gesture="kb:nvda+shift+p"
	)
	def script_mouseFromTopLeftToBottomRight(self, gesture):
		(w,h)=api.getDesktopObject().location[2:]
		winUser.setCursorPos(0,0)
		if not self.thread or not self.thread.is_alive():
			self.thread=threading.Thread(target=pyautogui.moveTo,args=(w-1,h-1,5),kwargs={"tween":pyautogui.easeInQuad})
			self.thread.start()
		else:
			ui.message("鼠标尚未完成移动。")
