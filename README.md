# Bato.to Downloader

Ce projet est un script Python permettant de télécharger des chapitres de mangas depuis le site [Bato.to](https://bato.to), de sauvegarder les images localement, et de les convertir en fichiers CBZ.

## Fonctionnalités

- Extraction des liens de chapitres depuis une URL de série.
- Téléchargement des images de chaque chapitre.
- Création de fichiers CBZ pour chaque chapitre.

## Prérequis

- Python 3.x
- Les bibliothèques suivantes doivent être installées :
    - `requests`
    - `re` (inclus dans la bibliothèque standard)
    - `os` (inclus dans la bibliothèque standard)
    - `zipfile` (inclus dans la bibliothèque standard)

## Installation

1. Clonez ce dépôt ou copiez le script dans un fichier local.
2. Installez les dépendances nécessaires avec la commande suivante :
     ```bash
     pip install requests
     ```

## Utilisation

1. Exécutez le script Python :
     ```bash
     python script.py
     ```
2. Entrez l'URL de la série que vous souhaitez télécharger (ou laissez vide pour utiliser l'URL par défaut).
3. Le script téléchargera les chapitres et créera des fichiers CBZ dans le dossier `cbz`.

## Structure du Code

### Fonctions principales

- **`extract_href_and_b_content(url)`**  
    Extrait les liens des chapitres et leurs titres depuis une URL de série.

- **`download_images_from_chapter(url, chapter_number)`**  
    Télécharge les images d'un chapitre et les sauvegarde dans un dossier dédié.

- **`create_cbz_from_directory(directory_name)`**  
    Crée un fichier CBZ à partir des images d'un dossier.

### Flux principal

1. L'utilisateur fournit une URL de série.
2. Les chapitres sont extraits et téléchargés.
3. Les images sont converties en fichiers CBZ.

## Avertissements

- Ce script est conçu pour un usage personnel uniquement. Assurez-vous de respecter les conditions d'utilisation du site Bato.to.
- Les performances peuvent varier en fonction de la taille des chapitres et de la vitesse de votre connexion Internet.

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request pour améliorer ce projet.

## Licence

Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus d'informations.  