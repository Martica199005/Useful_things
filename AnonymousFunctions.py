#Anonymous functions
#lambda x1,x2,..,xn : <expression>
g=lambda x: 3*x+1

print(g(2))


full_name= lambda fn, ln: fn.strip().title()+" "+ln.strip().title()

h=full_name("Marta", "Agudelo")
print(h)

# Quadratic function

def build_quadratic_function(a,b,c):
  """ Returns the function f(x)= ax^2 +bx +c """
  return lambda x: a*x**2 +b*x +c

f=build_quadratic_function(2,3,-5)

print(f(0))
print(f(1))
print(f(2))

#Calculate f in x=2
f1=build_quadratic_function(3,0,1)(2)
print(f1)


#strip() function

string = '  xoxo love xoxo   '
print(string.strip())
print(string.strip(' xoe'))
# Argument doesn't contain space
# No characters are removed.
print(string.strip('stx'))

string = 'android is awesome'
print(string.strip('an'))



