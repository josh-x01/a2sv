class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius+273.15,(9/5)*celsius+32]