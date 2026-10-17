"""
Valid Anagram (Easy) - Kalıp: Hash map (sayma)
Sinyal: "her harf iki string'de aynı sayıda geçmeli" -> frekans tablosu
Zaman: O(n)  Bellek: O(1) (sadece 26 küçük harf)
Kısa yol: return Counter(s) == Counter(t)
"""


class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        harf_sayilari = dict()
        for harf in s:
            if harf in harf_sayilari:
                harf_sayilari[harf] += 1
            else:
                harf_sayilari[harf] = 1

        for harf in t:
            if harf not in harf_sayilari:
                return False
            harf_sayilari[harf] -= 1

        for sayi in harf_sayilari.values():
            if sayi != 0:
                return False
        return True
