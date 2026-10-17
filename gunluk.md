# Soru Günlüğü

Tekrar aralıkları: Aşama 0 → 1 gün, 1 → 3 gün, 2 → 7 gün, 3 → 21 gün, 4 → tamam.
Tekrarda yardımsız çözersen aşama +1, çözemezsen aşama 0.

| Tarih | Soru | Zorluk | Kalıp | Kendim çözdüm mü | Nerede takıldım | Aşama | Sonraki tekrar |
|---|---|---|---|---|---|---|---|
| 17.10.2026 | Contains Duplicate | Easy | Hash set (arama) | Evet | Kaba kuvvette bellek (O(1) olmalı) | 1 | 20.10.2026 |
| 17.10.2026 | Valid Anagram | Easy | Hash map (sayma) | Evet | Karmaşıklığı önce ters söyledi, isimlendirme, elle testte azaltmayı atladı | 1 | 20.10.2026 |
| 17.10.2026 | Two Sum | Easy | Hash map (tamamlayıcı arama) | Hayır | Önce tüm sözlüğü doldurma tuzağı, return'de yanlış anahtar (2. kez), yarım isim değişikliği | 0 | 18.10.2026 |
| 18.10.2026 | Group Anagrams | Medium | Hash map (gruplama) | Hayır | n²·k karmaşıklığı, dict anahtar olamaz (unhashable), sorted() liste döndürür | 0 | 19.10.2026 |
| 18.10.2026 | Longest Consecutive Sequence | Medium | Hash set (zincir başı) | Hayır | Set'in rolü, O(n³) hesabı, "zincir başı" fikri | 0 | 19.10.2026 |

## Tekrar eden zayıf noktalar
- Bellek karmaşıklığı: "Benim oluşturduğum bir şey girdiyle büyüyor mu?" diye sor.
- Sınıf adı yerine değişken adı: `set.add`, `dict[i]` → kendi değişkenini kullan.
- Metot parantezi: `.keys` değil `.keys()` (ya da hiç `.keys` kullanma: `x in sozluk`).
- `in` ile neyi kontrol ettiysen, değeri alırken de aynı anahtarı kullan.
- İsim değiştirince kodda geçtiği her yeri değiştir.
