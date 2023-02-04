
#Source not specified: All state variables are false!

#Target: All bits are 1.

target b0 and b1 and b2 and b3;

transition increment_0()
not b0
{ b0; }

transition increment_1()
b0 and not b1
{ not b0; b1; }

transition increment_2()
b0 and b1 and not b2
{ not b0; not b1; b2; }

transition increment_3()
b0 and b1 and b2 and not b3
{ not b0; not b1; not b2; b3; }