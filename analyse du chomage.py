"""
Analyse du chomage au Maroc - Import, nettoyage et visualisation
Sources officielles :
  - HCP (Haut-Commissariat au Plan) : notes d'information annuelles sur la
    situation du marche du travail (feuille "HCP_national")
  - Banque Mondiale (World Bank Open Data), indicateur SL.UEM.TOTL.ZS,
    "Unemployment, total (% of total labor force) (modeled ILO estimate)"
    (feuille "WorldBank_modele_OIT")
    Telechargement officiel direct (CSV/XML/EXCEL) :
    https://api.worldbank.org/v2/en/indicator/SL.UEM.TOTL.ZS?downloadformat=csv

A executer dans VS Code (ou en ligne de commande) :
    pip install pandas matplotlib openpyxl
    python analyse_chomage.py

Fichier de donnees attendu dans le meme dossier : chomage_maroc_officiel.xlsx
"""

import pandas as pd
import matplotlib.pyplot as plt

FICHIER = "chomage_maroc_officiel.xlsx"

# ---------------------------------------------------------------
# 1. IMPORT
# ---------------------------------------------------------------
hcp = pd.read_excel(FICHIER, sheet_name="HCP_national")
wb = pd.read_excel(FICHIER, sheet_name="WorldBank_modele_OIT")

# ---------------------------------------------------------------
# 2. NETTOYAGE
# ---------------------------------------------------------------
# - types numeriques corrects
# - suppression d'eventuels doublons
# - les valeurs manquantes (annees ou le detail jeunes/diplomes n'a pas
#   ete publie par le HCP) sont laissees en NaN plutot que comblees
#   artificiellement, pour ne pas fausser l'analyse.
for df in (hcp, wb):
    df["annee"] = df["annee"].astype(int)
    df.drop_duplicates(subset="annee", inplace=True)
    df.sort_values("annee", inplace=True)

print("=== HCP (donnees officielles nationales) ===")
print(hcp[["annee", "taux_national_pct", "taux_jeunes_15_24_pct", "taux_diplomes_pct"]])
print("\nValeurs manquantes par colonne (HCP) :")
print(hcp.isna().sum())

print("\n=== Banque Mondiale (estimation modelisee OIT, comparabilite internationale) ===")
print(wb[["annee", "taux_chomage_total_modelise_oit_pct"]].tail(10))

# ---------------------------------------------------------------
# 3. GRAPHIQUE 1 : long terme (2000-2025) - Banque Mondiale
# ---------------------------------------------------------------
plt.figure(figsize=(10, 5))
plt.plot(wb["annee"], wb["taux_chomage_total_modelise_oit_pct"], marker="o", color="darkred")
plt.axvspan(2019.5, 2020.5, color="grey", alpha=0.2, label="Choc Covid-19 / secheresse")
plt.title("Maroc : taux de chomage 2000-2025 (estimation modelisee OIT, Banque Mondiale)")
plt.xlabel("Annee")
plt.ylabel("Taux de chomage (%)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("graphique_1_tendance_longue_worldbank.png", dpi=150)
plt.close()

# ---------------------------------------------------------------
# 4. GRAPHIQUE 2 : comparaison des deux sources sur la periode commune
# ---------------------------------------------------------------
commun = pd.merge(
    hcp[["annee", "taux_national_pct"]],
    wb[["annee", "taux_chomage_total_modelise_oit_pct"]],
    on="annee", how="inner",
)
plt.figure(figsize=(9, 5))
plt.plot(commun["annee"], commun["taux_national_pct"], marker="o", label="HCP (enquete nationale, officiel)")
plt.plot(commun["annee"], commun["taux_chomage_total_modelise_oit_pct"], marker="o",
         label="Banque Mondiale (estimation modelisee OIT)")
plt.title("Maroc : deux methodologies, deux niveaux de chomage (2019-2025)")
plt.xlabel("Annee")
plt.ylabel("Taux de chomage (%)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("graphique_2_comparaison_sources.png", dpi=150)
plt.close()

# ---------------------------------------------------------------
# 5. GRAPHIQUE 3 : chomage des jeunes vs national (HCP, annees disponibles)
# ---------------------------------------------------------------
hcp_jeunes = hcp.dropna(subset=["taux_jeunes_15_24_pct", "taux_diplomes_pct"])
largeur = 0.25
x = range(len(hcp_jeunes))
plt.figure(figsize=(9, 5))
plt.bar([i - largeur for i in x], hcp_jeunes["taux_national_pct"], width=largeur, label="National")
plt.bar(x, hcp_jeunes["taux_jeunes_15_24_pct"], width=largeur, label="Jeunes 15-24 ans")
plt.bar([i + largeur for i in x], hcp_jeunes["taux_diplomes_pct"], width=largeur, label="Diplomes")
plt.xticks(list(x), hcp_jeunes["annee"])
plt.title("Maroc (HCP) : chomage national vs jeunes vs diplomes")
plt.xlabel("Annee")
plt.ylabel("Taux de chomage (%)")
plt.legend()
plt.grid(True, axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("graphique_3_jeunes_diplomes.png", dpi=150)
plt.close()

print("\nGraphiques generes :")
print(" - graphique_1_tendance_longue_worldbank.png")
print(" - graphique_2_comparaison_sources.png")
print(" - graphique_3_jeunes_diplomes.png")
