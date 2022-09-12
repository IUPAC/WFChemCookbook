# How To: Unique Identifiers for Chemical Data

```{tableofcontents}
```
To be FAIR in how you present, write, or deposit your research it is important to identify accurately what you have 
studied, what you have used to do the research, and the type(s) of data you have collected.  In this “how to” we talk 
about many of the unique identifier systems that chemistry researcher might need to use, and look at what’s coming.

### Why are unique identifiers important?
Have you ever done a search for information about a specific chemical only to have to try multiple searches on 
(probably Google)? That’s because different scientists have tended to name compounds differently for ease of reference, 
because it’s a trade name, because your language is not English, or because there are different ways to name compounds 
based on standard rules from [IUPAC](https://iupac.org/body/800/) or [ACS](https://www.acs.org/content/acs/en/about/governance/committees/nomenclature-terminology-symbols.html).  No matter what the reason, naming compounds has been difficult because 
there are so many of them (over 198,000,000 based on CAS).

<p style="text-align: center;">Question: How many names are there for acetone? Answer: Look 
<a href="https://pubchem.ncbi.nlm.nih.gov/compound/180#section=Names-and-Identifiers">here</a>.</p>

In today’s digital world, we need to work smarter with what is available to help accurately and 'FAIRly' identify 
chemical compounds and other important information that characterizes the work we do.  This does not mean that you 
should throw away a name for a compound that you normally use, just add a unique identifier when you add it to your 
notebook or include it in your paper or presentation.

Where and how do you find unique identifiers for chemical compounds?
There are many resources where you can search for unique chemical identifiers, some free, others not. Here is a short list, for more check out the “Resources for chemical identification” section. Each allows you to enter your name for the compound and get back unique identifier for that compound.
- Free
  - US NIH PubChem https://pubchem.ncbi.nlm.nih.gov
  - US NIH Chemical Identifier Resolver https://cactus.nci.nih.gov/chemical/structure
  - RSC ChemSpider https://www.chemspider.com
  - ACS Common Chemistry https://commonchemistry.cas.org
- For a fee
  - ACS SciFindern https://scifinder-n.cas.org

### Unique identifiers for chemical substances
Historically, the first system to identify chemical substances uniquely was developed by CAS, with the 
CAS Registry Number system. Each compound entered into CAS’s system was assigned a 
[unique number](https://en.wikipedia.org/wiki/CAS_Registry_Number) with a format of 
(two-eight digits)-(two digits)-(check digit).

More recently, the [International Chemical Identifier (InChI)](https://www.inchi-trust.org/) and its hashed 
InChIKey have become available and more popular due to these identifiers being created from a standard 
[molfiles](https://en.wikipedia.org/wiki/Chemical_table_file) and a 
[free piece of software](https://www.inchi-trust.org/download-latest-inchi-standard-software/), 
that implements the algorithm to generate the InChI and InChIKey.

### Unique identifiers for chemical reactions
The InChI-Trust that is responsible for the InChI standard has developed a standard for representing chemical reactions,
using the InChI as the basis.  The Reaction InChI, or [RInChI](https://www.inchi-trust.org/reactions/), takes the InChIs
(InChIKeys) for reactants, products and catalysts integrates them into a single identifier for a chemical reaction.

### Unique identifiers for macromolecules
Originally developed in the Pistoia Alliance and now supported by IUPAC, the Hierarchical Editing Language for 
Macromolecules ([HELM](https://www.pistoiaalliance.org/helm-project/)) is a standard to generate unique identifiers 
for larger molecules (e.g., proteins, nucleotides, antibody drug conjugates) where other identifier systems are 
impractical to use.

### Unique identifiers for chemical/physical quantities
The [IUPAC Green Book](https://iupac.org/what-we-do/books/greenbook/) is the definitive source of how to represent 
chemical and physical quantities in chemistry. The Green Book guidelines are for humans and although there is a new 
‘digital first’ edition in the works, the best system currently available to represent measured quantities is the 
Quantity, Units, Dimensions and Datatypes specification ([QUDT](https://www.qudt.org/doc/DOC_VOCAB-QUANTITY-KINDS.html))
that was originally developed for NASA.

### Unique identifiers for units of measurement
As above, the best place to go for the unique identification of units of measure is the 
[QUDT](https://www.qudt.org/doc/DOC_VOCAB-UNITS.html) specification. The string representation of each unit of 
measurement is formatted in accordance with a 
[set of rules](https://github.com/qudt/qudt-public-repo/wiki/Unit Vocabulary Submission Guidelines#qname-naming-rules), 
so if you don’t see the unit you want to use, you can generate the string for that unit even though it is not already 
part of the QUDT system.  You can subsequently submit a request to propose the new unit that you need.

### Unique identifiers for research articles
Introduced in 2000, the Digital Object Identifier ([DOI](https://www.doi.org/)) has revolutionized publishing research. 
Today all major publishers assign a DOI with a research article once its accepted and this makes the publication easy 
to reference and find.  In addition, if you write a paper and cite papers that have DOI’s, it is easier than ever to 
find related research.

DOI’s are now used for more than research articles, being assigned to books, book chapters, [definitions of chemical 
concepts](https://goldbook.iupac.org/), and more recently data, in repositories such as 
[figshare](https://figshare.com/) and [Zenodo](https://zenodo.org/).

### Unique Identifiers for researchers
In the past it was difficult to keep up with specific researchers, and very difficult to identifier a particular 
researcher if they had a common name.  Today, it's easy by using the freely available 
‘Open Researcher and Contributor ID’ (ORCID), designed for researchers.

### Other unique identifiers for research
- [Mass spectra](https://splash.fiehnlab.ucdavis.edu/)
- [Funding agencies](https://www.crossref.org/services/funder-registry/)
- [Research methods](https://www.protocols.io/)
- [Research resources](https://www.rrids.org/) (general)

### The future of unique identifiers
If you think about all the identifiers mentioned above it may dawn on you that there are other things you might 
want to more specifically identify when you publish your research.  Here are some things that are coming.
- [Persistent identifiers for instruments](https://www.rd-alliance.org/groups/persistent-identification-instruments-wg)
