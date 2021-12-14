
FROM python:3.8.12-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock",  "./"]

RUN pipenv install --system --deploy

COPY ["prediction_regression_project.py", "best_model.pkl", "poly.pkl", "scalar.pkl", "./"]

EXPOSE 9696

ENTRYPOINT ["waitress-serve", "--listen=0.0.0.0:9696", "app:app"]