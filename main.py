'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  if n > 1:
    for i in range(2, int(n / 2) + 1):
      if (n % i) == 0:
        return False
    return True
  else:
    return False
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  produs = 1
  for element in lst:
    produs = produs * element
  return produs


'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  if y == 0:
    return x
  elif x== 0:
    return y
  return get_cmmdc_v1(y,x%y)
  
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  # codul vostru aici
  if x == 0:
    return y
  if y == 0:
    return x
  if x == y:
    return x
  if x > y:
    return get_cmmdc_v2(x-y,y)
  return get_cmmdc_v2(x,y-x)

  

def main():
  # interfata de tip consola aici
  lista = [3,5,7,1,5]
  print(get_product(lista))
  a=12
  b=16
  print(get_cmmdc_v1(a,b))
  nrprim = 13
  print(is_prime(nrprim))
  print(is_prime(12))
  print(get_cmmdc_v2(25,10))

if __name__ == '__main__':
  main()