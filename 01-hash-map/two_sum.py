"""
Two Sum (Easy) - Kalıp: Hash map (tamamlayıcı arama)
Sinyal: bir elemanı bilince diğeri belli oluyor (target - x) -> sözlükte ara
Zaman: O(n)  Bellek: O(n)
Defter benzetmesi: her gelen ÖNCE "beni bekleyen var mı?" diye bakar,
yoksa "şu sayıyı bekliyorum, sıram şu" diye yazar.
Önce bak, sonra yaz -> eleman kendisiyle eşleşemez ([3, 2, 4], 6 tuzağı).
"""


class Solution(object):
    def twoSum(self, nums, target):
        tamamlayicilar = dict()
        for i in range(len(nums)):
            if nums[i] in tamamlayicilar:
                return [tamamlayicilar[nums[i]], i]
            tamamlayicilar[target - nums[i]] = i
