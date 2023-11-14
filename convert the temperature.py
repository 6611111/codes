class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        l=[]
        k=(celsius+273.15)+10**-5
        f=(celsius*1.80+32.00)+10**-5
        l.append(k)
        l.append(f)
        return l
