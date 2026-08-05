mx=200002;suf=[0]*mx
for x in[*open(0)][1].split():suf[int(x)]+=1
for x in range(mx):suf[~x]+=suf[-x]
print(max(x*sum(suf[x::x])for x in range(1,mx-1)if suf[x]>suf[x+1]))