import pandas as pd

df = pd.read_csv("reference.csv", delimiter=",")
df = df.iloc[:,[0,1,2,3,4,5,6,7,9]]
# dict = {
#     "'":0,"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, 
#     "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15,
#     "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, 
#     "x": 24, "y": 25, "z": 26," ": 30, "/":31
# }
# namehash=[]

# for i in range(len(df)):
#     names=list(str(df.iloc[i,0]))
#     names.reverse()
#     hash=0
#     for n,letter in enumerate(names):
#         hash+=dict[letter]*(32**n)
#     namehash.append(hash)

# hash=pd.DataFrame({"Name Code":namehash})
# df=pd.concat([df,hash],axis=1)
# print(df.head())



# cR=[];cG=[];cB=[];cH=[];cS=[];cV=[]
# dict={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"a":10,"b":11,"c":12,"d":13,"e":14,"f":15}
# for i in range(len(df)):
#     hex=str(df.iloc[i,1])
#     hex=list(hex)
#     R=dict[hex[1]]*16+dict[hex[2]]
#     G=dict[hex[3]]*16+dict[hex[4]]
#     B=dict[hex[5]]*16+dict[hex[6]]

#     cR.append(R)
#     cG.append(G)
#     cB.append(B)

#     R/=255
#     G/=255
#     B/=255

#     cmax=max(R,G,B)
#     cmin=min(R,G,B)
#     delta=cmax-cmin

#     if delta==0:
#         H=0
#     elif cmax==R:
#         H=60*(((G-B)/delta)%6)
#     elif cmax==G:
#         H=60*(((B-R)/delta)+2)
#     elif cmax==B:
#         H=60*(((R-G)/delta)+4)

#     if cmax==0:
#         S=0
#     else:
#         S=delta/cmax
    
#     V=cmax
#     cH.append(H)
#     cS.append(S*100)
#     cV.append(V*100)

# cd=pd.DataFrame({"R":cR,"G":cG,"B":cB,"H":cH,"S":cS,"V":cV})
# df=pd.concat([df,cd],axis=1)

df.to_csv("reference.csv", index=False)
