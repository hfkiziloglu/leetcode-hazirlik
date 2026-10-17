"""
Longest Consecutive Sequence (Medium) - Kalıp: Hash set (zincir başı)
Sinyal: O(n) isteniyor + "x+1 var mı?" diye sürekli arama -> set
Fikir: zinciri sadece BAŞINDAN başlat (x-1 set'te yoksa x zincir başıdır).
Her sayı en fazla iki kez ziyaret edilir.
Kaba kuvvet (her sayıdan zincir, dizide arama): O(n^3)
Zaman: O(n)  Bellek: O(n)
"""


class Solution(object):
    def longestConsecutive(self, nums):
        sayilar = set(nums)
        en_uzun = 0
        for x in sayilar:
            if x - 1 not in sayilar:
                uzunluk = 1
                while x + uzunluk in sayilar:
                    uzunluk += 1
                en_uzun = max(en_uzun, uzunluk)
        return en_uzun
