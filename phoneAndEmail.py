# phoneAndEmail.py - finds phone numbers and email addresses in the clipboard
import pyperclip, re


#Creating phone number regex
phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?   #Area code
	(\s|-|\.)			 #Separator
	(\d{3})				 #First 3 digits
	(\s|-|\.)			 #Separator
	(\d{4})				 #Second four digits
	(\s*(ext|x|ext.)\s*(\d{2,5}))?
	)''', re.VERBOSE)

#Creating Email regex
emailRegex = re.compile(r'''(
	[a-zA-Z0-9_%+-.]+	#Username
	@					#@ symbol
	[a-zA-Z0-9.-]+		#domain name
	(\.[a-zA-z0-9]{2,5})#dot-something
	)''', re.VERBOSE)


text = str(pyperclip.paste().encode("utf-8"))


matches = []
for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1],groups[3],groups[5]])
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)

for groups in emailRegex.findall(text):
	matches.append(groups[0])
		
if len(matches) > 0: 
	pyperclip.copy('n'.join(matches))
	print 'Copied to clipboard: '
	print '\n'.join(matches)
	