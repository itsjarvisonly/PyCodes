N = int(input())
step = list(range(N))
dat = dict()
nom = []
gom = []
for k in step:
  name = input()
  grade = float(input())
  dat[name] = grade
for na , ga in dat:
  nom.append(na)
  print(nom)
#def taker(name , grade):