#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kayıp Çorap Arayıcı - Evrenin En Gereksiz Ama En Samimi Programı
Bu program kayıp çoraplarınızı bulmak için tasarlanmıştır.
Ancak çoraplar hiçbir zaman bulunmaz. Çünkü çoraplar özgür olmak ister.
"""

import time
import random
import sys

def sonsuz_arama():
    print("\n🔍 Çorap Arama Ritiüeli Başlatıldı...")
    print("Dikkat: Bu program asla bitmez. Çoraplar gibi kaybolmak serbesttir.\n")
    
    yerler = [
        "yatağın altı",
        "çamaşır makinesi arkası",
        "komşunun balkonu",
        "paralel evren",
        "devletin kayıp eşya deposu",
        "kendi vicdanınız"
    ]
    
    deneme = 0
    while True:  # Sonsuz döngü, çoraplar gibi
        deneme += 1
        yer = random.choice(yerler)
        print(f"[{deneme}. deneme] {yer} kontrol ediliyor...")
        time.sleep(random.uniform(1.5, 4.0))  # Gerçekçi arama süresi
        
        sonuc = random.choice([
            "Hiçbir şey bulunamadı. Çorap kaçmış olmalı.",
            "Toz ve ümitsizlik bulundu.",
            "Bir tane tek çorap bulundu ama eşi yok. Trajedi.",
            "Çorap 'ben özgürüm' diye bağırdı ve kayboldu.",
            "Arama başarısız. Belki de çoraplar hiç var olmadı."
        ])
        print(f"   → {sonuc}\n")
        
        # Gizli mesaj (saklı siyasi anlam)
        if deneme % 13 == 0:
            print("   (Not: Bazen kaybolan şeyler geri gelmez, tıpkı bazı haklar gibi. Sessiz kal.)\n")
        
        if deneme > 100:
            print("Hala arıyorum. Çoraplar inatçıdır. Sen de ol.")
            deneme = 0  # Reset ama devam et

if __name__ == "__main__":
    try:
        sonsuz_arama()
    except KeyboardInterrupt:
        print("\n\nProgram durduruldu. Ama çoraplar hala kayıp. 😅")
        print("\n--- Damga ---")
        print("İmza: Kayyum Grok | Tarih: 17.10.2026 | İsim: Sonsuz Çorap Avcısı")
        print("Ciddiyet seviyesi: %87 (abartılı ama samimi)")
        sys.exit(0)
