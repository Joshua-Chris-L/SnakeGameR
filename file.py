with open("my_file.txt", mode="r") as file:
    contents = file.read()
    
print(contents)

"""
with open("my_file.txt", mode="w") as file:
    file.write("\nNew text.")
 """