import sys

script, filename = sys.argv

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN")

input("?")

print("Opening the file...")
target = open(filename, "w")

print("Truncating the file. Goodbye!")

print("Now I'm going to ask you for three lines.")

line_1 = input("line 1: ")
line_2 = input("line 2: ")
line_3 = input("line 3: ")

print("I'm going to write these to the file")

target.write(line_1 + "\n" + line_2 + "\n" + line_3 + "\n")

print("And finally, we close it")
target.close()