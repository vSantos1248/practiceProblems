import math;
'''
def testPrime(n):
    if(n<2): return False;
    if(n<4): return True;
    if(n%2==0 or n%3==0): return False;
    i=5;
    while(i*i<=n):
        if(n%i==0 or n%(i+2))==0: return False;
        i+=6;
    return True;
'''

'''
def checkRegion(grid, i, j, region, coords):
    region+=1;
    coords.append([i,j]);
    if i!=0 and [i-1, j] not in coords: #left
        if grid[i-1][j]==1: region, coords=checkRegion(grid, i-1, j, region, coords);
    if i!=len(grid)-1 and [i+1, j] not in coords: #right
        if grid[i+1][j]==1: region, coords=checkRegion(grid, i+1, j, region, coords);
    if j!=0 and [i, j-1] not in coords: #down
        if grid[i][j-1]==1: region, coords=checkRegion(grid, i, j-1, region, coords);
    if j!=len(grid[0])-1 and [i,j+1] not in coords: #up
        if grid[i][j+1]==1: region, coords=checkRegion(grid, i, j+1, region, coords);   
    if i!=0 and j!=len(grid[0])-1 and [i-1,j+1] not in coords: #up-left
        if grid[i-1][j+1]==1: region, coords=checkRegion(grid, i-1, j+1, region, coords);
    if j!=len(grid[0])-1 and i!=len(grid)-1 and [i+1,j+1] not in coords: #up-right
        if grid[i+1][j+1]==1: region, coords=checkRegion(grid, i+1, j+1, region, coords);
    if j!=0 and i!=0 and [i-1,j-1] not in coords: #down-left
        if grid[i-1][j-1]==1: region, coords=checkRegion(grid, i-1, j-1, region, coords);
    if j!=0 and i!=len(grid)-1 and [i+1,j-1] not in coords: #down-right
        if grid[i+1][j-1]==1: region, coords=checkRegion(grid, i+1, j-1, region, coords);
    return region, coords;
    
def getBiggestRegion(grid):
    region=0;
    maxRegion=0;
    coords=[];
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if [i,j] not in coords and grid[i][j]==1:
                region, coords=checkRegion(grid, i, j, 0, coords);
                if region>maxRegion: maxRegion=region;
    return maxRegion;

grid=[[1,0,0,1],[1,1,1,1],[0,0,0,0],[1,1,0,0],[0,0,0,1]];
print(getBiggestRegion(grid))
'''


'''
def sumOfTwo(a, b, v): #not working for 1 test case
    i=0;
    j=0;
    a=sorted(a);
    b=sorted(b);
    
    
    for i in a:
        low=0;
        high=len(b)-1;
        mid=(low+high)//2;
        while(low<=high):
            temp=b[mid];
            if i+temp==v: return True;
            if i+temp>v: high=mid-1;
            if i+temp<v: low=mid+1;
            mid=(low+high)//2;           
    return False;

a=[4,5,7,1,2,6,7,1,6,8,2,4];
b=[1,3,6,8,9,2,4,6,8,2,1,7,7,2,1,3,2,7,2];
print(sumOfTwo(a, b, 20));
print(sumOfTwo([1,2,3],[10,20,30,40],42));
'''

'''
def textJustifier(text, width):        
    def getWord(text, start, width):
        temp="";
        for i in range(start, len(text)):
            if(text[i]==" "): return temp;
            temp+=text[i];
        return temp;
    def fixLine(tempLine, width):
        if(tempLine[len(tempLine)-1]==" "): tempLine=tempLine[:len(tempLine)-1];
        diff=width-len(tempLine);
        if(diff==0): return tempLine+"\n";
        spaces=tempLine.count(" ");
        i=0;
        while(diff>0):
            if tempLine[i]==" ":
                tempLine=tempLine[:i]+" "+tempLine[i:];
                diff-=1;
                if diff==0: break;
                while(i<len(tempLine) and tempLine[i]==" "): i+=1;
            else: i+=1;
            if(diff>0 and i>=len(tempLine)): i=0;
        return tempLine+"\n";
    
    start=0;
    tempLine="";
    retString="";
    while(len(text)>0):
        tempWord=getWord(text, start, width);
        if(len(tempLine)+len(tempWord)<width):
            tempLine=tempLine+tempWord+" ";
            start+=len(tempWord)+1;
        else:
            retString+=fixLine(tempLine, width);
            text=text[start:];
            tempLine="";
            start=0;
    return retString; #last line is broken
            
text="Lorem ipsum dolor sit amet, vis veniam vivendo at, ei usu accusata dissentiunt, te mel ancillae constituam. Te aeque graeco mei. Sumo percipit detraxit in duo, ea verterem recteque scribentur has, nec agam iriure equidem eu. Labores noluisse concludaturque no sea, at eum posse dolorum. Mutat urbanitas eam at, vis ad melius dissentiunt.";
print(text+"\n\n");
print(textJustifier(text, 40));
'''

'''
n=150
print([b for b in bin(n)[2:] if b=="0"])
'''

'''
def amendTheSentence(s):
    i=0;
    while(i<len(s)):
        if(i!=0 and s[i].isupper()):
            s=s[:i]+" "+s[i:];
            i+=1;
        i+=1;
    return s.lower();
print(amendTheSentence("HelloThisSucksLol"));
'''

'''
def findFirstSubstringOccurrence(s, x):
    for i in range(len(s)):
        if(s[i]==x[0]):
            if s[i:i+len(x)] == x: return i;
    return -1;

print(findFirstSubstringOccurrence("CodefightsIsAwesome","IsA"));
'''

'''
def regexMatching(pattern, test):
    if pattern[0]=="^": 
        return pattern[1:]==test[0:len(pattern)-1];
    if pattern[len(pattern)-1]=="$":
        return pattern[:len(pattern)-1]==test[(len(test)-len(pattern)+1):]
    return (pattern in test);
print(regexMatching("^code","codefights"));
'''

'''
#given a sorted array, a, remove all duplicate values without using
#extra memory for new lists, dictionaries, etc
def removeDuplicates(a):
    i=0;
    a.append(None);
    while(a[i]):
        while(a[i]==a[i+1]): del a[i+1];
        i+=1;
    a.pop();
    return a;
a=[1,2,2,3,4,5,6,7,8,8,8,9,10,10,10,11,12,12];
b=[1,1,2];
print(removeDuplicates(b));
'''

'''
def findFirstSubstringOccurrence(s, x):
    if x not in s: 
        return -1;
    else:
        for i in range(len(s)):
            if s[i:i+len(x)] == x: 
                return i;
	#return -1;
'''

'''
def classifyStrings(s):
    vowels=["a", "e", "i", "o", "u"];
    
    v=0;
    c=0;
    mixed=0;
    mixedFlag=False;
    
    for i in s:
        if i=="?":
            v+=1;
            c+=1;
            mixed=5;
        elif i in vowels:
            v+=1;
            c=0;
            mixed-=1;
        else:
            c+=1;
            v=0;
            mixed-=1;
            
        if v>=3 or c>=5:
            if((mixed>0 and c==5) or (mixed>2 and v==3)): 
                if(c==5 and v==3): return "bad";
                else:
                    mixedFlag=True;
            else: return "bad";
    
    if mixedFlag: return "mixed";
    return "good";
        

print(classifyStrings("aa?bbbb")); #bad?
print(classifyStrings("bbbb?a?bbb?a?bbbb"));#bad
print(classifyStrings("aa?bbb?aa"));#bad
print(classifyStrings("bbbb?a?bbbb"));#bad
print(classifyStrings("bbbb?bbbbaa"));#mixed
'''

'''
def sumOfTwo(a, b, v):
    if len(a)==0 or len(b)==0: return False;
    #a=list(set(a));
    #b=list(set(b));
    a=sorted(a); #nlogn
    b=sorted(b); #mlogm
    for i in a: #n
        #if i>v: return False;
        low=0;
        high=len(b)-1;
        mid=(low+high)//2;
        while(low<=high): #logm
            if i+b[mid]==v: return True;
            if i+b[mid]>v: high=mid-1;
            if i+b[mid]<v: low=mid+1;
            mid=(low+high)//2;
    return False; #nlogn+(m+n)logm
'''

