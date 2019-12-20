s = 'azcbobobegghakl'
j=0
count =0
array=''
var=s[0]
length = len(s)
for i in range(length-1):
    if(s[i] <= s[i+1]):
        var = var+s[i+1]
        count+=1
    else:
        if(count>j):
            j= count
            array=var
            print array
        count =0
        var = s[i+1]
if(count>j):
    j= count
    array=var
print "Longest substring in alphabetical order is: "+ str(array)