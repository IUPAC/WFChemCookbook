## OPSIN: Open Parser for Systematic IUPAC Nomenclature

- Function: IUPAC chemical name to chemical identifier converter
- Format: Website for form based queries and URL base API
- Input: IUPAC systematic chemical name
- Outputs: Standard InChI string, Standard InChIKey, SMILES, Chemical Markup Langauge (CML) XML, image (.png or .svg)
- Usage: [Instructions](https://opsin.ch.cam.ac.uk/instructions.html)
- Publication: [https://doi.org/10.1021/ci100384d](https://pubs.acs.org/articlesonrequest/AOR-PcYgSy87ettZWfqyvHmN)
- Website: https://opsin.ch.cam.ac.uk
- Application Programming Interface (API): https://opsin.ch.cam.ac.uk/opsin/
  - Endpoint: <chemicalname>.cml (e.g., https://opsin.ch.cam.ac.uk/opsin/benzene.cml)
  - Endpoint: <chemicalname>.stdinchi (e.g., https://opsin.ch.cam.ac.uk/opsin/benzene.json)
  - Endpoint: <chemicalname>.stdinchikey (e.g., https://opsin.ch.cam.ac.uk/opsin/benzene.json)
  - Endpoint: <chemicalname>.smiles (e.g., https://opsin.ch.cam.ac.uk/opsin/benzene.json)
  - Endpoint: <chemicalname>.json (e.g., https://opsin.ch.cam.ac.uk/opsin/benzene.json)
  - Endpoint: <chemicalname>.png (e.g., https://opsin.ch.cam.ac.uk/opsin/benzene.png)
  - Endpoint: <chemicalname>.svg (e.g., https://opsin.ch.cam.ac.uk/opsin/benzene.svg)
- Code Repository: https://github.com/dan2097/opsin