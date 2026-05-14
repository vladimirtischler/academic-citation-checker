# Automatic Citation Integrity Verification for LLM-Assisted Academic Writing

Tento repozitár obsahuje zdrojové kódy, konfiguračné súbory a dokumentáciu k diplomovej práci na Fakulte matematiky, fyziky a informatiky Univerzity Komenského v Bratislave.

## 📝 Abstrakt a cieľ
Cieľom práce je navrhnúť a vyhodnotiť systém, ktorý extrahuje a normalizuje citačné reťazce a kotvy z textu, overuje ich voči vedeckým metadátam (napr. OpenCitations) a posudzuje, či citované dielo skutočne podporuje tvrdenie v texte. Systém je navrhnutý tak, aby identifikoval halucinácie LLM (fiktívne citácie), chyby v metadátach a slabé sémantické prepojenia.

## 🎯 Hlavné ciele (Aims)
*   **Vytvorenie evaluačného setu:** Zostavenie súboru akademických pasáží s citáciami (vrátane generovaných LLM) so štítkami pre existenciu, správnosť metadát a podporu kontextu.
*   **Benchmarking parsovania:** Testovanie robustnosti parsovania a normalizácie "hlučných" a formátovo rôznorodých bibliografických reťazcov s dôrazom na neúplné metadáta.
*   **Vývoj rezolučného modulu:** Implementácia systému na obnovu identifikátorov a fuzzy matching, ktorý odlíši neexistujúce diela od reálnych, ale zle formátovaných referencií.
*   **Overovanie citačnej podpory:** Prototypovanie mechanizmu na skórovanie sémantickej zhody medzi tvrdením a citovaným dielom.
*   **Analýza kompromisov:** Vyhodnotenie presnosti, nákladov a latencie pre praktické redakčné a edukačné použitie.

## 📚 Kľúčová literatúra
Práca vychádza z analýzy nasledujúcich vedeckých prác:
*   **Walters (2023):** Výskum fabrikácií a chýb v citáciách generovaných ChatGPT.
*   **Guenci et al. (2025):** Pipeline pre párovanie referencií s neúplnými metadátami pomocou OpenCitations a Crossref.
*   **CiteME (2024):** Benchmark pre priraďovanie citácií a systém CiteAgent.
*   **Alvarez et al. (2024):** Zero-shot overovanie vedeckých tvrdení pomocou LLM a citačného textu.

## ✅ Postup práce (Roadmap)

### 1. Príprava a rešerš
- [x] Štúdium literatúry o halucináciách LLM v citáciách (Walters)
- [x] Analýza techník matchingu neúplných metadát (Guenci et al.)
- [x] Štúdium sémantického overovania tvrdení (Alvarez et al., CiteME)
- [x] Definícia technickej architektúry a cieľov práce

### 2. Dátová a praktická časť
- [ ] Zber a kurácia evaluačného datasetu (akademické pasáže + LLM citácie)
- [ ] Generovanie negatívnych vzoriek (negácií) pomocou LLM pre testovanie
- [ ] Implementácia ML parsera (GROBID) na extrakciu z hlučných dát
- [ ] Vývoj rezolučného modulu (kaskádová stratégia dopytov SPARQL)

### 3. Evaluácia a finalizácia
- [ ] Benchmarking úspešnosti extrakcie a matchingu
- [ ] Testovanie sémantického verifikátora v zero-shot režime
- [ ] Analýza limitov (jazykové bariéry, nekonzistencia rokov)
- [ ] Dopísanie textu diplomovej práce a dokumentácie

---
**Autor:** Bc. Vladimír Tischler

**Školiteľ:** Mgr. Marek Šuppa

**Pracovisko:** Katedra aplikovanej informatiky, FMFI UK
