# MLOps





## Poetry

Poetry est un outil de gestion des dépendances python.
Il reprend les fonctionnalités d'outils comme npm, yarn, qui manquaient à pip.
Poetry est une construit à partir de pip, et rajoute une couche de fonctionnalités.

```bash
poetry new pred_chomage #créer un nouveau projet
cd pred_chomage 
poetry install #créer l'environnement virtuel
poetry add pandas
poetry remove pandas
poetry add pandas
poetry show
poetry show --tree
```

### Fonctionnalités

#### Poetry permet la cohabitation de plusieurs versions d'une même librairies

exemple: Imaginons un projet de deep learning, qui utilise une certaine version de pandas, et de PIL. Lors de l'installation d'une librairie comme PyTorch qui intègre aussi PIL et pandas il peut y avoir des conflits entre les versions. PyTorch qui nécessite une version plus récente de pandas, et une autre librairie qu'on utilise qui va générer un conflit;

![image-20220721143232348](/home/michal/.config/Typora/typora-user-images/image-20220721143232348.png)

On voit sur cette capture d'écran l'organisation en librairies et sous-librairies

### Environnement de dev et  de prod avec un unique fichier de config

![image-20220721143623792](/home/michal/.config/Typora/typora-user-images/image-20220721143623792.png)

#### Plus de détails sur l'environnement

![image-20220721143644795](/home/michal/.config/Typora/typora-user-images/image-20220721143644795.png)