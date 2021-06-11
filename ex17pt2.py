import sys

import os.path

script, from_file, to_file = sys.argv

indata = open(from_file).read()

open(to_file, "w").write(indata)
