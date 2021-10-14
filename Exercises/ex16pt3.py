import sys

script, filename = sys.argv

doc = open(filename)

print("the file reads:",
	doc.read())