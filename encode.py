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
    usr = input("Any TEXT here: ")
    sep = "#"

if usr=="-h" or usr=="help" or usr=="--help":
        print("python3 encode.py \t will ask for Binary Data input, only single line allowed","\n")
        print("python3 encode.py <TEXT_DATA-filename> \t will print in STDOUT","\n")
        print("python3 encode.py <TEXT_DATA-filename> <OUT_FILENAME> \t will write in File","\n")
        print("python3 encode.py <TEXT_DATA-filename> <OUT_FILENAME> <CUSTOM_SEPERATOR>\t will write in File with custom seperators","\n")
        exit(0)

res = ""
usr = open(usr,"r").read()
try:
    res = sep.join(format(ord(i)+1,"08b") for i in usr)
except:
    print("There is Custom Seperator Needed, type 'python encode.py -h' for help ")
try:
    fil = open(filn,"w")
    fil.write(res)
    fil.close()
except:
    print(res)
    
