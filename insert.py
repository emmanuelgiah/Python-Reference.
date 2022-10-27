from random import randint as ri
import math

numbas = list();

for x in range(0, 10):
	numbas.append(ri(0, 100));

def insertSort(arr):
	for x in range(0, len(arr)):
		for y in range(0, x):
			if (arr[y] > arr[x]):
				temp = arr[x];
				arr[x] = arr[y];
				arr[y] = temp;

	return arr;

def binSort(arr, num):
	firstIndex = 0;
	lastIndex = len(arr);
	mid = int((firstIndex + lastIndex) / 2);

	while ((lastIndex - firstIndex) > 0):
		if (arr[mid] == num):
			return mid
		elif (num > arr[mid]):
			firstIndex = mid;
			mid = int((firstIndex + lastIndex) / 2);
		elif (num < arr[mid]):
			lastIndex = mid;
			mid = int((firstIndex + lastIndex) / 2);
	return -1;


print("UnSorted: " + str(numbas));
print("Sorted: " + str(insertSort(numbas)));

toFind = numbas[ri(0, len(numbas)-1)]
print("Search For: " + str(toFind));
print("Index: " + str(binSort(numbas, toFind)));