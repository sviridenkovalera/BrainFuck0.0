import sys
#l-value of program
cmd            = ''  #current command
code           = ''  #input program code
point          = 0   #point ceill of memory map
cmdIndex       = 0   #index of current command
ceillSize      = 256 #size single ceill
maxSizeMemMap  = 30000  
loopsMap       = [] 
memMap         = [ 0 for index in range ( maxSizeMemMap ) ] #memory map
commandMap     = ('+', '-', '<', '>', '[', ']', '.', ',') # all commad BF language 
#input program code
for byte in sys.stdin.read():
    if byte in commandMap:
        code += byte
for i in code:
    print (i)
sys.exit ()
#processing code 
while cmdIndex < len ( code ):
    cmd = code [cmdIndex]
    if cmd == '<':
        point -= 1
        if point < 0:
            point = maxSizeMemMap - 1
    elif cmd == '>':
        point += 1
        if point == maxSizeMemMap:
            point = 0
    elif cmd == '+':
        memMap [point] += 1
        memMap [point] %= ceillSize
    elif cmd == '-':
        memMap [point] -= 1
        if memMap [point] < 0:
            memMap [point] = ceillSize - 1
    elif cmd == '.':
        sys.stdout.write ( chr ( memMap [point] ) )
    elif cmd == ',':
        memMap [point] = ord ( sys.stdin.read (1) )
        memMap [point] %= ceillSize
    elif cmd == '[':
        loopsMap.append ( cmdIndex )
    elif cmd == ']':
        if memMap and memMap [point] == 0:
            loopsMap.pop ()
        else:
            cmdIndex = loopsMap [len ( loopsMap ) - 1] + 1
            continue
    cmdIndex += 1
print ('')       
     
        
