# Airflow Studies

<img src="https://img.shields.io/badge/python-3.10.2-blue"/> <img src="https://img.shields.io/badge/airflow-2.5.1-blue">

## 1. Description

The objective of this repository is to gather DAGs I've created in order to study Airflow and its operators.


## 2. Installation

If you want to run any of the examples, you can clone this repository using the code below: 

```
git clone https://github.com/camila-marquess/estudos-airflow.git
```

Before running Airflow, make sure you have installed docker in your OS. If you do not, follow this steps based on your OS: [Installing Docker Compose](https://docs.docker.com/desktop/install/windows-install/).

In order to start Airflow you have to run: 

```
docker-compose up -d
```

Then you can visualize the Airflow UI by accessing `localhost:8080` on your browser. The default login and password are: `airflow`.

In order to stop the containers, you can run: 

```
docker-compose down
```
