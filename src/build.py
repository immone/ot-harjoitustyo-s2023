from initialize_database import initialize_database

# Alustaa tietokannan


def build():
    initialize_database()


# Voidaan kutsua build-funktiota ulkopuolelta
if __name__ == "__main__":
    build()
