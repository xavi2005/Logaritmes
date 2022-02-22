#Pimer defimin una funció que retorni els intervals en els quals el número pot ser trobat. És una interació per cada numero fins trobar aquell que la seva resta sigui més gran que 0, o sigui quan es sobrepassa el numero. També retorna el anterior per poguer fer l'algoritme amb els dos intervals
def intervals(base,resultat):
  curr = -1
  if base == 1:
    return base

  elif resultat == 0:
    return 1

  if base < 0:
    return None

  while base ** curr - resultat <= 0:
    curr += 1
  else:
    return curr-1,curr

  
#Aqui comprova que si els intervals tenen el resultat del logaritme i, en cas contrari, truca a la funció log per començar a la búsqueda del número
def comprovacio_restricions_log(base,resultat):
  inf,sup = intervals(base, resultat)
  if base ** inf == resultat:
    return inf

  elif base ** sup == resultat:
    return sup

  else:
    log(base,resultat,inf,sup,0)



def log(b,r,i,s,curr):
  #Cas principal on la meitat coincideix amb el número
  x = (i+s)/2
  curr+=1
  
  if b**x == r:
    print(x)

  
  if curr == 30:
    print(x) 

  #Cas contrari on utilitzem recursivitat per trobar el numero. Està inspirat en el mètode binari basat en dividir per la meitat i anar fent els intervals cada vegada més petits

  else:
    if b**x > r:
      s = x
      print(x)
      log(b, r, i, s, curr)

    elif b** x < r:
      print(x)
      i = x
      
      log(b, r, i, s, curr)

b = 2 #Variable condicional
p = 19 #Variable condicional



comprovacio_restricions_log(b,p)
