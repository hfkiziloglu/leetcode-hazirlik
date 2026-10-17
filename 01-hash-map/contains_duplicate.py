"""
Contains Duplicate (Easy) - Kalıp: Hash set (arama)
Sinyal: "tekrar var mı?" = "bu değeri daha önce gördüm mü?"
Zaman: O(n)  Bellek: O(n)
Alternatifler: iç içe döngü O(n^2)/O(1), sıralama O(n log n)/O(1) (diziyi değiştirir)
"""


class Solution(object):
    def containsDuplicate(self, nums):
        farkli_sayilar = set()
        for num in nums:
            if num in farkli_sayilar:
                return True
            farkli_sayilar.add(num)
        return False
