import math

denom = int(input("How many people are playing? >>> "));
num = int(input("What's your skin in the game? >>> "));
newNum = denom - num;

numtrys = (math.log(.5) / math.log((newNum / denom))) + 1;
print("You would have to play %d times have greater than 50%% chance of winning" % (numtrys));