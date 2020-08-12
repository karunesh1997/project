################# start another project################

indian=["samosa","daal","roti","rice"]
chinese=["noodels","egg role","fried rice"]
italian=["pizza","pasta","risotto"]

dish=input("Enter a dish name: ")
if dish in indian:
    print("indian")
elif dish in chinese:
    print("it is chinese")
elif dish in italian:
    print("italian")
else:
    print("i don't know the dish",dish)