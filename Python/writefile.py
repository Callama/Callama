#Writing to Files
import time

write = True
while write == True:
    #fname = input("Please enter a File name to write to")
    with open("file.txt" , "a") as file:
        text = input("Please enter Text to print to the File")
        if text == "stop":
            file.close()
            write = False
            print("The File as been saved and Closed succesfully")
        else:
           file.write(text+"\n")
        if text == "clear":
            file.truncate()
            print("File has been succesfully cleared")

#with open ("text.txt" , "w") as file:
    #file.write("Hello World!\n")
    #file.write("Hello above!\n")
    #file.close()