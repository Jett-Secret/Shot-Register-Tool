from pynput.keyboard import Key, KeyCode,Listener
from pynput.mouse import Button,Listener as mListener
from settingsLoader import loadSettings
import sys,datetime,time
import threading
from tkinter import *
from tkinter import Button as Btn
from pynput.mouse import Controller
from pynput.keyboard import Key,Listener
from pynput import keyboard
mouse = Controller()
import re,windowController,json
WIN_SIZE = (0,0)
#for win in aux.getWindowSizes():
#	if re.match(re.compile("^OmegaStrikers"),win[0]):
#		WIN_SIZE = win[2];
#		break
#if(WIN_SIZE==(0,0)):
#	WIN_SIZE=(1920,1080)
global movable
movable=False
KILL = False
def on_release(e):
	pass
def closeWindows():
	
	global settingsWindowController
	global KILL
	KILL = True
	settingsWindowController.stop = True
	time.sleep(1)
	settingsWindowController.root.destroy()
	settingsWindowController.root = None
	quit()
def drill():
	pass
def writeShots(e):
	pass
	
def readCharactersFromFile():
	f = open("./data/lists.json")
	contents = f.read();
	
	data = json.loads(contents)
	if "strikers" not in data:
		return -1
	
	return data['strikers']
	
	
def readMapsFromFile():
	f = open("./data/lists.json")
	contents = f.read();
	
	data = json.loads(contents)
	if "maps" not in data:
		return -1
	
	return data['maps']
	
def updateMouse():
	global settingsWindowController
	while True:
		global KILL
		if KILL:
			break
		pos = mouse.position
		settingsWindowController.mouseX.set(pos[0])
		settingsWindowController.mouseY.set(pos[1])
		time.sleep(.1)
		
def keylog(key):
	prelogR(key)
	global shift
	#print(shift)
	global settingsWindowController
	focus = settingsWindowController.root.focus_get()
	if focus is not None and focus is not settingsWindowController.root:
		if key == keyboard.Key.enter:
			settingsWindowController.root.focus()
		return
	
	
	#print(key)
	#keymap = {'1':,'2':,'3':,'q':,'w':,'e':}
	if key == keyboard.Key.backspace:
		settingsWindowController.handle_key_press(8)
		return
	elif key == keyboard.Key.f1:
		settingsWindowController.handle_key_press(112)
		settingsWindowController.SetActiveRowText()
		return
	elif key == keyboard.Key.f2:
		settingsWindowController.handle_key_press(113)
		settingsWindowController.SetActiveRowText()
		return
	elif key == keyboard.Key.f3:
		settingsWindowController.handle_key_press(114)
		settingsWindowController.SetActiveRowText()
		return
	elif key == keyboard.Key.f4:
		settingsWindowController.handle_key_press(115)
		settingsWindowController.SetActiveRowText()
		return
	elif key == keyboard.Key.f5:
		settingsWindowController.handle_key_press(116)
		settingsWindowController.SetActiveRowText()
		return
	elif key == keyboard.Key.enter:
		settingsWindowController.handle_key_press(0,enter=True)
		return
	
		
	try:
		keyToCall = key.vk
		settingsWindowController.handle_key_press(keyToCall,shift=shift)
	except:
		pass
def prelog(key):
	global shift
	if key == Key.shift:
		shift=True
def prelogR(key):
	global shift
	if key == Key.shift:
		shift=False
def inputKeyLog():
	global settingsWindowController
	with Listener(on_press = prelog,on_release = keylog ) as l:
		l.join()
	while True:
		global KILL
		if KILL:
			break
			
global shift
shift=False	
global settingsWindowController
settingsWindowController = windowController.WinControl()

def run():
	global settingsWindowController
	settingsWindowController.stop = False
	#if(not aux.is_omega_strikers_window_open()):
	#	print("Omega Strikers isn't running :(")
		#return
	#procs = aux.getProcessess()
	#for p in procs:
	#	if b"\\OmegaStrikers-Win64-Shipping.exe" in p:
	#		print(p);
	paddingy=8
	paddingx=6
	settings = Tk()
	BG_COLOR = "#dadada"
	settings.configure(bg=BG_COLOR)
	characters = readCharactersFromFile()
	
	if(characters == -1):
		print("Could not read from file strikers.json")
		return
	maps = readMapsFromFile()
	#print(maps)
	
	if(maps == -1):
		print("Could not read from file strikers.json")
		return
		
	mapName = StringVar(settings,"Ahten City")
	settingsWindowController.mapName = mapName;
	
	settingsWindowController.mouseX = IntVar(settings,0)
	settingsWindowController.mouseY = IntVar(settings,0)
	settingsWindowController.week = IntVar(settings,1)
	
	#settings.bind('<KeyPress>', settingsWindowController.handle_key_press)
	
	shotType = StringVar(settings,"Strike")
	settingsWindowController.shotType = shotType
	f1nameText1 = StringVar(settings,"T1F1")
	f2nameText1 = StringVar(settings,"T1F2")
	gnameText1 = StringVar(settings,"T1G")
	f1nameText2 = StringVar(settings,"T2F1")
	f2nameText2 = StringVar(settings,"T2F2")
	gnameText2 = StringVar(settings,"T2G")
	settingsWindowController.nameStrings={"team1":[f1nameText1,f2nameText1,gnameText1],"team2":[f1nameText2,f2nameText2,gnameText2]}
	
	f1charText1 = StringVar(settings,"AiMi")
	f2charText1 = StringVar(settings,"AiMi")
	gcharText1 = StringVar(settings,"AiMi")
	f1charText2 = StringVar(settings,"AiMi")
	f2charText2 = StringVar(settings,"AiMi")
	gcharText2 = StringVar(settings,"AiMi")
	settingsWindowController.characterStrings={"team1":[f1charText1,f2charText1,gcharText1],"team2":[f1charText2,f2charText2,gcharText2]}
	
	f1keyText1 = StringVar(settings,"<1>")
	f2keyText1 = StringVar(settings,"<2>")
	gkeyText1 = StringVar(settings,"<3>")
	f1keyText2 = StringVar(settings,"<q>")
	f2keyText2 = StringVar(settings,"<w>")
	gkeyText2 = StringVar(settings,"<e>")
	filename = StringVar(settings,"./out/game.csv")
	
	settingsWindowController.f1key1 = 49;
	settingsWindowController.f2key1 = 50
	settingsWindowController.gkey1 = 51;
	settingsWindowController.f1key2 = 81;
	settingsWindowController.f2key2 = 87
	settingsWindowController.gkey2 = 69;
	setNumber = IntVar(settings,1)
	goalType = StringVar(settings,"Strike")
	assisters = IntVar(settings,0)
	
	
	settingsWindowController.filename = filename
	settingsWindowController.setNumber = setNumber
	settingsWindowController.goalType = goalType
	settingsWindowController.assisters = assisters
	settingsWindowController.team1Name = StringVar(settings,"Team 1")
	settingsWindowController.team2Name = StringVar(settings,"Team 2")
	
	
	settingsWindowController.keyStrings={"team1":[f1keyText1,f2keyText1,gkeyText1],"team2":[f1keyText2,f2keyText2,gkeyText2]}
	
	metaFrame = Frame(settings)
	metaFrame.grid(row=0,column=0)
	metaFrame.configure(bg=BG_COLOR)
	setLabel = Label(metaFrame,text="Set:",bg=BG_COLOR)
	setLabel.grid(row=0,column=0)
	setOptions = [1,2,3,4,5]
	setEntry = OptionMenu(metaFrame,setNumber,*setOptions)
	setEntry.grid(column=1,row=0)
	mapLabel = Label(metaFrame,text="Map:",bg=BG_COLOR)
	mapLabel.grid(row=0,column=2)
	mapEntry = OptionMenu(metaFrame,mapName,*maps)
	mapEntry.grid(column=3,row=0)
	shotTypeLabel = Label(metaFrame,text="Shot Type:",bg=BG_COLOR)
	shotTypeLabel.grid(row=0,column=4)
	shotTypeLabelVal = Label(metaFrame,textvariable=shotType,bg=BG_COLOR,width=9)
	shotTypeLabelVal.grid(row=0,column=5)
	
	weekLabel = Label(metaFrame,text="Week:",bg=BG_COLOR)
	weekLabel.grid(row=0,column=6)
	
	weekLabelVal = Entry(metaFrame,textvariable=settingsWindowController.week,width=3)
	weekLabelVal.grid(row=0,column=7)
	
	xmouseLabel = Label(metaFrame,text="X:",bg=BG_COLOR)
	xmouseLabel.grid(row=0,column=8)
	xmouseLabelVal = Label(metaFrame,textvariable=settingsWindowController.mouseX,bg=BG_COLOR,width=5)
	xmouseLabelVal.grid(row=0,column=9)
	ymouseLabel = Label(metaFrame,text="Y:",bg=BG_COLOR)
	ymouseLabel.grid(row=0,column=10)
	ymouseLabelVal = Label(metaFrame, textvariable=settingsWindowController.mouseY,bg=BG_COLOR,width=5)
	ymouseLabelVal.grid(row=0,column=11)
	
	
	editPanel = Frame(settings, width=300, height=400,relief=RAISED,background=BG_COLOR)
	editPanel.grid(row=1, column=0, padx=paddingx, pady=paddingy)
	
	#TEAM1 entries
	team1 = Label(editPanel,text="Team 1:",bg=BG_COLOR)
	team1.grid(column=0,row=0,padx=paddingx,pady=paddingy)
	
	teamEntry1 = Entry(editPanel,textvariable=settingsWindowController.team1Name)
	teamEntry1.grid(column=1,row=0,padx=paddingx,pady=paddingy)
	
	f11 = Label(editPanel,text="Forward 1:",bg=BG_COLOR)
	f11.grid(column=0,row=1,padx=paddingx,pady=paddingy)
	fEntry11 = Entry(editPanel,textvariable=f1nameText1)
	fEntry11.grid(column=1,row=1,padx=paddingx,pady=paddingy)
	
	keyf11 = Label(editPanel,text="Key Bind:",bg=BG_COLOR)
	keyf11.grid(column=2,row=1,padx=paddingx,pady=paddingy)
	keyEntryf11 = Entry(editPanel, textvariable=f1keyText1,width=5)
	keyEntryf11.grid(column=3,row=1,padx=paddingx,pady=paddingy)
	keyEntryf11.bind('<KeyRelease>', settingsWindowController.updateF1KeyText1)
	
	fChar11 = OptionMenu(editPanel, f1charText1 ,*characters)
	fChar11.grid(column=4,row=1,padx=paddingx,pady=paddingy)
	
	
	f21 = Label(editPanel,text="Forward 2:",bg=BG_COLOR)
	f21.grid(column=0,row=2,padx=paddingx,pady=paddingy)
	fEntry21 = Entry(editPanel,textvariable=f2nameText1)
	fEntry21.grid(column=1,row=2,padx=paddingx,pady=paddingy)
	
	keyf21 = Label(editPanel,text="Key Bind:",bg=BG_COLOR)
	keyf21.grid(column=2,row=2,padx=paddingx,pady=paddingy)
	keyEntryf21 = Entry(editPanel, textvariable=f2keyText1,width=5)
	keyEntryf21.grid(column=3,row=2,padx=paddingx,pady=paddingy)
	keyEntryf21.bind('<KeyRelease>', settingsWindowController.updateF2KeyText1)
	fChar21 = OptionMenu(editPanel, f2charText1 ,*characters)
	fChar21.grid(column=4,row=2,padx=paddingx,pady=paddingy)
	
	g1 = Label(editPanel,text="Goalie:",bg=BG_COLOR)
	g1.grid(column=0,row=3,padx=paddingx,pady=paddingy)
	gEntry1 = Entry(editPanel,textvariable=gnameText1)
	gEntry1.grid(column=1,row=3,padx=paddingx,pady=paddingy)
	
	keyg1 = Label(editPanel,text="Key Bind:",bg=BG_COLOR)
	keyg1.grid(column=2,row=3,padx=paddingx,pady=paddingy)
	keyEntryg1 = Entry(editPanel, textvariable=gkeyText1,width=5)
	keyEntryg1.grid(column=3,row=3,padx=paddingx,pady=paddingy)
	keyEntryg1.bind('<KeyRelease>', settingsWindowController.updateGKeyText1)
	gChar1 = OptionMenu(editPanel, gcharText1 ,*characters)
	gChar1.grid(column=4,row=3,padx=paddingx,pady=paddingy)
	
	
	#TEAM2 entries
	team2 = Label(editPanel,text="Team 2:",bg=BG_COLOR)
	team2.grid(column=0,row=4,padx=paddingx,pady=paddingy)
	teamEntry2 = Entry(editPanel,textvariable=settingsWindowController.team2Name)
	teamEntry2.grid(column=1,row=4,padx=paddingx,pady=paddingy)
	
	f12 = Label(editPanel,text="Forward 1:",bg=BG_COLOR)
	f12.grid(column=0,row=6,padx=paddingx,pady=paddingy)
	fEntry12 = Entry(editPanel,textvariable=f1nameText2)
	fEntry12.grid(column=1,row=6,padx=paddingx,pady=paddingy)
	
	keyf12 = Label(editPanel,text="Key Bind:",bg=BG_COLOR)
	keyf12.grid(column=2,row=6,padx=paddingx,pady=paddingy)
	keyEntryf12 = Entry(editPanel, textvariable=f1keyText2,width=5)
	keyEntryf12.grid(column=3,row=6,padx=paddingx,pady=paddingy)
	keyEntryf12.bind('<KeyRelease>', settingsWindowController.updateF1KeyText2)
	fChar12 = OptionMenu(editPanel, f1charText2 ,*characters)
	fChar12.grid(column=4,row=6,padx=paddingx,pady=paddingy)
	
	f22 = Label(editPanel,text="Forward 2:",bg=BG_COLOR)
	f22.grid(column=0,row=7,padx=paddingx,pady=paddingy)
	fEntry22 = Entry(editPanel,textvariable=f2nameText2)
	fEntry22.grid(column=1,row=7,padx=paddingx,pady=paddingy)
	
	keyf22 = Label(editPanel,text="Key Bind:",bg=BG_COLOR)
	keyf22.grid(column=2,row=7,padx=paddingx,pady=paddingy)
	keyEntryf22 = Entry(editPanel, textvariable=f2keyText2,width=5)
	keyEntryf22.grid(column=3,row=7,padx=paddingx,pady=paddingy)
	keyEntryf22.bind('<KeyRelease>', settingsWindowController.updateF2KeyText2)
	fChar22 = OptionMenu(editPanel, f2charText2 ,*characters)
	fChar22.grid(column=4,row=7,padx=paddingx,pady=paddingy)
	
	g2 = Label(editPanel,text="Goalie:",bg=BG_COLOR)
	g2.grid(column=0,row=8,padx=paddingx,pady=paddingy)
	gEntry2 = Entry(editPanel,textvariable=gnameText2)
	gEntry2.grid(column=1,row=8,padx=paddingx,pady=paddingy)
	
	keyg2 = Label(editPanel,text="Key Bind:",bg=BG_COLOR)
	keyg2.grid(column=2,row=8,padx=paddingx,pady=paddingy)
	keyEntryg2 = Entry(editPanel, textvariable=gkeyText2,width=5)
	keyEntryg2.grid(column=3,row=8,padx=paddingx,pady=paddingy)
	keyEntryg2.bind('<KeyRelease>', settingsWindowController.updateGKeyText2)
	gChar2 = OptionMenu(editPanel, gcharText2 ,*characters)
	gChar2.grid(column=4,row=8,padx=paddingx,pady=paddingy)
	
	
	settingsWindowController.editPanel = editPanel
	
	#current_value = tk.DoubleVar()
	#closeAll = Btn(settings,text="close", bg='#dadada',font=("Courier", 10))
	#closeAll.grid(column=0, row=0,padx=paddingx,pady=paddingy)
	#closeAll.bind("<Button-1>",closeWindows)
	writeFrame = Frame(settings)
	
	rowLabel = Label(writeFrame,text="Current Row:",bg=BG_COLOR)
	rowLabel.grid(column=0,row=0,padx=paddingx,pady=paddingy)
	settingsWindowController.activeRowString = StringVar(settings,"")
	rowLabel = Label(writeFrame,textvariable=settingsWindowController.activeRowString,bg=BG_COLOR)
	rowLabel.grid(column=1,row=0,padx=paddingx,pady=paddingy)
	
	countlabel = Label(writeFrame,text = "Shot Count:")
	countlabel.grid(row=1,column=0)
	settingsWindowController.counter = IntVar(settings,0)
	countlabelVar = Label(writeFrame,textvariable= settingsWindowController.counter)
	countlabelVar.grid(row=1,column=1)
	
	writeFrame.grid(column=0,row=2)
	writeButton = Btn(writeFrame,text="Write Shots to File", bg='#dadada',font=("Courier", 10))
	writeButton.grid(column=1, row=2,padx=paddingx,pady=paddingy)
	writeButton.bind("<Button-1>",settingsWindowController.writeToFile)
	writeFilename = Entry(writeFrame,textvariable=filename)
	writeFilename.grid(column=0,row=2,padx=paddingx,pady=paddingy)
	
	
	settingsWindowController.editmode = False
	settingsWindowController.root = settings
	x = threading.Thread(target=updateMouse,daemon=True)
	x.start()
	x = threading.Thread(target=inputKeyLog,daemon=True)
	x.start()
	

	# set the position options in settings 
	# and have those update within the main (view) window
	
	settings.protocol("WM_DELETE_WINDOW", closeWindows)
	settings.mainloop()
	#print("here")
		
	quit()
run()
