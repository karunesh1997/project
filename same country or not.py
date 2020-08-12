usa=["atlanta","new york","chicago","baltimore"]
uk=["london","bristol","cambridge"]
india=["mumbai","delhi","banglore"]

city1=input("city1: ")
city2 = input("city2: ")

if city1 in usa and city2 in usa:
    print("Both cities are in usa")
elif city1 in uk and city2 in uk:
    print("Both cities are in uk")
elif city1 in india and city2 in india:
    print("Both cities are in india")
else:
    print("They don't belong to the same country ")
