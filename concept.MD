# Conceptualization for Movie Knowledge Graph

## 1) Define an ontology for the selected domain

Reusing classes and properties from https://schema.org/.
- Classes: `schema:Movie`, `schema:Person`, `schema:Country`, `schema:Organization`, `schema:Rating`.
- Properties: `schema:actor`, `schema:countryOfOrigin`, `schema:director`, `schema:duration`, `schema:productionCompany`, `schema:about`, `schema:abstract`, `schema:genre`, `schema:name`, `schema:datePublished`, `schema:award`.

## 2) Collect relevant data for this domain

- Scrape from TMDB (The Movie Database)

## 3) Transform collected data into 4* standard

- Transform raw data (CSV) into RDF (Turtle) using URIs 

## 4) Find and establish links to other datasets to obtain 5* standard

- Link to DBpedia, Wikidata for shared entities

## 5) Provide an interface via SPARQL endpoint to query the data

- Set up a SPARQL endpoint via Apache Jena Fuseki