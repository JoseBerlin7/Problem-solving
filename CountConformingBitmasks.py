'''
Problem -5:
In this problem we consider unsigned 30-bit integers, i.e. all integers B such that 0 ≤ B < 230.

We say that integer A conforms to integer B if, in all positions where B has bits set to 1, A has corresponding bits set to 1.

For example:

00 0000 1111 0111 1101 1110 0000 1111(BIN) = 16,244,239 conforms to
00 0000 1100 0110 1101 1110 0000 0001(BIN) = 13,032,961, but
11 0000 1101 0111 0000 1010 0000 0101(BIN) = 819,399,173 does not conform to
00 0000 1001 0110 0011 0011 0000 1111(BIN) = 9,843,471.
Write a function:

def solution(A, B, C)

that, given three unsigned 30-bit integers A, B and C, returns the number of unsigned 30-bit integers conforming to at least one of the given integers.

For example, for integers:

A = 11 1111 1111 1111 1111 1111 1001 1111(BIN) = 1,073,741,727,
B = 11 1111 1111 1111 1111 1111 0011 1111(BIN) = 1,073,741,631, and
C = 11 1111 1111 1111 1111 1111 0110 1111(BIN) = 1,073,741,679,
the function should return 8, since there are 8 unsigned 30-bit integers conforming to A, B or C, namely:

11 1111 1111 1111 1111 1111 0011 1111(BIN) = 1,073,741,631,
11 1111 1111 1111 1111 1111 0110 1111(BIN) = 1,073,741,679,
11 1111 1111 1111 1111 1111 0111 1111(BIN) = 1,073,741,695,
11 1111 1111 1111 1111 1111 1001 1111(BIN) = 1,073,741,727,
11 1111 1111 1111 1111 1111 1011 1111(BIN) = 1,073,741,759,
11 1111 1111 1111 1111 1111 1101 1111(BIN) = 1,073,741,791,
11 1111 1111 1111 1111 1111 1110 1111(BIN) = 1,073,741,807,
11 1111 1111 1111 1111 1111 1111 1111(BIN) = 1,073,741,823.
Write an efficient algorithm for the following assumptions:

A, B and C are integers within the range [0..1,073,741,823].
'''
# Solution
'''
Idea:
1. count all the possbilities of 30 bit unsigned integer for A,B,C 
2. Then minus the repetition of the possibilities (i.e., A or B, A or C, B or C)
3. Then add the possibilities of A,B,C together (i.e., A or B or C)'''

def solution(A, B, C):
    nA = 0
    nB = 0
    nC = 0
    nAB = nAC = nBC = nABC = 0 
    AoB, AoC, BoC, AoBoC = A|B, A|C, B|C, A|B|C

    for i in range(30):
        # Finding the valid possiblities of A, B, C
        if ((A >> i) & 0x01) == 0:
            nA += 1
        if ((B >> i) & 0x01) == 0:
            nB += 1
        if ((C >> i) & 0x01) == 0:
            nC += 1
        
        # Finding the valid possiblities of A or B, A or C, B or C
        if ((AoB>>i)&0x01) ==0:
            nAB +=1
        if ((AoC>>i)&0x01) ==0:
            nAC +=1
        if ((BoC>>i)&0x01) ==0:
            nBC +=1
        
        # Finding the valid possiblities of A or B or C
        if((AoBoC)&0x01) == 0:
            nABC +=1
    
    # calculating the actual possibilities  
    return ((1<<nA) + (1<<nB) + (1<<nC) - (1<<nAB) - (1<<nAC) - (1<<nBC) + (1<<nABC))
        
        
        

A = 1073741727  # 11 1111 1111 1111 1111 1111 1001 1111
B = 1073741631  # 11 1111 1111 1111 1111 1111 0011 1111
C = 1073741679  # 11 1111 1111 1111 1111 1111 0110 1111
print(solution(A, B, C)) 