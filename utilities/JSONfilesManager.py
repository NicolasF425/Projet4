import json


def to_file(object, filename):
    try:
        with open(filename, "w") as file:
            json.dump(object.to_dict(), file, indent=4)
            print(f"Sauvegarde effectuee dans {filename}")
    except Exception as e:
        print(f"Erreur de sauvegarde : {e}")
