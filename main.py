'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  # codul vostru aici
  return 1
  
  
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
  # codul vostru aici
  return 3
  
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  # codul vostru aici
  return 0
  

def main():
  # interfata de tip consola aici
  lista = [3,5,7,1,5]
  print(get_product(lista))

if __name__ == '__main__':
  main()