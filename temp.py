import math

def farToCel():
	f = float(input("Enter your temperature >>> "));
	c = ((5*f) - 160) / 9;
	print("%f --> %f" % (f, c));

def celToFar():
	c = float(input("Enter your temperature >>> "));
	f = ((9*c) + 160) / 5;
	print("%f --> %f" % (c, f));

def main():
	choice = input("What are you converting? (Cel / Far) >>> ");
	if choice[:1].lower() == "c":
		celToFar();
	elif choice[:1].lower() == "f":
		farToCel();

if __name__ == "__main__":
	main();