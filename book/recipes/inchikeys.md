## Recipe: Supplementing your records with InChIKey

- Author: [Jordi Cuadros](https://orcid.org/0000-0001-6513-9140)
- Reviewer:
- Topic: How to find InChIKeys for chemical substances using different approaches
- Format: Markdown file
- Skills: You should be familiar with
    - [Chemical Identifiers]()
- Learning outcomes: After completing this example you should understand:
  - Where to go to obtain InChIKeys starting from different chemical identifiers/formats
  - A unique identifier for a chemical substance is important to clearly indicate the chemical substances in your work
- Citation: 'Recipe: Supplementing your records with InChIKey', The IUPAC FAIR Chemistry Cookbook, https://iupac.github.io/WFChemCookbook/recipes/inchikeys.html
- Reuse: This notebook is made available under the IUPAC FAIR Chemistry Cookbook MIT license.

### Scenario
So far, you are quite used to annotate your chemical’s description with CAS-RN, but this is a propietary identifier 
with a structure that does help to make it findable. A way to increase the FAIRness of your is to append InChIKey 
anywhere you describe or refer to a chemical as in your papers, or your data and metadata files. Let’s do it together!

### Case 1: I can draw or unambiguously name my chemical 
You can use the [CACTUS Chemical Identifier Resolver](https://cactus.nci.nih.gov/chemical/structure) to get your InChIKey.

### Case 2: I have a MOL file for my chemical
If you have a MOL or SDF file for your molecule, you may use the [UniChem service](https://www.ebi.ac.uk/unichem/) to 
upload your file and obtain its InChI and InChIKey. You can also install locally and use the following software:
- InChI core software, https://www.inchi-trust.org/download-latest-inchi-standard-software/.
- OpenBabel, https://openbabel.org/wiki/Main_Page,
to convert your file to InChIKey.

### Case 3: I have the SMILES or the InChI for my chemical
You may use the CACTUS Chemical Identifier Resolver, https://cactus.nci.nih.gov/chemical/structure.

### Case 4: I only have the CAS-RN for my chemical
Try to use the ACS [Common Chemistry service](https://commonchemistry.cas.org/) to find the InChIKey for your compound. 

### Last step: Check your InChIKey
Google it!
OR
Check it through [UniChem](https://www.ebi.ac.uk/unichem/ )

### Possible additions to recipe
Ad-extra, extracting the InChIKeys from a text \b[A-Z]{14}[-][A-Z]{10}[-][A-Z]{1}\b
Version 1, standard InChI: \b[A-Z]{14}[-][A-Z]{8}SA[-][A-Z]{1}\b
Neutral specie: \b[A-Z]{14}[-][A-Z]{10}[-]N\b




