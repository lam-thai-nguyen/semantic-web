# Copilot Instructions

## Project scope

This project builds Linked Open Data (LOD) for the movie domain using a Knowledge
Graph. Refer to [README.MD](../README.MD) and [concept.MD](../concept.MD) as the
authoritative project-scope documents.

The planned technology and data stack is:

- **Ontology:** Reuse classes and properties from [schema.org](https://schema.org/),
  including movies, people, countries, organizations, ratings, actors, directors,
  genres, production companies, publication dates, and awards.
- **Data source:** Scrape relevant movie data from TMDB (The Movie Database).
- **LOD transformation:** Convert collected CSV data into RDF in Turtle format,
  using stable URIs.
- **Dataset linking:** Link shared entities to DBpedia and Wikidata to support the
  five-star Linked Open Data standard.
- **Query interface:** Provide the data through a SPARQL endpoint using Apache
  Jena Fuseki.
- **Environment:** Use the Python interpreter from the `semantic-web` Conda
  environment and the dependencies from `requirements.txt`, as documented in
  `README.MD`.

When making implementation decisions, preserve semantic-web interoperability,
valid RDF, consistent URI design, reuse of established vocabularies, and
compatibility with SPARQL/Fuseki.

## Response formatting

- Start every answer with `🟠🟠🟠`.
- When summarizing changes made, start that paragraph or section with `🟢🟢🟢`.
- When proposing next steps, start that paragraph or section with `🟡🟡🟡`.
- Keep responses concise, explicit about uncertainty, and grounded in the project
  scope described by `README.MD` and `concept.MD`.

## Change workflow

For any requested change:

1. Inspect the relevant files and confirm how the change fits the project scope.
2. Propose the intended changes, including important implementation choices,
   affected files, and validation steps.
3. Ask the user for permission before making the change when the request is
   exploratory, ambiguous, or does not explicitly authorize implementation.
4. Execute the change only after permission is granted, or immediately when the
   user has explicitly requested implementation.
5. Validate the result with the smallest relevant project checks.
6. Summarize the changes made, beginning with `🟢🟢🟢`.
7. Propose relevant next steps based on `concept.MD`, beginning with `🟡🟡🟡`.

Do not make unrelated changes. Preserve existing user work, follow repository
conventions, and update directly related documentation when behavior or setup
changes.
