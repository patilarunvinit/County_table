import pandas as pd

a_file = open("new123.txt", "r")
ll = []
for i in a_file:
  line = i.strip()
  l= line.split("|")
  ll.append(l)
a_file.close()
for i in ll:
    i.pop(0)
    i.pop(0)

Table_IND=[]
Table_USA=[]
Table_WAS=[]
Table_NYC=[]
Table_AU=[]
Table_IND.append(ll[0])
Table_USA.append(ll[0])
Table_WAS.append(ll[0])
Table_NYC.append(ll[0])
Table_AU.append(ll[0])
for i in ll:
  if "IND" in i:
    Table_IND.append(i)
  elif "USA" in i:
      Table_USA.append(i)
  elif "WAS" in i:
      Table_WAS.append(i)
  elif "NYC" in i:
      Table_NYC.append(i)
  elif "AU" in i:
      Table_AU.append(i)
  else:
      continue

IND= pd.DataFrame(Table_IND)
USA= pd.DataFrame(Table_USA)
WAS= pd.DataFrame(Table_WAS)
NYC= pd.DataFrame(Table_NYC)
AU= pd.DataFrame(Table_AU)
print(f"Table_IND \n {IND}")
print("----------------------------------------------------------------------------")
print(f"Table_USA \n {USA}")
print("----------------------------------------------------------------------------")
print(f"Table_WAS \n {WAS}")
print("----------------------------------------------------------------------------")
print(f"Table_NYC \n {NYC}")
print("----------------------------------------------------------------------------")
print(f"Table_AU \n {AU}")
print("----------------------------------------------------------------------------")
