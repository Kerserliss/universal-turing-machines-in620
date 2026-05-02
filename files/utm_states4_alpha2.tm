//-------CONFIGURATION
name: utm_states4_alpha2
init: start
accept: end

//-------INIT

// at start, simply skip and remove the first 1
start,1,_,_
gotoend,_,_,_,>,-,-

// then we should go the end of input
gotoend,0,_,_
gotoend,0,_,_,>,-,-

gotoend,1,_,_
gotoend,1,_,_,>,-,-

gotoend,#,_,_
gotoend,#,_,_,>,-,-

gotoend,_,_,_
copyXto3,_,_,_,<,-,-

// we copy the x to 3rd tape, right to left so it is easier
// we could do a bit of error detection by using 2 states (since alpha is 2 bits wide), but this is not done here
copyXto3,0,_,_
copyXto3,_,_,0,<,-,<

copyXto3,1,_,_
copyXto3,_,_,1,<,-,<

copyXto3,#,_,_
writeInitState1,_,0,_,-,>,-

writeInitState1,_,_,_
writeInitState2,_,0,_,-,>,-

writeInitState2,_,_,_
writeInitState3,_,0,_,-,>,-

writeInitState3,_,_,_
writeInitSymbol1,_,0,_,-,>,>

writeInitSymbol1,_,_,0
writeInitSymbol2,_,0,0,-,>,>

writeInitSymbol1,_,_,1
writeInitSymbol2,_,1,1,-,>,>

writeInitSymbol2,_,_,0
reset,_,0,0,-,-,-

writeInitSymbol2,_,_,1
reset,_,1,1,-,-,-

//-------RUN

// RESET tapes 1 and 2 to start
// starts with 0
reset,0,0,0
reset,0,0,0,<,<,-

reset,0,0,1
reset,0,0,1,<,<,-

reset,0,1,0
reset,0,1,0,<,<,-

reset,0,1,1
reset,0,1,1,<,<,-

reset,0,_,0
reset,0,_,0,<,-,-

reset,0,0,_
reset,0,0,_,<,<,-

reset,0,_,1
reset,0,_,1,<,-,-

reset,0,1,_
reset,0,1,_,<,<,-

// starts with 1
reset,1,0,0
reset,1,0,0,<,<,-

reset,1,0,1
reset,1,0,1,<,<,-

reset,1,1,0
reset,1,1,0,<,<,-

reset,1,1,1
reset,1,1,1,<,<,-

reset,1,_,0
reset,1,_,0,<,-,-

reset,1,0,_
reset,1,0,_,<,<,-

reset,1,_,1
reset,1,_,1,<,-,-

reset,1,1,_
reset,1,1,_,<,<,-

// starts with _
reset,_,0,0
reset,_,0,0,<,<,-

reset,_,0,1
reset,_,0,1,<,<,-

reset,_,1,0
reset,_,1,0,<,<,-

reset,_,1,1
reset,_,1,1,<,<,-

reset,_,0,_
reset,_,0,_,<,<,-

reset,_,1,_
reset,_,1,_,<,<,-

// end conditions
reset,_,_,0
ismatching,_,_,0,-,-,-

reset,_,_,1
ismatching,_,_,1,-,-,-

reset,_,_,_
ismatching,_,_,_,-,-,-

// ISMATCHING checks if current transition in code matches current state

// LOOP
ismatching,1,1,0
ismatching,1,1,0,>,>,-

ismatching,1,1,1
ismatching,1,1,1,>,>,-

ismatching,1,1,_
ismatching,1,1,_,>,>,-

ismatching,0,0,0
ismatching,0,0,0,>,>,-

ismatching,0,0,1
ismatching,0,0,1,>,>,-

ismatching,0,0,_
ismatching,0,0,_,>,>,-

// FOUND
ismatching,1,_,0
gotocurrstart,1,_,0,-,<,-

ismatching,1,_,1
gotocurrstart,1,_,1,-,<,-

ismatching,1,_,_
gotocurrstart,1,_,_,-,<,-

ismatching,0,_,0
gotocurrstart,0,_,0,-,<,-

ismatching,0,_,1
gotocurrstart,0,_,1,-,<,-

ismatching,0,_,_
gotocurrstart,0,_,_,-,<,-

// NOT MATCHING

ismatching,1,0,0
findnext,1,0,0,>,>,-

ismatching,1,0,1
findnext,1,0,1,>,>,-

ismatching,1,0,_
findnext,1,0,_,>,>,-

ismatching,0,1,0
findnext,0,1,0,>,>,-

ismatching,0,1,1
findnext,0,1,1,>,>,-

ismatching,0,1,_
findnext,0,1,_,>,>,-

// WRITENEXT
// GOTO CURR START
gotocurrstart,0,0,0
gotocurrstart,0,0,0,-,<,-

gotocurrstart,0,0,1
gotocurrstart,0,0,1,-,<,-

gotocurrstart,0,0,_
gotocurrstart,0,0,_,-,<,-

gotocurrstart,1,0,0
gotocurrstart,1,0,0,-,<,-

gotocurrstart,1,0,1
gotocurrstart,1,0,1,-,<,-

gotocurrstart,1,0,_
gotocurrstart,1,0,_,-,<,-

// end conditions of gotocurrstart
gotocurrstart,0,_,0
writecurrstate,0,_,0,-,>,-

gotocurrstart,0,_,1
writecurrstate,0,_,1,-,>,-

gotocurrstart,0,_,_
writecurrstate,0,_,_,-,>,-

gotocurrstart,1,_,0
writecurrstate,1,_,0,-,>,-

gotocurrstart,1,_,1
writecurrstate,1,_,1,-,>,-

gotocurrstart,1,_,_
writecurrstate,1,_,_,-,>,-

// WRITE TO CURR

writecurrstate,0,0,0
writecurrstate,0,0,0,>,>,-

writecurrstate,0,0,1
writecurrstate,0,0,1,>,>,-

writecurrstate,0,0,_
writecurrstate,0,0,_,>,>,-

writecurrstate,0,1,0
writecurrstate,0,1,0,>,>,-

writecurrstate,0,1,1
writecurrstate,0,1,1,>,>,-

writecurrstate,0,1,_
writecurrstate,0,1,_,>,>,-

writecurrstate,1,0,0
writecurrstate,1,0,0,>,>,-

writecurrstate,1,0,1
writecurrstate,1,0,1,>,>,-

writecurrstate,1,0,_
writecurrstate,1,0,_,>,>,-

writecurrstate,1,1,0
writecurrstate,1,1,0,>,>,-

writecurrstate,1,1,1
writecurrstate,1,1,1,>,>,-

writecurrstate,1,1,_
writecurrstate,1,1,_,>,>,-

writecurrstate,0,_,0
writesymbol1,0,_,0,-,<,-

writecurrstate,0,_,1
writesymbol1,0,_,1,-,<,-

writecurrstate,0,_,_
writesymbol1,0,_,_,-,<,-

writecurrstate,1,_,0
writesymbol1,1,_,0,-,<,-

writecurrstate,1,_,1
writesymbol1,1,_,1,-,<,-

writecurrstate,1,_,_
writesymbol1,1,_,_,-,<,-


// WRITE SYMBOL

writesymbol1,0,0,0
writesymbol2,0,0,0,-,<,<

writesymbol1,0,0,1
writesymbol2,0,0,0,-,<,<

writesymbol1,0,0,_
writesymbol2,0,0,0,-,<,<

writesymbol1,0,1,0
writesymbol2,0,1,1,-,<,<

writesymbol1,0,1,1
writesymbol2,0,1,1,-,<,<

writesymbol1,0,1,_
writesymbol2,0,1,1,-,<,<

writesymbol1,1,0,0
writesymbol2,1,0,0,-,<,<

writesymbol1,1,0,1
writesymbol2,1,0,0,-,<,<

writesymbol1,1,0,_
writesymbol2,1,0,0,-,<,<

writesymbol1,1,1,0
writesymbol2,1,1,1,-,<,<

writesymbol1,1,1,1
writesymbol2,1,1,1,-,<,<

writesymbol1,1,1,_
writesymbol2,1,1,1,-,<,<


writesymbol2,0,0,0
move1,0,0,0,-,<,>

writesymbol2,0,0,1
move1,0,0,0,-,<,>

writesymbol2,0,0,_
move1,0,0,0,-,<,>

writesymbol2,0,1,0
move1,0,1,1,-,<,>

writesymbol2,0,1,1
move1,0,1,1,-,<,>

writesymbol2,0,1,_
move1,0,1,1,-,<,>

writesymbol2,1,0,0
move1,1,0,0,-,<,>

writesymbol2,1,0,1
move1,1,0,0,-,<,>

writesymbol2,1,0,_
move1,1,0,0,-,<,>

writesymbol2,1,1,0
move1,1,1,1,-,<,>

writesymbol2,1,1,1
move1,1,1,1,-,<,>

writesymbol2,1,1,_
move1,1,1,1,-,<,>

