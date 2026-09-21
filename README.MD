# Linked Open Data Application using Movie Knowledge Graph

## Conceptualization

Refer to [concept.MD](concept.MD)

## Set up environment

Use miniconda to set up the environment as follows:

```bash
conda create -n semantic-web python=3.14.7
conda activate semantic-web
pip install -r requirements.txt
```

## Collect data from TMDB

Get an API Key from https://www.themoviedb.org/, then store it as an environment variable. On Windows Powershell, run:

```powershell
$env:TMDB_API_KEY = "your-tmdb-api-key"
```

To collect the data, run:

```bash
python tmdb.py
```

The generated files include `movies.csv`, `cast.csv`, `crew.csv`, entity lookup files such as `genres.csv` and `companies.csv`, and relationship files such as `movie_genres.csv` and `movie_companies.csv`.

## Transform CSV data into RDF

To transform table data into RDF triples (Turtle notation), run:

```bash
python transform.py
```

Output: `output/movies.ttl`

## Build an ontology using OWL

To enable deduction (ie making new facts using logic), we need to add constraints on top of RDF triples by writing `./ontology.owl`. Then, we use `owlrl` package for SPARQL reasoning.

Output: `./ontology.owl` (manually written)

## Query the RDF file from the command line

After generating `output/movies.ttl` and building `./ontology.owl`, you can run a SPARQL query from the provided example `queries/`

```bash
python queries.py -Q queries/1.sparql
```

| File (queries/) | Target question | Requires Deduction | KG Expressiveness |
| :---: | --- | :---: | :---: |
| 1.sparql | List 20 movies | o | ⭐ |
| 2.sparql | List 20 actors | o | ⭐ |
| 3.sparql | List 20 directors | o | ⭐ |
| 4.sparql | List 5 actors for "Spider-Man: Brand New Day" the movie | o | ⭐ |
| 5.sparql | What is the basic information of "The Odyssey" the movie? | o | ⭐ |
| 6.sparql | List 20 highest-rated movies | o | ⭐⭐ |
| 7.sparql | List 20 highest-rated "Action" movies | o | ⭐⭐ |
| 8.sparql | List 20 highest-rated "Action" movies since 2020 | o | ⭐⭐ |
| 9.sparql | List 20 highest-rated "Action" movies since 2020 that starred Tom Holland | o | ⭐⭐ |
| 10.sparql | List 20 actors that have worked with Tom Holland in more than 1 movie | o | ⭐⭐ |
