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

The `tmdb.py` script collects movie data from The Movie Database (TMDB) and
writes the results as CSV files in the `data/` directory. It retrieves popular
movies, movie details, genres, production companies, countries, languages, the
top five cast members, and directors.

Before running the script, configure a valid TMDB API key in `tmdb.py`. The
number of popular-movie pages to collect can be changed through the `PAGES`
setting in the same file.

Run the data collection script from the project root:

```bash
python tmdb.py
```

The generated files include `movies.csv`, `cast.csv`, `crew.csv`, entity
lookup files such as `genres.csv` and `companies.csv`, and relationship files
such as `movie_genres.csv` and `movie_companies.csv`.

## Transform CSV data into RDF

The CSV files in `data/` can be transformed into a consolidated Turtle graph:

```bash
python transform.py --base-uri https://example.org/
```

The default output is `output/movies.ttl`. Entity identifiers become stable URI
paths (`movie`, `person`, `company`, `country`, `genre`, and `language`), while
descriptive, date, numeric, and ranking fields become typed literals. The
relationship CSV files create URI-to-URI links such as `schema:actor`,
`schema:genre`, `schema:productionCompany`, `schema:countryOfOrigin`, and
`schema:inLanguage`.

## Query the RDF file from the command line

After generating `output/movies.ttl`, you can run a SPARQL query from the provided example `queries/`

```bash
python queries.py -Q queries/1.sparql
```

Replace `queries/1.sparql` with any query file in the table below. The command
loads the local Turtle graph, executes the query, and prints each result row as
tab-separated values.

| File | Question |
| --- | --- |
| `queries/1.sparql` | List 10 people |
| `queries/2.sparql` | List 10 movies |
| `queries/3.sparql` | List 10 actors for Spider-Man: Brand New Day movie |
| `queries/4.sparql` | What is the basic information of a movie? |
| `queries/5.sparql` | List 20 highest-rated movies |
| `queries/6.sparql` | Which movies were released before 2026? |
| `queries/7.sparql` | Which Adventure movies were released in 2026? |
| `queries/8.sparql` | Which Adventure movies were released in 2026 that starred Tom Holland? |
| `queries/9.sparql` | Which actors have worked with Tom Holland in more than 2 movies? |
| `queries/10.sparql` | Which movies has Tom Holland starred in? |
| `queries/11.sparql` | Which movies has Christopher Nolan directed? |
