#This is menuFile
import additionFile, subtractionFile, multiplicationFile, divisionFile, modulusFile



print("<-- Mathematical Program -->\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus")
inp = int(input("Enter your choice->"))
if(inp==1):
	print(additionFile.add())
elif(inp==2):
	print(subtractionFile.subt())
elif(inp==3):
	print(multiplicationFile.multi())
elif(inp==4):
	print(divisionFile.div())
else:
	print("Invalid choice")