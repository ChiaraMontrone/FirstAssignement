ab = int(input())
bc = int(input())
import math

ac = math.sqrt(ab**2 + bc**2)
#print(ac)
mc = ac / 2
div = ab / ac
mcb = round(math.degrees(math.asin(div)))
#print(mcb)
bm = math.sqrt( mc**2 + bc**2 -2*((mc*bc)*(math.cos(math.radians(mcb)))))
#print (bm)

fract = round(mc / bm)
last = fract*math.sin(math.radians(mcb))
mbc = math.asin(last)

print(str(round(math.degrees(mbc)))+chr(176))
