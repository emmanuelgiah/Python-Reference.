from random import randint

def propagate(succeedingGenerations, minimumOffSpring):
	genePool = 1;
	for x in range(1, succeedingGenerations):
		offSet = randint(-1, 1);
		genePool *= (minimumOffSpring + offSet);
	return genePool;

succeedingGenerations = int(input("How many generations you want your gene pool to spread>>> "));
minimumOffSpring = int(input("How many kids you want each generation to have>>> "))
print("By the next %s generations you will %s Giahs floating around" % 
	(succeedingGenerations, propagate(succeedingGenerations, minimumOffSpring)));
