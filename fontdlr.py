# -*- coding: utf-8 -*-
#FONTDLR
#Sends blown up ascii text to the user's clipboard.

from Tkinter import Tk
import time, sys

alph = {}
charCounter = 0

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


#Sends text to the clipboard
def cliptify(text): 
	r = Tk()
	r.withdraw()
	r.clipboard_clear()
	r.clipboard_append(text)
	r.destroy()

#Slowly write stuff to console (Windows only)
def slowPrint(text,delay=20):
	delay/=float(1000)
	for c in text:
		sys.stdout.write(c)
		time.sleep(delay)
	sys.stdout.write("\n")


#Creates a 3-row string of ascii text
def textMake(text,font): 
	output=''
	lines = ['','','']
	global charCounter
	for letter in text:
		n=0
		for bixel in font[letter]: #For each char in letter object
			if bixel == "\n":
				n+=1
				continue
			lines[n] += bixel
			charCounter+=1
	for line in lines:
		output+=line+"\n"
	return output


slowPrint("FONTDLR version 1.0\n\n\n")
userText =raw_input("Enter text: ").lower()
output = textMake(userText,alph)
cliptify(output)
slowPrint("\nCopied "+str(charCounter)+" characters to clipboard.")

time.sleep(1)
	