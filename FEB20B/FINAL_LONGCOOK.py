l = len(DB)
def searchh( x ): 
    for i in range(0,l) :
        if ( DB[i] >= x ) :
            return i
def countofcollisions(a,b) :
    low = searchh(a)
    hi = searchh(b)
    if ( DB[hi] != b ) :
        hi -= 1
    return hi-low+1
def main() :
    t = int(input()) 
    while ( t > 0 ) :
        t -= 1
        start_m = input().split()
        start_y = int(start_m[1])
        start_m = int(start_m[0])
        end_m = input().split()
        end_y = int(end_m[1])
        end_m = int(end_m[0])
                if start_m > 2 :
            start_y += 1 
        if end_m == 1 :
            end_y -= 1 
        print(countofcollisions(start_y,end_y))
main()