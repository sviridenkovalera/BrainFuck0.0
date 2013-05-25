import sys

str = ''
for line in sys.stdin:
    str += line.replace ( ' ', '')
cmdIndex = 0
cmd = ''
index = 0
memMap = []
memMap.append (0)
ceillSize = 256
loopsMap = []


while cmdIndex < len ( str ):
    cmd = str [cmdIndex]
    memMap [index] %= ceillSize
    if cmd == '<':
        index -= 1
        if index < 0:
            print ( 'Error index < 0')
            sys.exit ( - 1 )
    elif cmd == '>':
        index += 1
        if index == len ( memMap ):
            memMap.append ( 0 )
    elif cmd == '+':
        memMap [index] += 1
    elif cmd == '-':
        memMap [index] -= 1
    elif cmd == '.':
        sys.stdout.write ( chr ( memMap [index] ) )
    elif cmd == ',':
       memMap [index] = ord ( sys.stdin.read (1) )
    elif cmd == '[':
        loopsMap.append ( cmdIndex + 1 )
    elif cmd == ']':
        if memMap [index] == 0:
            loopsMap.pop ()
        else:
            cmdIndex = loopsMap [ len ( loopsMap ) - 1]
            continue
    cmdIndex += 1
print ('')       
     
        