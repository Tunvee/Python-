file = open("sample.txt","a")
file.write("\n Tunvee Sharma's document")
file.close()
file2 = open("sample.txt","r")
print file2.read()
