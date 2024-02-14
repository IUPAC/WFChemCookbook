# Data Repository: PubChem

```{dropdown} About this recipe
- Author: [Sunghwan Kim](https://orcid.org/0000-0001-9828-2074)
- Reviewer: [Sam Munday](https://orcid.org/0000-0001-5404-6934)
- Topics: The PubChem database, PubChem dataypes, PubChem tutorial
- Format: Markdown file
- Scenarios: Retrieve chemical data from an online database
- Skills: You should be familiar with
    - [Application Programming Interfaces (APIs)](https://www.ibm.com/topics/api)
    - [The JavaScript Object Notation (JSON) file format](https://www.w3schools.com/js/js_json_intro.asp)
    - [Introductory Python](https://www.youtube.com/watch?v=kqtD5dpn9C8)
- Learning outcomes: After completing this recipe you should understand:
    - The kinds of data that PubChem makes available
    - What a PubChem summary page is how to access it
    - Available PubChem tools (via tutorial)
- Citation: 'Data Repository: PubChem', Sunghwan Kim, The IUPAC FAIR Chemistry Cookbook, Contributed: 2023-02-28 [https://w3id.org/ifcc/IFCC004](https://w3id.org/ifcc/IFCC004).
- Reuse: This notebook is made available under a [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) license.
```

## What is PubChem?

PubChem [(https://pubchem.ncbi.nlm.nih.gov)](https://pubchem.ncbi.nlm.nih.gov) {cite:p}`Kim2023` is a very popular 
chemistry information resource for biomedical research communities in many areas, including cheminformatics, 
chemical biology, medicinal chemistry, and drug discovery. PubChem's information content, collected from 
hundreds of data sources, is organized into multiple data collections, including Substance, Compound, BioAssay, 
Gene, Protein, Pathway, Cell Line, Taxonomy, and Patent {cite:p}`Kim2022`.

Substance archives the chemical data submitted by individual data sources and Compound stores the unique 
chemical structures extracted from Substance through chemical structure standardization. BioAssay contains 
biological assay descriptions and test results deposited by assay data providers. The record identifiers (IDs)
used in Substance, Compound, and BioAssay are called Substance ID (SID), Compound ID (CID), and Assay ID (AID),
respectively. The other data collections (i.e., Gene, Protein, Pathway, Cell Line, Taxonomy, and Patent) 
provide alternative views of PubChem data, related to a specific gene, protein, pathway, cell line, taxon, 
and patent document, respectively. Each record in the data collections has a dedicated web page (called 
a Summary page), which presents information available in PubChem for that record. This page also presents 
relevant annotations collected by PubChem from authoritative data sources.  Here are some example Summary 
pages for PubChem records.

- Compound (CID 60823, aspirin):<br>
  [https://pubchem.ncbi.nlm.nih.gov/compound/2244](https://pubchem.ncbi.nlm.nih.gov/compound/2244)

- Substance (SID 829042, depositor-provided structure of aspirin)<br>
  [https://pubchem.ncbi.nlm.nih.gov/substance/829042](https://pubchem.ncbi.nlm.nih.gov/substance/829042)

- Assay (AID 463075, high-throughput assay to identify inhibitors of TNF-<sym>alpha-induced cell death)<br>
  [https://pubchem.ncbi.nlm.nih.gov/bioassay/463075](https://pubchem.ncbi.nlm.nih.gov/bioassay/463075)

- Gene (human tumor necrosis factor (TNF); NCBI GeneID 7124)<br>
  [https://pubchem.ncbi.nlm.nih.gov/gene/7124](https://pubchem.ncbi.nlm.nih.gov/gene/7124)

- Protein (mouse Cytochrome P450 1A1 (CYP1A1); NCBI accession P00184)<br>
  [https://pubchem.ncbi.nlm.nih.gov/protein/P00184](https://pubchem.ncbi.nlm.nih.gov/protein/P00184)

- Pathway (Glycolysis in human; Reactome ID R-HSA-70171)<br>
  [https://pubchem.ncbi.nlm.nih.gov/pathway/Reactome:R-HSA-70171](https://pubchem.ncbi.nlm.nih.gov/pathway/Reactome:R-HSA-70171)

- Cell Line (Michigan Cancer Foundation-7 (MCF-7) breast cancer cell line)<br>
  [https://pubchem.ncbi.nlm.nih.gov/cell/mcf-7](https://pubchem.ncbi.nlm.nih.gov/cell/mcf-7)

- Taxonomy (Saccharomyces cerevisiae (baker's yeast); NCBI Taxonomy ID 4932)<br>
  [https://pubchem.ncbi.nlm.nih.gov/taxonomy/4932](https://pubchem.ncbi.nlm.nih.gov/taxonomy/4932)

- Patent (US Patent US-2021379090-A1)<br>
  [https://pubchem.ncbi.nlm.nih.gov/patent/US-2021379090-A1](https://pubchem.ncbi.nlm.nih.gov/patent/US-2021379090-A1)


## PubChem Tutorials

For novice users, an interactive online PubChem tutorial is available at the following webpage:

[https://www.nlm.nih.gov/oet/ed/pubchem/tutorial/index.html](https://www.nlm.nih.gov/oet/ed/pubchem/tutorial/index.html)

In addition, the following paper {cite:p}`Kim2021` provides step-by-step instructions on how to explore data contained in PubChem, along with examples of commonly requested tasks.

>Kim S. **Exploring Chemical Information in PubChem.** Curr. Protoc.; 2021 Aug 9; 1(8):e217. doi: https://doi.org/10.1002/cpz1.217.  
>[\[PubMed PMID: 34370395\]](https://pubmed.ncbi.nlm.nih.gov/34370395/) [\[PubMed Central PMCID: PMC8363119\]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8363119/) [\[Free Full Text\]](https://doi.org/10.1002/cpz1.217)

This paper includes several protocols designed to help users to get familiar with PubChem's data and tools.

* **Basic Protocol 1**: [Finding genes and proteins that interact with a given compound](https://currentprotocols.onlinelibrary.wiley.com/doi/10.1002/cpz1.217#cpz1217-prot-0001)
* **Basic Protocol 2**: [Finding drug-like compounds similar to a query compound through a two-dimensional (2-D) similarity search](https://currentprotocols.onlinelibrary.wiley.com/doi/10.1002/cpz1.217#cpz1217-prot-0002)
* **Basic Protocol 3**: [Finding compounds similar to a query compound through a three-dimensional (3-D) similarity search](https://currentprotocols.onlinelibrary.wiley.com/doi/10.1002/cpz1.217#cpz1217-prot-0003)
* **Support Protocol**: [Computing similarity scores between compounds](https://currentprotocols.onlinelibrary.wiley.com/doi/10.1002/cpz1.217#cpz1217-prot-0004)
* **Basic Protocol 4**: [Getting the bioactivity data for the hit compounds from substructure search](https://currentprotocols.onlinelibrary.wiley.com/doi/10.1002/cpz1.217#cpz1217-prot-0005)
* **Basic Protocol 5**: [Finding drugs that target a particular gene](https://currentprotocols.onlinelibrary.wiley.com/doi/10.1002/cpz1.217#cpz1217-prot-0006)
* **Basic Protocol 6**: [Getting bioactivity data of all chemicals tested against a protein](https://currentprotocols.onlinelibrary.wiley.com/doi/10.1002/cpz1.217#cpz1217-prot-0007)
* **Basic Protocol 7**: [Finding compounds annotated with classifications or ontological terms](https://currentprotocols.onlinelibrary.wiley.com/doi/10.1002/cpz1.217#cpz1217-prot-0008)
* **Basic Protocol 8**: [Finding stereoisomers and isotopomers of a compound through identity search](https://currentprotocols.onlinelibrary.wiley.com/doi/10.1002/cpz1.217#cpz1217-prot-0009)
  
Finally, one of the developers at PubChem, Dr. Sunghwan Kim, has developed some [tutorials](pubchem_pugrest) about the PubChem API,
the Power User Group - Representation State Transfer ([PUG-REST](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest)) service.

## References  
  
```{bibliography}
:filter: docname in docnames
```
