
source p1;

target X and Y;

transition p1p2()
p1 and (not X or not Y)
{ not p1; p2; }

transition p2p3()
p2 and not X
{ not p2; p3; }

transition p3p1()
p3 
{ not p3; p1; X; }

transition p2p4()
p2 and X
{ not p2; p4; }

transition p4p1()
p4
{ not p4; p1; Y; }

transition p1p5()
p1 and X and Y
{ not p1; p5; }