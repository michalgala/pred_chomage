# Toy project MLOps

### Run the project in dev mode

```
docker-compose up
```

### Run jupyter

from the docker terminal run

```
poetry run jupyter notebook
```

or

```
poetry run jupyter lab
```

:warning: git ignore the exploratory notebooks, push the refined ones

### Add a new dev dependency

From the docker terminal

```
poetry add -D pandas
```

### Add a new prod dependency

From the docker terminal

```
poetry add pandas
```

# TODO

- [ ] Vérifier que les ajouts de dependency sont bien pushé sur github dans le .toml