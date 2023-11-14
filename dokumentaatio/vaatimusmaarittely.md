# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjän on mahdollista kerrata abstraktin algebran taitojaan, 
esimerkiksi ennen tenttiä. Sovelluksessa on mahdollista valita
kysymyksien vaativuustaso ja aihealue.

## Käyttöliittymäluonnos

Sovellus koostuu kolmesta näkymästä: ensimmäinen näkymä mahdollistaa
sallii käyttäjän vaikuttaa tehtävien tasoon, toisessa näkymässä
voi spesifioida kysymyksien aihetta ja viimeisessä näkymässä käyttäjä
pääsee tekemään tehtäviä.

## Perusversion tarjoama toiminnallisuus

## Käynnistyksen yhteydessä
- Käyttäjä voi valita kahdesta vaikeustasosta (helppo/vaikea)
- Valittuaan vaikeustason käyttäjä siirtyy tehtävien valintaan

## Tehtävien valinta
- Käyttäjä pystyy valitsemaan minkä aihealueen kysymyksiin haluaisi
vastata: esimerkiksi ryhmät, renkaat, kunnat ja niin edelleen. 
- Lisäksi käyttäjä voi valita minkälaisiin kysymyksiin hän haluaisi 
vastata: pelkästään määritelmien kertaamisiin, ongelmiin vai
teoreemien kertaamiseen.
- Löydettyään sopivan aihealueen käyttäjä siirtyy itse tehtävien tekemiseen.

## Tehtävien tekeminen
- Tehtävätyypistä riippuen käyttäjä voi vastata joko monivalinnalla
tai syöttää vastauksen suoraan alueelle, mistä tarkastetaan sen oikeus ja 
annetaan käyttäjälle palautetta.
- Käyttäjällä on mahdollisuus palata edelliseen näkymään, mikäli hän
haluaisi vaihtaa tehtävätyyppiä tai -aihetta.

## Jatkokehitysideoita
- Kuinka implementoida eri tehtävätyyppien vastaaminen järkevästi:
esimerkiksi riittääkö pelkät monivalinnat vai onko järkevää lisätä 
vastauslaatikko?

