**Auteur :** [Zainab Merzouk]
**Date :** [27/09/2026]
# Pourquoi le taux de chômage augmente-t-il sans cesse au Maroc ?

**Analyse basée sur deux jeux de données officiels : HCP (Haut-Commissariat au Plan) et Banque Mondiale (World Bank Open Data, estimation modélisée OIT)**

## 1. Deux sources, deux chiffres : un premier résultat d'analyse

Le fichier `chomage_maroc_officiel.xlsx` contient deux feuilles :

- **HCP_national** : taux de chômage officiel du Maroc (enquête nationale sur l'emploi), 2019-2025.
- **WorldBank_modele_OIT** : indicateur `SL.UEM.TOTL.ZS` de la Banque Mondiale, "Unemployment, total (% of total labor force) (modeled ILO estimate)", 2000-2025 — une estimation modélisée par le Bureau International du Travail à des fins de comparaison internationale.

| Année | HCP (officiel, %) | Banque Mondiale (modélisé OIT, %) |
|-------|--------------------|-------------------------------------|
| 2019  | 9,2                | 9,2 |
| 2020  | 11,9               | 11,2 |
| 2021  | 12,3               | 10,6 |
| 2022  | 11,8               | 9,4 |
| 2023  | 13,0               | 8,9 |
| 2024  | 13,3               | 9,1 |
| 2025  | 13,0               | 9,0 |

Les deux séries partent du même point en 2019 puis divergent fortement à partir de 2021 : le HCP montre un chômage qui reste au-dessus de 11-13 %, alors que l'estimation modélisée de la Banque Mondiale redescend vers 9 %. Ce n'est pas une contradiction mais une **différence de méthodologie** : l'enquête HCP mesure directement la population active au Maroc selon les définitions nationales, tandis que l'estimation de la Banque Mondiale est un modèle statistique de l'OIT ajusté pour la comparabilité entre pays (il lisse notamment les à-coups conjoncturels). Un rapport rigoureux doit signaler cet écart plutôt que de le passer sous silence — c'est en soi une leçon méthodologique sur l'usage des statistiques internationales.

## 2. Ce que montre le graphique long terme (2000-2025, Banque Mondiale)

Sur 25 ans, le taux de chômage marocain (mesure modélisée) suit une tendance baissière de 13,6 % (2000) à environ 9 % (2018), avec un point bas à 8,9 % en 2011 et en 2023. Le choc de 2020 (11,2 %) casse cette tendance : c'est la **conjonction de la pandémie de Covid-19 et d'une campagne agricole sèche** qui a entraîné la destruction d'environ 432 000 postes d'emploi selon le HCP. Depuis, le niveau ne revient que partiellement à la normale.

## 3. Ce que montrent les données HCP (2019-2025) : la vraie hausse est structurelle et sélective

Le taux national du HCP n'augmente pas de façon strictement continue (baisse en 2021-2022, puis en 2025), mais il reste **durablement plus élevé qu'avant 2020**. Surtout, deux catégories concentrent la hausse presque sans interruption :

- **Jeunes (15-24 ans)** : 31,2 % (2020) → 32,7 % (2022) → 36,7 % (2024) → 37,2 % (2025).
- **Diplômés** : 18,5 % (2020) → 18,6 % (2022) → 19,6 % (2024) → 19,1 % (2025), contre 4-5 % pour les personnes sans diplôme.

C'est cette dynamique — un chômage des jeunes et des diplômés qui progresse presque chaque année — qui nourrit la perception d'un chômage "qui ne cesse d'augmenter", plus qu'une hausse mécanique du taux global.

## 4. Les causes principales

**a) Une croissance trop faible et trop instable pour absorber la population active.**
Le rebond après 2020 n'a pas suffi à compenser les pertes d'emploi, d'autant que le Maroc a enchaîné plusieurs années de sécheresse.

**b) La vulnérabilité du secteur agricole.**
L'agriculture reste une source majeure d'emplois (souvent non rémunérés), très sensible à la pluviométrie ; ses pertes de postes (ex. -247 000 postes entre T1-2022 et T1-2023) ne sont pas compensées par les autres secteurs.

**c) L'inadéquation formation-emploi.**
Le chômage des diplômés (environ 19 %) reste presque 4 à 5 fois supérieur à celui des non-diplômés : les filières de formation ne correspondent pas toujours aux besoins des entreprises, ce qui allonge la durée moyenne de recherche d'emploi (31 à 33 mois entre 2024 et 2025, HCP).

**d) Un chômage des jeunes structurellement très élevé.**
Plus d'un jeune actif sur trois est au chômage en 2025 (37,2 %). Le HCP note qu'en 2025, 52,9 % des chômeurs n'ont jamais travaillé (primo-demandeurs), contre 49,3 % un an plus tôt.

**e) Le poids de l'emploi informel et non rémunéré.**
Une partie des créations d'emploi correspond à de l'emploi non rémunéré ou précaire, qui n'offre pas de sécurité durable aux nouveaux arrivants sur le marché du travail.

## 5. Conclusion

Le chômage marocain ne progresse pas de façon strictement linéaire selon les chiffres officiels du HCP, et l'estimation internationale de la Banque Mondiale suggère même une légère amélioration depuis 2020. Mais ces deux lectures s'accordent sur un point : le marché du travail marocain reste fragile, très dépendant de la pluviométrie, et concentre un chômage massif chez les jeunes et les diplômés. Une amélioration durable suppose une diversification économique moins dépendante de l'agriculture pluviale et un meilleur arrimage entre les formations et les besoins du marché du travail.

## 6. Sources et fichiers de données

**HCP (Haut-Commissariat au Plan)** — source primaire pour la définition nationale du chômage :
- Note d'information relative à la situation du marché du travail en 2025 (PDF officiel) : https://www.hcp.ma/file/247824/
- Note d'information relative à la situation du marché du travail en 2023 (PDF officiel) : https://hcp.ma/file/242461
- Portail des publications HCP : https://www.hcp.ma

**Banque Mondiale (World Bank Open Data)** — source pour la comparabilité internationale :
- Page de l'indicateur : https://data.worldbank.org/indicator/SL.UEM.TOTL.ZS
- Téléchargement officiel direct (CSV/XML/Excel) : https://api.worldbank.org/v2/en/indicator/SL.UEM.TOTL.ZS?downloadformat=csv

**Fichiers de données joints** :
- `chomage_maroc_officiel.xlsx` (2 feuilles : HCP_national, WorldBank_modele_OIT)
- `chomage_maroc_hcp.csv` et `chomage_maroc_worldbank.csv` (versions CSV séparées des deux feuilles)

**Remarque méthodologique pour le prof** : le HCP ne publie ses données que sous forme de notes PDF (pas de fichier CSV/Excel en libre accès sur son site) ; les chiffres du HCP dans ce fichier ont donc été retranscrits manuellement à partir de ces notes officielles, avec le lien exact vers chaque note en colonne `source`. Les données de la Banque Mondiale, elles, sont téléchargeables directement en CSV/Excel depuis le lien ci-dessus.
