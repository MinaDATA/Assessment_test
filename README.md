# Test d’évaluation candidature Data Engineer spécialisé en web scraping

## Section 1: Extraction de données de comptes Twitter sans utiliser l'API de Twitter
Objectif: Le candidat doit être en mesure de récupérer des données de plusieurs comptes Twitter et suivre l’évolution des métriques liées dans le temps en utilisant des techniques de web scraping. Les données à récupérer sont les suivantes:
- Le contenu des tweets (texte, média, liens, documents, hashtag) en définissant le type de média.
- Les métriques d’un compte Twitter: nombre de followers et son évolution sur 7 jours.
- Les métriques d’un tweet: un suivi sur 7 jours pour le nombre de likes, de retweets et de partages.

Exercice pratique: décrire la stratégie d’attaque et la détailler étape par étape, en expliquant les outils/bibliothèques utilisées.

## Section 2: Web Scraping et traitement de données

Objectif: Le candidat doit être en mesure de récupérer des données de plusieurs sources web, les nettoyer, les structurer de manière homogène, les analyser et suivre les changements dans le temps.

1. **Extraction de données**: élaborez un script Python pour extraire les données des pages web ci-dessous:
   - [https://www.creditmutuel.fr/fr/particuliers/epargne/livret-de-developpement-durable.html](https://www.creditmutuel.fr/fr/particuliers/epargne/livret-de-developpement-durable.html)
   - [https://www.monabanq.com/fr/produits-bancaires/livret-developpement-durable/en-resume.html](https://www.monabanq.com/fr/produits-bancaires/livret-developpement-durable/en-resume.html)
   - [https://www.banquepopulaire.fr/bpaura/epargner/livret-transition-energetique/](https://www.banquepopulaire.fr/bpaura/epargner/livret-transition-energetique/)

2. **Création d'APIs/Web Services**: créez une API simple ou un web service en Python qui renvoie les données extraites et nettoyées sous forme de JSON. Le candidat doit démontrer une compréhension approfondie des principes RESTful et être capable de concevoir une API bien structurée et documentée.

3. **Base de données NoSQL**: proposez un schéma pour une base de données NoSQL (comme RavenDB) qui stocke les données extraites. Il doit être capable de démontrer comment il importerait les données dans cette base de données et comment il utiliserait cette base de données pour servir les données via l'API qu'il a créée.

4. **Git et Collaboration**: fournissez le code de l'exercice via un référentiel GitHub, démontrant ainsi sa compréhension des principes de versioning avec Git.

NB: Veuillez mettre la réponse à la question 3 de la Section 2 et la Section 1 dans un fichier PDF/Word et l’inclure au dépôt Github.
