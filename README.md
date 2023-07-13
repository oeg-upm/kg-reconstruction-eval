# Constructing or Re-construction? An RDF reification evaluation
We investigate two alternatives for re-constructing an existing graph with different structure from a reification perspective. This work is useful when there is a need for reification and the KG engineers responsible for the construction of a KG want to explore alternatives. We evaluate KG re-construction in four reifications with (i) KG construction systems, that construct the KG from heterogeneous data with declarative mappings; and (ii) using CONSTRUCT queries from KG stored in triplestores.


## Engines
We test the performance and scalability of a set of KG construction and triplestores:

KG Construction Engines:
- [SPARQL-Antything v0.8](https://github.com/SPARQL-Anything/sparql.anything/releases/tag/v0.8.1)
- [Morph-KGC v2.5.0](https://github.com/oeg-upm/morph-kgc/releases/tag/2.5.0)

Triplestores:
- [GraphDB v10.2.1](https://graphdb.ontotext.com/)
- [Jena Fuseki v4.8.0](https://jena.apache.org/download/)
- [Oxigraph v0.3.1](https://github.com/oxigraph/oxigraph/releases/tag/v0.3.10)


## Evaluation resources: SemMedDB

[SemMedDB](https://lhncbc.nlm.nih.gov/ii/tools/SemRep_SemMedDB_SKR.html), the Semantic MEDLINE Database, is a repository that contains information of extracted biomedical entities and predications (subject-predicate-object triples) from biomedical texts (titles and abstracts from PubMed citations). 

The tables that comprise SemMedDB are available for [download as a relational database or CSV files](https://lhncbc.nlm.nih.gov/ii/tools/SemRep_SemMedDB_SKR/SemMedDB_download.html).
The data in this use case is licensed under the [UMLS - Metathesaurus License Agreement](https://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/release/license_agreement.html), which does not allow for its distribution (Data may be accessed by obtaining an account with the UMLS licence [here](https://www.nlm.nih.gov/databases/umls.html))

## Authors
- Ana Iglesias (Ontology Engineering Group - UPM)
- David Chaves-Fraga (Ontology Engineering Group - UPM)
- Jhon Toledo (Ontology Engineering Group - UPM) 


