from pronto import Ontology

# Loading Gene Ontology
url = "http://purl.obolibrary.org/obo/go.obo"
ontology = Ontology(url)

# General information about the ontology
print(f"Number of terms in the ontology: {len(ontology)}")

# Search for a specific term
term_id = "GO:0008150"  # Биологический процесс
term = ontology[term_id]
print(f"Term ID: {term.id}")
print(f"Name: {term.name}")
print(f"Definition: {term.definition}")

# List all parent terms
print("\nParent Terms:")
for parent in term.superclasses(distance=1):
    print(f"- {parent.id}: {parent.name}")

# Print all child terms
print("\nChild Terms:")
for child in term.subclasses(distance=1):
    print(f"- {child.id}: {child.name}")
