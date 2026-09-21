import argparse
import time

from owlrl import DeductiveClosure, OWLRL_Semantics
from rdflib import Graph
from tabulate import tabulate


def main():
    parser = argparse.ArgumentParser(description="Interactive SPARQL CLI using rdflib")
    parser.add_argument("--rdf", help="Path to RDF file", default="output/movies.ttl")
    parser.add_argument("--ontology", help="Path to OWL ontology", default="ontology.owl")
    parser.add_argument("--links", help="Path to links or sameAs(es)", default="links.ttl")
    parser.add_argument("-q", "--query-file", help="Path to a file containing a SPARQL query", required=True)
    parser.add_argument("--no-reasoning", action="store_true", help="Skip OWL-RL inference")
    args = parser.parse_args()

    g = Graph()
    g.parse(args.rdf, format="turtle")
    g.parse(args.ontology, format="turtle")
    g.parse(args.links, format="turtle")

    if not args.no_reasoning:
        start = time.time()
        DeductiveClosure(OWLRL_Semantics).expand(g)
        elapsed = time.time() - start
        print(f"[timing] OWL-RL Reasoning: {elapsed:.3f}s\n")

    with open(args.query_file, encoding="utf-8") as f:
        query = f.read()

    results = g.query(query)
    if results.type == "ASK":
        print(str(results.askAnswer).lower())
        return

    if results.type == "DESCRIBE":
        serialized = results.serialize(format="turtle")
        if isinstance(serialized, bytes):
            serialized = serialized.decode()
        print(serialized, end="")
        return

    headers = [str(v) for v in results.vars] if results.vars else []
    print(tabulate(list(results), headers=headers, tablefmt="simple"))
    return

if __name__ == "__main__":
    start = time.time()
    main()
    elapsed = time.time() - start
    print(f"\n[timing] Total time: {elapsed:.3f}s")
