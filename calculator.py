total = float(input("What is your bill sub-total? ").strip('$'))

tip_15 = total * 0.15
tip_18 = total * 0.18
tip_20 = total * 0.20

print("Tip Suggestions:")
print("----------------")
print("15 is $%.2f" % (tip_15))
print("18 is $%.2f" % (tip_18))
print("20 is $%.2f" % (tip_20))