# -*- coding: utf-8 -*-
#ASCII STEAMER
#Sends ascii blown up ascii text to the user's clipboard.

from Tkinter import Tk
import time


alph = {}

alph['a'] = '''░█▀█
░█▀█
░▀░▀'''

alph['b']='''░█▀█░
░█▀▀█
░▀▀▀▀'''

alph['c']='''░█▀▀
░█░░
░▀▀▀'''

alph['d']='''░█▀▄
░█░█
░▀▀░'''

alph['e']='''░█▀▀
░█▀▀
░▀▀▀'''

alph['f']='''░█▀▀
░█▀░
░▀░░'''

alph['g']='''░█▀▀
░█░█
░▀▀▀'''

alph['h']='''░█░█
░█▀█
░▀░▀'''

alph['i']='''░█
░█
░▀'''

alph['j']='''░░▀█▀
░▄░█░
░▀▀▀░'''

alph['k']='''░█░▄▀
░█▀▄░
░▀░░▀'''

alph['l']='''░█░░
░█░░
░▀▀▀'''

alph['m']='''░█▄░▄█
░█░▀░█
░▀░░░▀'''

alph['n']='''░█▄░█
░█░▀█
░▀░░▀'''

alph['o']='''░█▀█
░█░█
░▀▀▀'''

alph['p']='''░█▀█
░█▀▀
░▀░░'''

alph['q']='''░█▀█░
░█░█░
░▀▀▀▄'''

alph['r']='''░█▀█
░█▀▄
░▀░▀'''

alph['s']='''░█▀▀
░▀▀█
░▀▀▀'''

alph['t']='''░▀█▀
░░█░
░░▀░'''

alph['u']='''░█░█
░█░█
░▀▀▀'''

alph['w']='''░█░░░█
░█░█░█
░▀▀░▀▀'''

alph['x']='''░▀▄░▄▀
░░▄▀▄░
░▀░░░▀'''

alph['y']='''░█░█
░▀█▀
░░▀░'''

alph['v']='''░█░█
░█░█
░░▀░'''

alph['z']='''░▀▀█░ 
░▄▀░░
░▀▀▀░'''

alph[' ']='''░░
░░
░░'''

alph['[']='''█▀░
█░░
▀▀░'''

alph[']']='''░▀█
░░█
░▀▀'''

def cliptify(text): #Sends text to the clipboard
	r = Tk()
	r.withdraw()
	r.clipboard_clear()
	r.clipboard_append(text)
	r.destroy()

def textMake(text): #Creates a 3 line string of ascii text
	output=''
	lines = ['','','']
	for letter in text:
		n=0
		for bixel in alph[letter]:
			if bixel == "\n":
				n+=1
				continue
			lines[n] += bixel
	for line in lines:
		output+=line+"\n"
	return output


userText =raw_input("Enter text: ")
userText = userText.lower()
text = textMake(userText)
cliptify(text)