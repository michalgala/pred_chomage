# Toy project MLOps

### Run the project in dev mode

```bash
docker-compose up
```

### Run jupyter

from the docker terminal run

```bash
poetry run jupyter notebook --ip 0.0.0.0 --allow-root
```

or

```bash
poetry run jupyter lab --ip 0.0.0.0 --allow-root
```

:warning: git ignore the exploratory notebooks, push the refined ones

### Add a new dev dependency

From the docker terminal

```bash
poetry add -D pandas
```

### Add a new prod dependency

From the docker terminal

```bash
poetry add pandas
```

### Query endpoint

- demo endpoint

- request by post

- returns a jsonified DataFrame: 

  ```python
  df.to_json(orient="records")
  ```

  

```http
http://localhost:8000/return_df/5
```



# TODO

- [ ] Vérifier que les ajouts de dependency sont bien pushé sur github (contenu de pyproject.toml et poetry.lock)
- [ ] Faire tourner l'environnement de dev dans docker-compose et prod dans le Dockerfile
- [ ] ajouter un volume pour les notebooks