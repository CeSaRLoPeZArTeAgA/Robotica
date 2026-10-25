import sympy as sp
from rot3DS import Rxhs,Rzhs
pfi, theta, psi, alfa = sp.symbols("pfi theta psi alfa")
print("\n*****Matriz homogenea simbolica*****\n")
H=Rzhs(alfa)@Rxhs(pfi)@Rzhs(theta)@Rxhs(psi)
print(H)
print("\n*****Reemplazando valores*****\n")
valores = {pfi:-30, theta:45, psi:60, alfa:75}
H=H.subs(valores)
print(H)
print("\n*****Evaluando*****\n")
H=H.evalf()
print(H)
print("\n*****H redondeado*****\n")
H_redondeado = [sp.N(val, 2) for val in H]
print(H_redondeado,2)