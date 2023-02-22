# Glossary

A glossary of FAIR terminology will be developed.  The entries below come from the recent paper {cite:p}`Hanson2022`
from the [IUPAC 'FAIR Spec' project](https://iupac.org/project/2019-031-1-024/) and will be augmented with chemistry
examples and addition entries as needed.  Terms marked [RDA] are found/derived from this 
[Research Data Alliance resource](https://smw-rda.esc.rzg.mpg.de/dft-3.0.html).

- _chemical structure identifier_ -
  A meaningful alphanumeric text string that can uniquely identify a chemical compound and facilitate its handling in 
  computer databases string of characters that characterizes a structure. Examples include InChI and SMILES.
- _curation_ - 
  The process of maintaining, preserving and adding value to data throughout its lifecycle. One aspect of curation 
  is the design and creation of metadata associated with a digital collection. Curation can involve automated 
  machine-based processes as well as manual or semi-automated cataloging of digital objects.
- _data_ - 
  To a practicing chemist, it should be obvious that digital entities coming from a laboratory instrument constitute 
  "raw data" (referred to herein as "datasets"). However, the word data as used here is a broader term. For our 
  purposes, data includes the digital entities associated with spectroscopic data analysis. These might include peak 
  lists or chemical shift, splitting, and integration descriptions in NMR spectroscopy, as well as 1D and 2D spectral 
  assignments in relation to molecular structure. Chemical structure graphs (MOL, SDF, for example) also fall in this category.
- _data and metadata extraction_ - 
  The primarily machine-based act of curation of one or more digital entities associated with a (spectroscopic) dataset 
  carried out in order to generate value-added digital representations of that dataset.  For example, the creation of a 
  spectrum in JCAMP-DX format from an instrument-derived "raw" dataset and the creation of a PNG image or peak table 
  from that spectrum, or the extraction of temperature, probe, and pulse sequence information from a dataset.
- _data management_ - 
  The overall activity of organizing, maintaining, and cataloging data assets. We interpret this to be not just the 
  activity of professional data managers, but also all the curation of data that takes place in the field during 
  data collection and analysis.
- _data management plan_ - 
  A type of plan usually described in a formal document that outlines how data are to be handled both during a 
  research project and after the project is completed.
- _data model_ [RDA] - 
  A data model is an abstract model that specifies the structure or schema of a data set. We extend this definition 
  to relate to the full set of digital objects associated with an IUPAC FAIRSpec Data Collection.
- _data provenance_ [RDA] - 
  A type of historical information or metadata about the origin, location or the source of a digital object, or the 
  history of the ownership or location of a digital object.
- _data repository_ - 
  A service operated by organizations where data assets are stored, managed and made accessible. The repository 
  contains data organized as digital objects and digital entities and is accompanied by descriptive metadata for 
  these items. The three primary types of data repository are generalist (not domain-specific), specialist 
  (domain-specific), and institutional (based at a research institution).
- _data representation_ - 
  A digital object that may take any one of a number of forms that allow for various levels of data reuse. For 
  example, an IUPAC FAIRSpec Data Collection might include data representations in the form of the full raw 
  spectroscopic dataset, a spectrum or free induction decay (FID) stored in JCAMP-DX format, an image, and a
  text description of the spectrum in a standardized journal-ready format. Each of these data representations has 
  intrinsic value that, for a given re-user, might be the most appropriate or desirable.
- _dataset (spectroscopic)_ - 
  The "raw" data representation collected by an instrument in whatever native format that instrument creates. This 
  could be a single file or a zip file or folder containing multiple parameter files along with one or more raw or
  processed data files. In this article, we distinguish between the more general term, data, and the more specific 
  terms spectroscopic dataset.
- _digital aggregation_ [RDA] - 
  A bundle of digital entities.
- _digital collection_ - 
  A digital collection is an aggregation which contains digital objects and digital entities. The collection is 
  described by metadata. A digital collection is an organized, systematic form of purposeful aggregation, grouping
  or arrangement of elements, that has an identity of its own separate from the identity of the elements. RDA defines 
  a "Data Collection" as "a type of collection formed by some agent-driven aggregation or grouping process whose 
  parts/elements are made of data/datum. A data collection is identified by a PID and described like other types of 
  DOs by metadata" with essentially the same meaning. In addition, we recognize the term heterogeneous digital 
  collection to refer to a digital collection that includes a variety of data types (in our context, for example: 
  NMR, IR, MS, X-ray diffraction, polarimetry, cyclic voltammetry, chromatography data) as well as structural or 
  sample properties and representations.
- _digital entity_ [RDA] - 
  Anything that can be represented by a bitstream (which is a sequence of bits that encodes a specific content, 
  either stored on some media or being transferred under control of protocols).
- _digital finding aid_ - 
  A digital object that is a description typically consisting of contextual and structural information about 
  an archival resource.
- _digital object_ [RDA] - 
  A digital entity composed of a structured sequence of bits/bytes. As an object it is named. The bit sequence 
  realizing the object can be identified and accessed directly or indirectly via a unique and persistent identifier 
  or by use of referencing attributes describing its properties.
- _Digital Object Identifier (DOI)_ - 
  A unique character string form of a persistent identifier, such as "10.1515/pac-2021-2009" (more precisely referred to as 
  a DOI Name) that can be part of a URL such as "https://doi.org/10.1515/pac-2021-2009". The distribution and management of 
  DOIs are carried out by a federation of registration agencies under the auspices of the International DOI Foundation.
- _FAIR Data Management_ - 
  Data management based on the FAIR (Findable, Accessible, Interoperable, and Reusable) Guiding Principles, recognizing 
  that there are many degrees of "FAIRness", some more aspirational than realized.
- _InChI or International Chemical Identifier_ - 
  A textual identifier for chemical substances, designed to provide a standard way to encode molecular information and to 
  facilitate the search for such information in databases and on the web generated using the algorithm as defined by IUPAC.
- _IUPAC FAIRSpec Data Collection_ - 
  A curated spectroscopic data collection organized using the principles described in this article and the 
  (developing) IUPAC FAIRSpec Specification.
- _IUPAC FAIRSpec Data Model_ (IFS Data Model) - 
  The abstract data model currently under development by the Task Group. This model describes the structure and
  format of data and metadata associated with an IUPAC FAIRSpec Data Collection.
- _landing page_ - 
  The endpoint for the resolution of a persistent identifier, typically in HTML or XML format. If the endpoint is 
  changed, this change must ideally be reflected in any registered metadata for that identifier.
- _metadata_ [RDA] - 
  Data that contains descriptive, contextual and provenance assertions about the properties of a Digital Object. 
  Metadata are data that play the role of documentation for data/resource discovery, description/documentation, 
  contextualization. Metadata can conform to a declared schema that sets out the vocabulary and properties of the 
  metadata. The schema may specify control or constraints on the values of both.
- _metadata crosswalk_ - 
  A well-defined mapping that translates elements and values from one metadata schema to those of another. Crosswalks
  facilitate interoperability between different metadata schemas and serve as a base for metadata harvesting and record exchange.
- _metadata element_ [RDA] - 
  An aspect of a digital object generally characterized by a key/value pair. To the extent that the metadata are part 
  of a defined metadata schema, the element will be designated by a unique controlled-vocabulary key, and its value
  will adhere to the description of that key within the schema.
- _metadata harvesting_ - 
  The automated collection of metadata records from different sources to create useful aggregations of metadata
  and the related services that are enabled by this process.
- _metadata registration_ - 
  The process of associating a digital object (quite possibly a collection) with a persistent identifier assigned by 
  a recognized metadata registration agency, allowing URL resolution back to the original digital object. If the 
  location of the digital object is changed, then this change must be recorded in the metadata that has been registered,
  thus ensuring its persistence. If the data repository where the digital object is stored ceases to operate, the 
  metadata records associated with that repository will continue to be available via the agency where they were registered.
- _metadata registration agency_ - 
  An organization that provides persistent identifiers for various types of digital objects and/or research outputs 
  in exchange for the registration of a metadata record, allowing these outputs and their associated metadata to 
  become discoverable. DataCite is one example of a metadata registration agency, providing managed curation of an
  extensive metadata schema. Metadata registration agencies can also provide various services that take advantage of
  their stored metadata records, including the capability of rich fielded searches and analyses of these records when 
  combined with metadata from authorities specializing in other types of persistent identifiers, such as people (ORCID),
  research organizations (ROR), data (DataCite), journal articles and funders (CrossRef).
- _metadata schema_ [RDA] - 
  A type of data schema or structure organized by a logical plan that shows the relationships between metadata elements. 
- _metadata store_ - 
  A queryable database of metadata records.
- _open data_ [RDA] - 
  Open data are data available/visible to others and that can be freely used, reused, shared, republished and 
  redistributed by anyone, within the parameters defined by license. We note that FAIR management of data does not 
  necessitate open data, and that the act of curation has a cost that might be shared with reusers.
- _persistent identifier_ (PID) [RDA] - 
  A character string (functioning as a symbol) that identifies a digital object. The identifier can be persistently 
  resolved (digitally actionable) to meaningful metadata state information about the identified digital object.
- _PID graph_ - 
  A graph of persistent identifiers themselves as the basic entities that are linked together; whatever they refer
  to is left implicit.
- _reuser_ - 
  The person or entity that has accessed a digital object for purposes, quite possibly completely different from 
  any imagined by the originator of the data.
- _sample_ - 
  A portion of material selected from a larger quantity of material. More specifically, the physical sample that was 
  the source of the spectroscopic dataset in a collection. We note that efforts are underway to uniquely identify 
  and register samples in a persistent manner43.
- _serialization_ (of a finding aid) - 
  The generation of a byte sequence in a machine- and potentially human-readable form such as JSON or XML. The IUPAC 
  FAIRSpec standard does not specify a preferred serialization of the IUPAC FAIRSpec Finding Aid, only that the 
  serialization must preserve the specified structure and vocabulary of the finding aid and its associated collection.
- _SMILES (Simplified Molecular Input Line Entry System)_ - 
  A linear representation of a molecular graph in character string form, used for searching for, matching, and
  atom-atom mapping of chemical structures and models.
