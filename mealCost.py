import math;

mealCost = float(raw_input());
tip = raw_input();
tax = raw_input();

tipPercent = mealCost * (float(tip) / 100.0);
taxPercent = mealCost * (float(tax) / 100.0);
totalCost = float(mealCost) + tipPercent + taxPercent;

print "The total meal cost is", int(round(totalCost)), "dollars.";
