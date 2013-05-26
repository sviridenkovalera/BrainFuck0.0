_DEBUG = False
_ADD_FUNCTION = False
_SHOW_FORMT_CODE = False
_SHOW_CLINE_CODE = True
import sys
def clineCode ( code ):
    print ( 'Cliner code:')
    print ( code )
    print ('')
def formatCode ( code ):
    shift = 0
    add_shift = 4
    for i in code:
        if i == '[':
            shift += add_shift
        for j in range ( shift ):
            sys.stdout.write ( '    ')
        if i == ']':
            shift -= add_shift
        if i not in ( '[', ']'):
            sys.stdout.write ( '    ')
        print ( str ( i ) )
    print ('')
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
if _ADD_FUNCTION:
    if _SHOW_FORMT_CODE:
        formatCode ( code )
    if _SHOW_CLINE_CODE:
        clineCode ( code )
    sys.exit (0)
steps_all = 0
#processing code 
while cmdIndex < len ( code ):
    if _DEBUG:
        print ( 'Step: ' + str ( steps_all) )
        print ( 'Current point: ' + str ( cmdIndex ) )
        print ( 'Command: ' + code [ cmdIndex ] )
        steps_all += 1
        print ('****************************')
        _cnt = 10
        _min = point - _cnt
        if _min < 0:
            _min = 0
        _max = point + _cnt
        if _max >= maxSizeMemMap:
            _max = maxSizeMemMap - 1
        for prtIndex in range ( _min, _max + 1 ):
            if prtIndex != point:
                print ( "#" + str ( prtIndex) + ' Value: ' + str ( memMap [prtIndex]) )
            else:
                print ( "[ #" + str ( prtIndex) + ' Value: ' + str ( memMap [prtIndex]) + str (' ]') )
        print ('*****************************')
        print ('')
        if code [cmdIndex] != ',':
            sys.stdin.read (1)
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
        if _DEBUG:
            print ('Print value:    ')
        sys.stdout.write ( chr ( memMap [point] ) )
    elif cmd == ',':
        if _DEBUG:
            print ('Input value:')
        memMap [point] = ord ( sys.stdin.read (1) )
        memMap [point] %= ceillSize
    elif cmd == '[':
        if memMap [point] == 0:
            cmdIndex += 1
            _cnt = 1
            while cmdIndex < len ( code ) and _cnt > 0:
                if code [cmdIndex] == '[':
                    _cnt += 1
                elif code [cmdIndex] == ']':
                    _cnt -= 1
                cmdIndex += 1
            continue
        else:
            loopsMap.append ( cmdIndex )
    elif cmd == ']':
            if memMap [point] == 0:
                loopsMap.pop ()
            else:
                cmdIndex = loopsMap [len ( loopsMap ) - 1] + 1
                continue
    cmdIndex += 1
print ('')       
     
        
