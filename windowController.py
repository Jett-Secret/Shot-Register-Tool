from pynput.mouse import Controller
import os
mouse = Controller()
class WinControl:
	def __init__(self):
		self.rows=[]
		self.header = "Week,Type,Map,Scorer Team, Against Team, Player,Assister (Duo), Goalie (Against),Striker,Level,Staggered,Set,Clock,Man Power,Type of Goal,Coreflip,Red Core,X,Y"
		self.resetActiveRow()
	def resetActiveRow(self):
		self.activeRow = {
			"team":0,
			"scorer":None,
			"assists":[],
			"mouse":(0,0),
				"flip":False
		}
	def updateF1KeyText1(self,e):
		self.keyStrings["team1"][0].set("<"+e.keysym+">")
		self.f1key1 = e.keycode
		y = e.y;
		x = e.x;
		#print(x,y)
		self.team1rows.append([self.nameStrings['team1'][0].get(),x,y])
		self.root.focus()
	def updateF2KeyText1(self,e):
		self.keyStrings["team1"][1].set("<"+e.keysym+">")
		self.f2key1 = e.keycode
		y = e.y;
		x = e.x;
		self.team1rows.append([self.nameStrings['team1'][1].get(),x,y])
		self.root.focus()
	def updateGKeyText1(self,e):
		self.keyStrings["team1"][2].set("<"+e.keysym+">")
		self.gkey1 = e.keycode
		y = e.y;
		x = e.x;
		self.team1rows.append([self.nameStrings['team1'][2].get(),x,y])
		self.root.focus()
		
	def updateF1KeyText2(self,e):
		self.keyStrings["team2"][1].set("<"+e.keysym+">")
		self.f1key2 = e.keycode
		y = e.y;
		x = e.x;
		self.team1rows.append([self.nameStrings['team2'][0].get(),x,y])
		self.root.focus()
	def updateF2KeyText2(self,e):
		self.keyStrings["team2"][1].set("<"+e.keysym+">")
		self.f2key2 = e.keycode
		y = e.y;
		x = e.x;
		self.team1rows.append([self.nameStrings['team2'][1].get(),x,y])
		self.root.focus()
	
	def updateGKeyText2(self,e):
		self.keyStrings["team2"][2].set("<"+e.keysym+">")
		self.gkey2 = e.keycode
		y = e.y;
		x = e.x;
		self.team1rows.append([self.nameStrings['team2'][2].get(),x,y])
		self.root.focus()
		
	def validateDir(self,fname):
		os.makedirs(fname[:fname.rindex('/')],exist_ok=True)
		
	def writeToFile(self,e):
		if len(self.rows)==0:
			print("Nothing to write!")
			return
		fname = self.filename.get();
		
		self.validateDir(fname)
		FIL = open(fname,'w+')
		FIL.write(self.header+"\n")
		for l in self.rows[:-1]:
			FIL.write(l+"\n")
		FIL.write(self.rows[-1])
		FIL.flush()
		FIL.close()
		
		self.rows=[]
		self.counter.set(0);
		
	
	def handle_key_press(self,code,enter=False,shift=False):
		'''
		try:
			get = e.widget.get()#, self.root.focus_get())
			return
		except:
			pass
	
		for s in self.characterStrings:
			break
			print(s)
			for x in self.characterStrings[s]:
				print(x.get());
		'''
		
		# check if the key matches one of the correct ones
		
		#code = e.keycode;
		'''ctrl  = (e.state & 0x4) != 0
		if code ==17:
			return
		if ctrl:
			#check z undo.
			return;
		'''
		#print(code,enter)
		if enter:
			self.AppendRow()
			return
		result = None
		team = 1
		player = -1
		BACKSPACE = 8
		
		if(code == self.f1key1):
			player=0
		elif (code == self.f2key1):
			player=1
		elif (code == self.gkey1):
			player=2
		elif(code == self.f1key2):
			team=2
			player=0
		elif (code == self.f2key2):
			team=2
			player=1
		elif (code == self.gkey2):
			team=2
			player=2
			
			
		#F1-F5
		if code<=116 and code >= 112:
			if code == 112:
				self.shotType.set("Strike")
			elif code == 113:
				self.shotType.set("Primary")
			elif code == 114:
				self.shotType.set("Secondary")
			elif code == 115:
				self.shotType.set("Special")
			else:
				self.shotType.set("Passive")
			return
			
		flip = shift
		#print(player)
		if player==-1 and code!=BACKSPACE: 
			print("could not register shot")
			return
			
		#get mouse position
		pos = mouse.position
		x= pos[0];
		y= pos[1];
		
		row = self.activeRow
		
		if 'team' not in row or row['team'] != team:
			row = {
				"team":team,
				"scorer":None,
				"assists":[],
				"mouse":(x,y),
				"flip":False
			}
		if code != BACKSPACE:
			if row is None:
				row = {
					"team":team,
					"scorer":player,
					"assists":[]
				}
			else:
				if 'scorer' in row and row['scorer'] is not None and row['scorer']!=-1:
					if len(row['assists'])>1:
						row['assists'][0]=row['assists'][1]
						row['assists'][1]=player
					else:
						row["assists"].append(player)
				else:
					if 'team' not in row or row['team'] != team:
						row['team']=team
					row['mouse']=(x,y)
					row['flip']=flip
					row['scorer']=player
		else:
			# if the key is backspace
			# and the assists list is not empty
			# remove an assist, else remove the scorer.
			if 'assists' in row and len(row['assists'])>0:
				row['assists']=row['assists'][0:-1]
			else:
				row['scorer'] = None
				row['mouse']=(0,0)
				row['flip']=flip
		
		self.activeRow = row
		self.SetActiveRowText()
	def SetActiveRowText(self):
		#print("setrow")
		row = self.activeRow
		#print(row)
		t = row['team']
		tstr = "team1"
		#print(t)
		if t==2:
			tstr = "team2"
		if row['scorer'] is None:
			player = "None"
		else:
			player = self.nameStrings[tstr][row['scorer']].get()
		assists = ""
		shotType = self.shotType.get()
		mapName = self.mapName.get();
		#print(self.nameStrings[tstr])
		if 'assists' in row:
			for a in row['assists']:
				#print(a,"::")
				assists+=","+str(self.nameStrings[tstr][a].get())
		
		setstring=str(row['mouse'])+" : flip?"+str(row['flip'])+" "+ (self.team1Name.get() if t==1 else self.team2Name.get())+ " ("+ shotType + "): " +player+assists+ " : "+mapName
		self.activeRowString.set(setstring)
		
		
	
	def AppendRow(self):
		
		row = self.activeRow
		if row['scorer'] is None:
			print("There isn't a scorer in this selection!")
			return;
		teamGeneric = "team1" if row['team']==1 else 'team2'
		otherTeamGeneric = "team1" if row['team']!=1 else 'team2'
		nassists = len(row['assists'])
		line = str(self.week.get())+","+("Solo" if nassists==0 else ("Duo" if nassists==1 else "Team"))+","+self.mapName.get()+","+(self.team1Name.get() if row['team']==1 else self.team2Name.get())+","+(self.team1Name.get() if row['team']!=1 else self.team2Name.get())+","
		line +=	self.nameStrings[teamGeneric][row['scorer']].get()+","+("n/a" if nassists>1 else ("n/a" if nassists==0 else self.nameStrings[teamGeneric][row['assists'][0]].get()))
		line += self.nameStrings[otherTeamGeneric][2].get()+","+self.characterStrings[otherTeamGeneric][2].get()+",0,False,"+self.goalType.get()+","+str(row['flip'])+",False,"
		line += str(row['mouse'][0]) + ","+ str(row['mouse'][1])
		
		self.rows.append(line)
		self.resetActiveRow()
		self.SetActiveRowText()
		self.counter.set(len(self.rows))