daysPerYear = 365;

dpd = int(input("How much are you going to save per day? >>> "));
age = int(input("How old are you? >>> "));
end = int(input("When do you plan to retire? >>> "));

total = ((end - age) * daysPerYear) * dpd;

print("When you retire you will have $%s saved up." % (str(total)))