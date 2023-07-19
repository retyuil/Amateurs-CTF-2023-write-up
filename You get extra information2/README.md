
# You get extra information 2

This challenge is similar to the challenge you get extre information 1

The output gives us the result of the following equation : $`n^2(p^3 + 5(p+1)^2) + 5nq + q^2`$

We know that n = p*q so by replacing q by n/p we get an equation with get an equation where the only unknow is p.

Unfortunately the equation is of degree 5 so we can't find exact solution to it. 
But we know that p is an int so we just need to be close to the solution.

To calculat the equation I used Bisection method, here is my code :

```
def h(x):
    q = Decimal(n/x)
    return((n**2)*(x**3 + 5*(x+1)**2) + 5*n*q + q**2 - k)

def solve_equation(lower_bound, upper_bound):
    # Précision décimale

    # Bornes inférieure et supérieure de l'intervalle
    lower = Decimal(lower_bound)
    upper = Decimal(upper_bound)

    # Vérification des signes des bornes
    if h(lower) * h(upper) > 0:
        print("Pas de racine dans l'intervalle donné")
        return None  # Pas de racine dans l'intervalle donné

    # Itérations de la méthode de bissection
    while upper - lower > Decimal('1e-2'):
        mid = Decimal((lower + upper) / 2)  # Point milieu de l'intervalle
        print(h(mid))
        if h(mid) == 0:
            return mid  # Solution trouvée
        elif h(mid) * h(lower) < 0:
            upper = Decimal(mid)
            print("Monte")
        else:
            lower = Decimal(mid)
            print("Descend")

    return (lower + upper) / 2  # Approximation de la racine


lower_bound = Decimal(2**511)
upper_bound = Decimal(2**513)


res = math.ceil(solve_equation(lower_bound,upper_bound))
print(math.floor(res) - 1)
```

This code allows us to calculate p and therefore to factorise n. 
