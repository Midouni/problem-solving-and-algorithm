# link: https://codeforces.com/contest/69/problem/A
# Name: A. Young Physicist
# statut: Accepted
# type: Math

res=[0,0,0]
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    res[0]+=x
    res[1]+=y
    res[2]+=z
print("YES" if res[0]==res[1]==res[2]==0 else "NO")
