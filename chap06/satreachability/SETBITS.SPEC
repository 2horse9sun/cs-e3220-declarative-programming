
#Source not specified: All state variables are false!

#Target: All bits are 1.


# Every transition turns one bit 1.

trajectoryformula
a@3 and b@3 and not c@3;

transition t1()
not a and not b
{ a; }

transition t2()
not b
{ b; }

transition t3()
a and b and c
{ not a; not b; not c; }

# Comment
# With SAT and partially ordered transition sequences this problem
# is trivial, as all transitions are independent. Without the partial
# ordering, the proofs that sequences of length N-1 and shorter
# do not exist become very difficult. However, source-target sequences
# could still be found fast without knowledge the required transition
# sequence length if multiple SAT solvers were run at the same time
# for different lengths.
