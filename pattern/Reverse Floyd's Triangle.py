r, i, j, n = None, None, None, 1

# x - denotes the number of rows

 

print ("-----Kindly enter the number of rows to print Floyd's triangle number pattern-----")

r = int (input ())

 

print ("\n-----This is Floyd's triangle number pattern-----\n")

 

for i in range (r + 1, 1, -1):

	print (end="\t")	for j in range (i, 1, -1):

		print (n, end="\t")

		n = n + 1

	print (end="\n\n")

 
