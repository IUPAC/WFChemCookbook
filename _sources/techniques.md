# FAIR Techniques for Chemical Data

Making your science FAIRer: This section details how you can make your work FAIRer by upgrading how you can do common 
activities in a FAIR enabled way. 

This material will be informed by the WorldFAIR Chemistry D3.1 project related to Reporting Guidance for FAIR chemical 
data and other community resources, including the NDFI4Chem Knowledgebase and the ELIXIR FAIR Cookbook. In addition, 
efforts to inform best practice, such as the IUPAC FAIR Spec Project, will be highlighted.

Test Kitchen / Checking your chemical data/metadata: This section will review protocols for confirming the completeness
and consistency of chemical data and metadata files, for example the checkCIF service for Crystallographic Information 
Files (CIF). This material will also be informed by the WorldFAIR Chemistry D3.3 project related to Protocol Services 
for standardized programmatic access to chemical data, and other community resources.

Ingredients / Data standards and formats for Chemistry: This section will provide descriptions of standard notation 
and file formats available for sharing and reusing chemical data that are referred to in recipes throughout this book.
- Chemical structures
- Chemical properties
- Chemical terminology
- Other useful formats

This category introduces basic techniques on how to work with machine-readable data with particular emphasis on 
chemical data nuances and ways chemical data can be made more FAIR, when it is initially shared and for reusing 
data that are not fully FAIR. Techniques should be relatively easy to implement into common workflow(s) and give 
tangible results/improvements.  

- Overview of good FAIR practices 
  - You’ve got to manage your data [files, structures, description, etc.] 
  - You’ve got to get the data shared and licensed and citable 
  - Identifying things of import (people, instrument, samples) 
  - Critical stages of data processing (raw, processed, derived) 
  - ***Example of how InChI supports F-A-I-R 
- Overview of working with FAIR chemical data 
  - Queries 
  - Matching on chemical identifiers/representations 
  - APIs (what is an API and then link to some the recipes that demo these for tools and resources)  
  - Chemical data standards! 
- Safety/watch-outs 
  - Syntax: character sets, units 
  - Semantics: valence models, units, temperature scale, date format  
  - Normalization
  - Validation 
  - Clean up 
  - Examples of unFAIR data
    - (condensed chemical formula is not fully interoperable/identifiable) 
    - Data values without reference (or other provenance, conditions) 
- Using chemical data standards 

- General resources on FAIR for chemistry
  - FAIR Data Principles | NFDI4Chem Knowledge Base
  - Elixir FAIR Cookbook
  - Elixir DRM…
- General topics about how to improve working with chemical data, for example…
  - Basic data management
  - Assigning unique identifiers (especially for chemicals) 
  - File naming conventions


Given that most users of the cookbook will not be cheminformatics/data science experts, there needs to be some content 
that provides background material to users. Generally this would mean content about chemistry information and data 
needed by a computer science/data science background AND computer science information needed by a chemistry professional
or student.  Some of this material will be available externally and linked in pages, but other content might be best 
discussed in the context of computer science or chemistry to communicate how they relate.
- Basic data manipulation stuff 
  - APIs, spreadsheets, languages 
  - What happens when you have unFAIR data 
- Basic chemistry issues? And how do you manage these? 
  - Chemical description 
  - Chemistry data standards 
