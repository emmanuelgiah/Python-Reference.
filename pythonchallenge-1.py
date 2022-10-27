phrase = str(input("Enter a string>>> "));
newPhrase = "";
for x in range(0, len(phrase)):
	letter = phrase[x:x+1];
	if (letter != " "):
		newPhrase += chr(ord(letter) + 2);

print(phrase);
print(newPhrase);