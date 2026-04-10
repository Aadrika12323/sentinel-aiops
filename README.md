# Sentinel-AIOps

A Flask-based API that analyzes server logs and suggests solutions using TF-IDF similarity.

## Features
- Log analysis using ML
- REST API
- MySQL logging
- Postman tested

## Endpoint

POST /analyze

{
  "log": "out of memory error"
}

## Tech Stack
- Python
- Flask
- Scikit-learn
- MySQL