---
layout: default
title: Travel
parent: Lab Basics
nav_order: 9
---

# Dienstreise

- [Dienstreiseantrag](https://www.uni-bamberg.de/fileadmin/abt-personal/Homepage_ab_2016-03/11_Formulare_Infos_Merkblaetter/Reisekosten/Antrag_auf_Genehmigung_einer_Dienstreise.pdf)

```mermaid
sequenceDiagram
    Professor->>+Reisekostenstelle: Antrag auf Genehmigung einer Dienstreise
    Reisekostenstelle->>+Professor: Genehmigter Antrag
    Note over Professor: Buchen
    Note over Professor: Konferenz (Rechnungen)
    Professor->>+Reisekostenstelle: Reisekostenabrechnung (inkl. Rechnungen und Antrag)
    Reisekostenstelle->>+Professor: Erstattung

```