import math;
import sys;
from random import randint as ri

def createAnswerKey(numQuestions):
	letterChoices = ['O' * 62, 'A' * 67, 'B' * 15, 'AB' * 6];
	key = [];
	for x in range(0,numQuestions):
		key.append(letterChoices[ri(0, len(letterChoices)-1)]);
	return key

def letterPercentage(letter, key):
	total = len(key);
	num = 0;
	for x in key:
		if x == letter:
			num += 1;
	return (num / total) * 100;

# answers = createAnswerKey(40);
# print(answers);
# print("%s%%" % (letterPercentage("C", answers)));
# print("%s%%" % (letterPercentage("B", answers)));

cavg = 0;
bavg = 0;
numTest = 1000;

for x in range(0, numTest):
	answers = createAnswerKey(50);
	print(answers);
	cpercent = letterPercentage("A", answers);
	bpercent = letterPercentage("AB", answers);

	cavg += cpercent;
	bavg += bpercent;
	progressPercentage = (x / numTest) * 100;
	if progressPercentage % 1 == 0:
		print("#%s%%" % (progressPercentage));

print("Average A Percentage: %s%%" % (cavg/numTest));
print("Average AB Percentage: %s%%" % (bavg/numTest));
