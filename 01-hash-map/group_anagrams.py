"""
Group Anagrams (Medium) - Kalıp: Hash map (gruplama)
Sinyal: "aynı özelliği taşıyanları grupla" -> ortak etiket = sözlük anahtarı
Etiket: harfleri sıralanmış string ("tea" -> "aet").
Sözlük/liste anahtar olamaz (değiştirilebilir); string ve tuple olabilir.
Kaba kuvvet (her grubun ilk elemanıyla isAnagram): O(n^2 * k)
Zaman: O(n * k log k)  Bellek: O(n * k)
"""
from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        gruplar = defaultdict(list)
        for kelime in strs:
            etiket = "".join(sorted(kelime))
            gruplar[etiket].append(kelime)
        return list(gruplar.values())
