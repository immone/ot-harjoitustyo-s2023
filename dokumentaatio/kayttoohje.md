# Käyttöohje

Lataa projektin viimeisimmän [releasen](https://github.com/immone/ot-harjoitustyo-s2023/releases) lähdekoodi valitsemalla _Assets_-osion alta _Source code_.

## Konfigurointi

Tallennukseen käytettävien tiedostojen nimiä voi halutessaan konfiguroida käynnistyshakemistossa _.env_-tiedostossa. Tiedostot luodaan automaattisesti _data_-hakemistoon, jos niitä ei siellä vielä ole. Tiedoston muoto on seuraava:

```
EXERCISES_FILENAME=exercises.json
DATABASE_FILENAME=database.sqlite
```

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:

```bash
poetry install
```

Jonka jälkeen suorita alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

Nyt ohjelman voi käynnistää komennolla:

```
poetry run invoke start
```

## Uuden käyttäjän luominen

Kirjautumisnäkymästä on mahdollista siirtyä uuden käyttäjän luomisnäkymään panikkeella "Create user" ja antamalla käyttäjätunnuksen sekä salasanan.

## Vaikeustason valitseminen

Seuraavassa käyttöliittymässä valitaan tehtävien vaikeustaso.
Annetussa tietokannassa on vain helpon tason kysymys, valitse siis "Easy" ja paina "Choose difficulty".

## Tehtävätyyppien valitseminen

Avautuvassa käyttöliittymässä valitaan tehtävien tyyppi.
Annetussa tietokannassa on vain ryhmäteorian määritelmäkysymys, valitse siis "Group" ja "Definition".

## Tehtävien tekeminen

Voit valita avautuvassa käyttöliitttymässä halutun kertaustehtävän. Paina "Choose", jolloin se aukeaa uuteen ikkunaan.

## Tehtävän vastaaminen
Valitse vastausvaihtoehto ja vastaa, jolloin uusi ikkuna antaa palautteen.
