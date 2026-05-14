# Automatic Citation Integrity Verification for LLM-Assisted Academic Writing

Tento repozitár obsahuje zdrojové kódy, konfiguračné súbory a dokumentáciu k diplomovej práci na Fakulte matematiky, fyziky a informatiky Univerzity Komenského v Bratislave [1, 2].

## 📝 Abstrakt a cieľ
Cieľom práce je navrhnúť a vyhodnotiť systém, ktorý extrahuje a normalizuje citačné reťazce a kotvy z textu, overuje ich voči vedeckým metadátam (napr. OpenCitations) a posudzuje, či citované dielo skutočne podporuje tvrdenie v texte [2]. Systém je navrhnutý tak, aby identifikoval halucinácie LLM (fiktívne citácie), chyby v metadátach a slabé sémantické prepojenia [2, 3].

## 🎯 Hlavné ciele (Aims)
*   **Vytvorenie evaluačného setu:** Zostavenie súboru akademických pasáží s citáciami (vrátane generovaných LLM) so štítkami pre existenciu, správnosť metadát a podporu kontextu [3].
*   **Benchmarking parsovania:** Testovanie robustnosti parsovania a normalizácie "hlučných" a formátovo rôznorodých bibliografických reťazcov s dôrazom na neúplné metadáta [3].
*   **Vývoj rezolučného modulu:** Implementácia systému na obnovu identifikátorov a fuzzy matching, ktorý odlíši neexistujúce diela od reálnych, ale zle formátovaných referencií [3].
*   **Overovanie citačnej podpory:** Prototypovanie mechanizmu na skórovanie sémantickej zhody medzi tvrdením a citovaným dielom [3].
*   **Analýza kompromisov:** Vyhodnotenie presnosti, nákladov a latencie pre praktické redakčné a edukačné použitie [3].

## 📚 Kľúčová literatúra
Práca vychádza z analýzy nasledujúcich vedeckých prác:
*   **Walters (2023):** Výskum fabrikácií a chýb v citáciách generovaných ChatGPT [4, 5].
*   **Guenci et al. (2025):** Pipeline pre párovanie referencií s neúplnými metadátami pomocou OpenCitations a Crossref [4, 6].
*   **CiteME (2024):** Benchmark pre priraďovanie citácií a systém CiteAgent [7-9].
*   **Alvarez et al. (2024):** Zero-shot overovanie vedeckých tvrdení pomocou LLM a citačného textu [4, 10].

## ✅ Postup práce (Roadmap)

### 1. Príprava a rešerš
- [x] Štúdium literatúry o halucináciách LLM v citáciách (Walters) [5, 11]
- [x] Analýza techník matchingu neúplných metadát (Guenci et al.) [6, 12]
- [x] Štúdium sémantického overovania tvrdení (Alvarez et al., CiteME) [8, 10]
- [x] Definícia technickej architektúry a cieľov práce [2, 3]

### 2. Dátová a praktická časť
- [ ] Zber a kurácia evaluačného datasetu (akademické pasáže + LLM citácie) [3]
- [ ] Generovanie negatívnych vzoriek (negácií) pomocou LLM pre testovanie [13, 14]
- [ ] Implementácia ML parsera (GROBID) na extrakciu z hlučných dát [15, 16]
- [ ] Vývoj rezolučného modulu (kaskádová stratégia dopytov SPARQL) [12, 17]

### 3. Evaluácia a finalizácia
- [ ] Benchmarking úspešnosti extrakcie a matchingu [3]
- [ ] Testovanie sémantického verifikátora v zero-shot režime [18, 19]
- [ ] Analýza limitov (jazykové bariéry, nekonzistencia rokov) [20]
- [ ] Dopísanie textu diplomovej práce a dokumentácie [1]

## 🛠 Technológie
*   **Jazyk:** Python
*   **Dátové zdroje:** OpenCitations Meta, Crossref, Semantic Scholar [6, 9, 12]
*   **Modely:** GPT-4, GPT-3.5 (pre overovanie a negácie) [13, 18, 21]
*   **Nástroje:** GROBID, SPARQL [12, 16]

---
**Autor:** Bc. Vladimír Tischler [1]
**Školiteľ:** Mgr. Marek Šuppa [1, 7]
**Pracovisko:** Katedra aplikovanej informatiky, FMFI UK [1, 7]
