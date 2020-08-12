usa=["atlanta","new york","chicago","baltimore"]
uk=["london","bristol","cambridge"]
india=["mumbai","delhi","banglore"]

city=input("Enter a city name: ")
if city in usa:
    print("usa")
elif city in uk:
    print("uk")
elif city in india:
    print(india)
else:
    print("Enter a valid city: ")