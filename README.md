# Projet Minitrice - Évaluation Git

## Table des Matières
- [Introduction](#Introduction)
- [Installation](#Installation)
- [Exécution](#Exécution)
- [Remarques](#Remarques)
- [Publication](#Publication)
- [Réponses aux questions](#Réponses-aux-questions)
- [Références/Liens Utiles](#Référencesliens-utiles)

## Introduction
Ce projet consiste à créer un programme capable de réaliser les quatre opérations arithmétiques élémentaires (addition, soustraction, multiplication et division) entre deux nombres positifs. Le développement du projet est suivi avec Git, en utilisant le modèle de branches GitFlow.

## Installation

### Prérequis
- Python 3.x
- Git

### Cloner le dépôt
```
git clone https://github.com/nom-utilisateur/git-evaluation_l_kev.git
cd git-evaluation_l_kev
```

### Rendre le script exécutable

## Exécution

### Utilisation Interactive
```
./minitrice
```

Exemple :

```
$ ./minitrice
> 3 + 9
12
> exit
Fin des calculs
```
### Utilisation avec echo

```
echo "3+12" | ./minitrice
```

### Utilisation avec cat

```
cat good-expression.txt | ./minitrice
```

### Générateur d'Expressions

```
python generator.py <number_of_expressions>
```
Exemple :

```
python generator.py 5
```

### Utilisation du Générateur avec minitrice

```
python generator.py 5 | ./minitrice
```

## Réponses aux Questions

1. **Git est un gestionnaire de version décentralisé. Qu’est-ce que cela signifie ? Quel est le rôle joué par un dépôt central sur GitHub ou GitLab dans ce cas ? Justifier.**
   - Git est un gestionnaire de version décentralisé, ce qui signifie que chaque utilisateur possède une copie complète de l'historique de version du dépôt, ce qui permet de travailler hors ligne et de fusionner les modifications de manière décentralisée. Un dépôt central sur GitHub ou GitLab agit comme un point de synchronisation où les utilisateurs peuvent pousser leurs modifications et récupérer celles des autres, facilitant la collaboration.

2. **À quoi sert la commande `git fetch -p` ?**
   - La commande `git fetch -p` (ou `git fetch --prune`) sert à synchroniser les branches locales avec le dépôt distant en supprimant les branches locales qui n'existent plus sur le dépôt distant.

3. **Dans quelles conditions est-ce qu’un conflit apparaît avec git ?**
   - Un conflit apparaît lorsque deux utilisateurs modifient les mêmes lignes d'un fichier ou des parties incompatibles du projet, et que Git ne peut pas fusionner automatiquement ces modifications.

4. **Lorsque vous résolvez un conflit, quelle est la dernière commande git que vous devez exécuter ?**
   - La dernière commande à exécuter après avoir résolu un conflit est `git commit` pour valider la résolution des conflits.

5. **Depuis GitHub, après avoir accepté une contribution sur la branche principale, que devez vous faire pour mettre à jour votre branche principale localement ?**
   - Vous devez exécuter la commande `git pull origin main` pour mettre à jour votre branche principale locale avec les modifications acceptées sur GitHub.

6. **Quelle est la différence entre les commandes `git reset --soft` et `git reset --hard` ? Donner un cas d’usage pratique et courant pour chacune de ces commandes.**
   - `git reset --soft` : Réinitialise l'index mais préserve les modifications dans le répertoire de travail. Utilisé pour modifier le dernier commit sans perdre les modifications.
   - `git reset --hard` : Réinitialise l'index et le répertoire de travail. Utilisé pour annuler des modifications non désirées et revenir à un état propre.

7. **Quelle est la (ou les) commande à exécuter pour transformer les commits 9f64652 et 68cd016 en un seul commit avec un nouveau message ?**
   - Utilisez la commande `git rebase -i HEAD~2`, puis combinez (squash) les deux commits et modifiez le message du commit.

8. **Pourquoi est-il déconseillé de rebase une branche publique (branche sur laquelle travaille aussi d’autres personnes) ?**
   - Il est déconseillé de rebase une branche publique car cela réécrit l'historique des commits, ce qui peut créer des incohérences et des conflits pour les autres développeurs travaillant sur la même branche.
