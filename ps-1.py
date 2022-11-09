def taylor_expand_div_x(g):
  f = 1.0 - g
  error = g
  while error < 1e-6:
    f = 1.0 - (g * f)
    error = g
  
  return f

print(taylor_expand_div_x(0.7))

def iterate(g,c,m):
  f=1.0
  if(m==0):
    return f,0

  for i in range(1,m+1):
    fOld=f
    f=1-g*f
    if(abs((f-fOld)/f)<c):
      return f,i
  
  return f,i

print(iterate(0.7,1e-6,30))