import argparse

from owlrl import DeductiveClosure, OWLRL_Semantics
from rdflib import Graph
from tabulate import tabulate


def main():
    parser = argparse.ArgumentParser(description="Interactive SPARQL CLI using rdflib")
    parser.add_argument("--rdf-file", help="Path to RDF file", default="output/movies.ttl")
    parser.add_argument("--ontology-file", help="Path to OWL ontology", default="ontology.owl")
    parser.add_argument("-q", "--query", help="Run a single query and exit (non-interactive)")
    parser.add_argument("-Q", "--query-file", help="Path to a file containing a SPARQL query")
    parser.add_argument(
        "--no-reasoning",
        action="store_true",
        help="Skip OWL-RL inference",
    )
    args = parser.parse_args()

    g = Graph()
    g.parse(args.rdf_file, format="turtle")
    g.parse(args.ontology_file, format="turtle")

    if not args.no_reasoning:
        DeductiveClosure(OWLRL_Semantics).expand(g)

    query = args.query
    if args.query_file:
        with open(args.query_file, encoding="utf-8") as f:
            query = f.read()

    if query:
        results = g.query(query)
        headers = [str(v) for v in results.vars] if results.vars else []
        print(tabulate(list(results), headers=headers, tablefmt="simple"))
        return

if __name__ == "__main__":
    main()
