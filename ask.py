import argparse
import time

from owlrl import DeductiveClosure, OWLRL_Semantics
from rdflib import Graph
from tabulate import tabulate

REMOTE_ENDPOINTS = {
    "wikidata": "https://query.wikidata.org/sparql",
    "dbpedia": "https://dbpedia.org/sparql",
}

def print_rdflib_results(results):
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

def print_remote_results(results):
    if "boolean" in results:
        print(str(results["boolean"]).lower())
        return

    bindings = results.get("results", {}).get("bindings", [])
    variables = results.get("head", {}).get("vars", [])
    rows = [
        [binding.get(variable, {}).get("value", "") for variable in variables]
        for binding in bindings
    ]
    print(tabulate(rows, headers=variables, tablefmt="simple"))

def main():
    parser = argparse.ArgumentParser(description="Interactive SPARQL CLI using rdflib")
    parser.add_argument("--rdf", help="Path to RDF file", default="output/movies.ttl")
    parser.add_argument("--ontology", help="Path to OWL ontology", default="ontology.owl")
    parser.add_argument("--links", help="Path to links or sameAs(es)", default="links.ttl")
    parser.add_argument("-q", "--query-file", help="Path to a file containing a SPARQL query", required=True)
    parser.add_argument("--target", choices=["local", "wikidata", "dbpedia"], default="local", help="Query target (default: local RDF graph)")
    parser.add_argument("--no-reasoning", action="store_true", help="Skip OWL-RL inference")
    args = parser.parse_args()

    with open(args.query_file, encoding="utf-8") as f:
        query = f.read()

    if args.target == "local":
        g = Graph()
        g.parse(args.rdf, format="turtle")
        g.parse(args.ontology, format="turtle")
        g.parse(args.links, format="turtle")

        if not args.no_reasoning:
            start = time.time()
            DeductiveClosure(OWLRL_Semantics).expand(g)
            elapsed = time.time() - start
            print(f"[timing] OWL-RL Reasoning: {elapsed:.3f}s\n")

        print_rdflib_results(g.query(query))
        return

    from SPARQLWrapper import JSON, SPARQLWrapper
    
    sparql = SPARQLWrapper(REMOTE_ENDPOINTS[args.target])
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    print_remote_results(sparql.query().convert())


if __name__ == "__main__":
    start = time.time()
    main()
    elapsed = time.time() - start
    print(f"\n[timing] Total time: {elapsed:.3f}s")
