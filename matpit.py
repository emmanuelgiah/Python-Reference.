import webbrowser
import sys
# import pyperclip

if len(sys.argv) > 1:
	#get address from command line.
	address = ' '.join(sys.argv[1:]);
else:
	#Get Address from clipboard.
	# address = pyperclip.paste();

print(address);
webbrowser.open('https://www.google.com/maps/place/' + address);
