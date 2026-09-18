import argparse

from rdflib import Graph
from tabulate import tabulate


def main():
    parser = argparse.ArgumentParser(description="Interactive SPARQL CLI using rdflib")
    parser.add_argument("--rdf-file", help="Path to RDF file", default="output/movies.ttl")
    parser.add_argument("-q", "--query", help="Run a single query and exit (non-interactive)")
    parser.add_argument("-Q", "--query-file", help="Path to a file containing a SPARQL query")
    args = parser.parse_args()

    g = Graph()
    g.parse(args.rdf_file, format="turtle")

    query = args.query
    if args.query_file:
        with open(args.query_file) as f:
            query = f.read()

    if query:
        results = g.query(query)
        headers = [str(v) for v in results.vars] if results.vars else []
        print(tabulate(list(results), headers=headers, tablefmt="simple"))
        return

if __name__ == "__main__":
    main()
