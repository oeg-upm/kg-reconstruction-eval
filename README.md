# (Re)Construction Impact on Metadata Representation Models
We investigate two alternatives for re-constructing an existing graph to interchange between different metadata representation models. This work is useful when is needed to change the metadata representation in a pre-existing KG and the KG engineers responsible for the construction of a KG want to explore alternatives. We evaluate KG re-construction in four representations with (i) KG construction systems, that construct the KG from heterogeneous data with declarative mappings; and (ii) using CONSTRUCT queries from KG stored in triplestores.

<p align="center">
 <img src="https://github.com/oeg-upm/kg-reconstruction-eval/assets/36294992/d8383308-fc20-4188-b631-e7b7df2d5757" alt="workflow" width="650"/>
</p>

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

### Dataset
[SemMedDB](https://lhncbc.nlm.nih.gov/ii/tools/SemRep_SemMedDB_SKR.html), the Semantic MEDLINE Database, is a repository that contains information of extracted biomedical entities and predications (subject-predicate-object triples) from biomedical texts (titles and abstracts from PubMed citations). 

The tables that comprise SemMedDB are available for [download as a relational database or CSV files](https://lhncbc.nlm.nih.gov/ii/tools/SemRep_SemMedDB_SKR/SemMedDB_download.html).
The data in this use case is licensed under the [UMLS - Metathesaurus License Agreement](https://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/release/license_agreement.html), which does not allow for its distribution (Data may be accessed by obtaining an account with the UMLS licence [here](https://www.nlm.nih.gov/databases/umls.html)). 

We perform the evaluation with this dataset structured in four metadata representations (Standard Reification, Named Graphs, N-Ary Relationships and RDF-star) and in four size scales (1K, 10K, 100K and 1M).

### Mappings and Queries

- [RML mappings](https://github.com/oeg-upm/kg-reconstruction-eval/tree/main/mappings/rml)
- [SPARQL-Antything queries](https://github.com/oeg-upm/kg-reconstruction-eval/tree/main/mappings/sparql-anything)
- [SPARQL CONSTRUCT queries](https://github.com/oeg-upm/kg-reconstruction-eval/tree/main/queries)


All results (including fine-grained ones) can be found [here](https://github.com/oeg-upm/kg-reconstruction-eval/tree/main/results)



## Authors
- Ana Iglesias (Ontology Engineering Group - UPM)
- David Chaves-Fraga (Ontology Engineering Group - UPM)
- Jhon Toledo (Ontology Engineering Group - UPM) 


