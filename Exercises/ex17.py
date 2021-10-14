import sys

import os.path

script, from_file, to_file = sys.argv

print("Copying from %s to %s" % (from_file, to_file))

#we could do these two on one line too, how?
indata = open(from_file).read()

print("The input file is %d bytes long" % len(indata))

print("Does the output file exist? %r" % os.path.exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, "w")
out_file.write(indata)

print("Alright, all done.")

from_file.close()
in_file.close()