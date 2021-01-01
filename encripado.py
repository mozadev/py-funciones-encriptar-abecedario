def encriptar(y):
  x1=y.replace('a', 'z')
  x2=x1.replace('b', 'y')
  x3=x2.replace('c', 'x')
  x4=x3.replace('d', 'w')
  x5=x4.replace('e', 'v')
  x6=x5.replace('f', 'u')
  x7=x6.replace('g', 't')
  x8=x7.replace('h', 's')
  x9=x8.replace('i', 'r')
  x10=x9.replace('j', 'q')
  x11 = x10.replace('k', 'p')
  x12 = x11.replace('l', 'o')
  x13 = x12.replace('m', 'n')

  dic = {'n':'m', 'o':'l', 'p':'k', 'q':'j', 'r':'i', 's':'h', 't':'q', 'u':'f', 'v':'e', 'w':'d', 'x':'c', 'y':'b', 'z':'a'}


  for i in range(len(x13)):
      if x13[i]==y[i]:

          x13 = x13.replace(x13[i],dic[x13[i]])


  return x13


y= input("¿Qué frase quieres encriptar?: ").lower() or 'HOLA'
z=encriptar(y)
print(z)


