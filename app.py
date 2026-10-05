import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

figure.write_html('ventes-par-region.html')
print('ventes-par-région.html généré avec succès !')

# Partie 6
données['ca'] = données['prix'] * données['qte']

stats_6_a = données.groupby('produit').agg(
    ca_moyenne=('ca', 'mean'),
    ca_mediane=('ca', 'median'),
    volume_moyenne=('qte', 'mean'),
    volume_mediane=('qte', 'median'),
)

print('6 a: moyenne et médiane des CA et volume par produit :')
print(stats_6_a)

stats_6_b = données.groupby('produit').agg(
    volume_ecart_type=('qte', 'std'),
    volume_variance=('qte', 'var'),
)

print('6 b: écart-type et variance du volume par produit :')
print(stats_6_b)

# Partie 7
ventes = données[['produit', 'qte']].values.tolist()

qte_par_produit = {}
for produit, qte in ventes:
    if produit in qte_par_produit:
        qte_par_produit[produit] += qte
    else:
        qte_par_produit[produit] = qte

plus_vendu = max(qte_par_produit, key=qte_par_produit.get)
moins_vendu = min(qte_par_produit, key=qte_par_produit.get)

print('7: Quantités min et max vendues pour les produits :')
print(f'Produit le plus vendu : {plus_vendu} ({qte_par_produit[plus_vendu]} unités)')
print(f'Produit le moins vendu : {moins_vendu} ({qte_par_produit[moins_vendu]} unités)')

# Patrie 8
totaux = données.groupby('produit', as_index=False)[['qte', 'ca']].sum()

figure = px.bar(totaux, x='produit', y='qte', title='quantité vendue par produit')
figure.write_html('ventes-par-produit.html')
print('\nventes-par-produit.html généré avec succès !')

figure = px.bar(totaux, x='produit', y='ca', title="chiffre d'affaires par produit")
figure.write_html('ca-par-produit.html')
print('ca-par-produit.html généré avec succès !')
