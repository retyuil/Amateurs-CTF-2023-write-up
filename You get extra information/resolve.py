import math
from decimal import *
getcontext().prec = 10000

n = (83790217241770949930785127822292134633736157973099853931383028198485119939022553589863171712515159590920355561620948287649289302675837892832944404211978967792836179441682795846147312001618564075776280810972021418434978269714364099297666710830717154344277019791039237445921454207967552782769647647208575607201)
c =  55170985485931992412061493588380213138061989158987480264288581679930785576529127257790549531229734149688212171710561151529495719876972293968746590202214939126736042529012383384602168155329599794302309463019364103314820346709676184132071708770466649702573831970710420398772142142828226424536566463017178086577
e =  65537
x = (26565552874478429895594150715835574472819014534271940714512961970223616824812349678207505829777946867252164956116701692701674023296773659395833735044077013)

def calculerDelta(a,b,c):
   return Decimal(b*b-4*a*c)


def resoudreEquationSecondDegre(a,b,c):
   delta = calculerDelta(a,b,c)
   if delta > 0:
      racineDeDelta=delta.sqrt()
      retour = [(-b-racineDeDelta)/(2*a),(-b+racineDeDelta)/(2*a)]
   elif delta < 0:
      retour = []  #liste vide
   else:
      retour = [-b/(2*a)] #liste d'un seul élément
   return retour


a = 2
b = -x
c = n

#q = (resoudreEquationSecondDegre(a,b,c)[1])

#p = (n / q)

f = 12346
encoded = 55170985485931992412061493588380213138061989158987480264288581679930785576529127257790549531229734149688212171710561151529495719876972293968746590202214939126736042529012383384602168155329599794302309463019364103314820346709676184132071708770466649702573831970710420398772142142828226424536566463017178086577



q = 8128979845892982561867353232387733688040820165501281055994560204992985831326225951788922087412585314864187432126945670029964128100746510232539453211798711
p = 10307593182692464771859444251060107096737374203269378602523841560237645162159897774629661654952776237523790091862810352641745767095280638930754828620479591

phi = (p-1)*(q-1)
d = pow(e,-1,phi)
flag = pow(encoded,d,n)
flag = hex(flag)[2:]
print(bytes.fromhex(flag))
