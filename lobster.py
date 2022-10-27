import random

lifespan = 0;
winFactor = 0.5;
while lifespan < 13:
	confidence = random.random();
	print("con: %3.2f winf: %3.2f" % (confidence, winFactor));
	if confidence > winFactor:
		winFactor -= 0.1;
		print("Peter won his battle\n")
	elif confidence < winFactor:
		winFactor += 0.1;
		print("Peter lost his battle\n");

	if winFactor > 1:
		lifespan = 13;
		print("You are dead!!!!");
	elif winFactor < 0:
		lifespan = 13;
		print("You are a GOD!!!");
	lifespan += 1;
