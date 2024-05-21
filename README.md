## Install the dependencies
```bash
pip install -r requirements.txt
```

## Run
```bash
uvicorn main:app --port 8000
```

## Explore the documentation
```
http://localhost:8000/docs
```

## Insert data 

We use GraphQL and migration approach to insert data through the DB.

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  --data '{ "query": "mutation { addTemperature(data: { value: 25, type: \"C\" }) { value } }" }' \
  http://127.0.0.1:8000/measurement 
```

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  --data '{ "query": "mutation { addResistance(data: { value: 25, type: \"C\" }) { value } }" }' \
  http://127.0.0.1:8000/measurement
```

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  --data '{ "query": "mutation { addIsolation(data: { value: 25 }) { value } }" }' \
  http://127.0.0.1:8000/measurement 
```

## GET DATA

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
  "query": "query TemperatureQuery { getAllTemperatures (where: { type: \"C\", createdAt: { startDate: \"2024-04-01T09:37\", endDate: \"2024-04-01T09:37\" }}) {id value type createdAt}}, query IsolationQuery{ getAllIsolations (where: {createdAt: {startDate: \"2024-04-01T09:53\", endDate: \"2024-04-23T09:53\"}}) {id value createdAt}}"
  }' \
  http://127.0.0.1:8000/measurement
```