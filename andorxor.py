S=input()
A=int(S[0])
L=len(S)
for i in range(0,L-2,2):
    op=S[i+1]
    B=int(S[i+2])
    if op=="a":
      A=A&B
    elif op=="b":
      A=A | B
    elif op=="c":
      A=A^B
print(A)
