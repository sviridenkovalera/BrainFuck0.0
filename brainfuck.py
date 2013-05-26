import sys
#l-value of program
cmd            = ''  #current command
code           = ''  #input program code
point          = 0   #point ceill of memory map
cmdIndex       = 0   #index of current command
ceillSize      = 256 #size single ceill
loopsMap       = []  #store cmdIndex + 1 - begin loop 
memMap         = [0] #memory map
commandMap     = ('+', '-', '<', '>', '[', ']', '.', ',') # all commad BF language 
#input program code
for byte in sys.stdin.read():
    if byte in commandMap:
        code += byte
#processing code 
while cmdIndex < len ( code ):
    cmd = code [cmdIndex]
    memMap [point] %= ceillSize
    if cmd == '<':
        point -= 1
        if point < 0:
            print ( 'Error index < 0' )
            sys.exit ( - 1 )
    elif cmd == '>':
        point += 1
        if point == len ( memMap ):
            memMap.append ( 0 )
    elif cmd == '+':
        memMap [point] += 1
    elif cmd == '-':
        memMap [point] -= 1
        if memMap [point] < 0:
            memMap [point] += ceillSize
    elif cmd == '.':
        sys.stdout.write ( chr ( memMap [point] ) )
    elif cmd == ',':
        memMap [point] = ord ( sys.stdin.read (1) )
    elif cmd == '[':
        loopsMap.append ( cmdIndex + 1 )
    elif cmd == ']':
        if memMap [point] == 0:
            loopsMap.pop ()
        else:
            cmdIndex = loopsMap [len ( loopsMap ) - 1]
            continue
    cmdIndex += 1
print ('')       
     
        
