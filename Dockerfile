# https://medium.com/@harpalsahota/dockerizing-python-poetry-applications-1aa3acb76287
# https://betterprogramming.pub/python-fastapi-kubernetes-gcp-296e0dc3abb6
# docker build -t pred_chomage_img -f Dockerfile .
FROM python:3.8-slim

RUN mkdir /app
COPY /src /app
COPY pyproject.toml /app

WORKDIR /app
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# expose port
EXPOSE 8000

# second item file:FastAPI_class
CMD ["uvicorn", "api:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
