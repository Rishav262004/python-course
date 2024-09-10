str="This is the new file created automatically "

f=open("new_write_file.txt","w")   #this will create a new text file by the name "new_write_file.txt" automatically.
f.write(str)
f.close()