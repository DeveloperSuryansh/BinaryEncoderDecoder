from sys import argv,exit
argc = len(argv)

if argc==2:
    usr = argv[1]
    sep = "#"
elif argc==3:
    usr = argv[1]
    filn = argv[2]
    sep = "#"
elif argc==4:
    usr = argv[1]
    filn = argv[2]
    sep = argv[3]
else:
    usr = input("Any binary here: ")
    sep = "#"

if usr=="-h" or usr=="help" or usr=="--help":
        print("python3 decode.py \t will ask for Binary Data input, only single line allowed","\n")
        print("python3 decode.py <BINARY-DATA_Filename> \t will print in STDOUT","\n")
        print("python3 decode.py <BINARY-DATA_Filename> <OUT_FILENAME> \t will write in File","\n")
        print("python3 decode.py <BINARY-DATA_Filename> <OUT_FILENAME> <CUSTOM_SEPERATOR>\t will write in File with custom seperators","\n")
        exit(0)

res = ""
usr = open(usr,"r").read()
try:
  for i in usr.split(sep):
    res += chr(int(i,2)-1)
except:
    print("There is Custom Seperator Needed, type 'python encode.py -h' for help ")

try:
    fil = open(filn,"w")
    fil.write(res)
    fil.close()
except:
    print(res)
