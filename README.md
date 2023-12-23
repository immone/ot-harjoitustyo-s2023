# Algebra-app

## [Release 1](https://github.com/immone/ot-harjoitustyo-s2023/releases/tag/viikko6)

Sovelluksen avulla käyttäjän on mahdollista kerrata abstraktin algebran taitojaan, esimerkiksi ennen tenttiä. Sovelluksessa on mahdollista valita kysymyksien vaativuustaso ja aihealue.

## Dokumentaatio
### [Käyttöohje](https://github.com/immone/ot-harjoitustyo-s2023/blob/master/dokumentaatio/kayttoohje.md)
### [Tuntikirjanpito](https://github.com/immone/ot-harjoitustyo-s2023/blob/master/dokumentaatio/tuntikirjanpito.md)
### [Vaatimusmäärittely](https://github.com/immone/ot-harjoitustyo-s2023/blob/master/dokumentaatio/vaatimusmaarittely.md)
### [Changelog](https://github.com/immone/ot-harjoitustyo-s2023/blob/master/dokumentaatio/changelog.md)
### [Arkkitehtuurikuvaus](https://github.com/immone/ot-harjoitustyo-s2023/blob/master/dokumentaatio/arkkitehtuuri.md)

## Asennus
1. Asenna riippuvuudet komennolla
```bash
poetry install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

Testikattavuuden generointi tapahtuu komennolla 

```bash
poetry run invoke coverage html
```

ja projektin linttaus komennolla

```bash
poetry run pylint src
```