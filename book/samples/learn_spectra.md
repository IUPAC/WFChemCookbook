# FAIR formating of (multi, hyper) spectral data

```{dropdown} About this interactive ![icons](../images/rocket.png) recipe
- Author: [Jordi Cuadros](https://orcid.org/0000-0001-6513-9140)
- Reviewer: 
- Topics: Spectral data, MS, Spectral data processing, 
- Format: Markdown file
- Skills: You should be familiar with
    - [Identifiers](https://chem.libretexts.org/Courses/University_of_Arkansas_Little_Rock/ChemInformatics_(2015)%3A_Chem_4399_5399/Text/5_Chemical_Identifiers)
    - [Instrumental analysis](https://chem.libretexts.org/Bookshelves/Analytical_Chemistry/Instrumental_Analysis_(LibreTexts))
- Learning outcomes:  After completing this example you should understand:
    - Understand the different types of spectral data we may have and find
    - Know the most relevant data formats for storing MS data
    - Be able to prepare a set of MS Spectra for its FAIR distribution
- Citation: 'FAIR formating of (multi, hyper)spectral data', The IUPAC FAIR Chemistry Cookbook, https://iupac.github.io/WFChemCookbook/samples/learn_spectra.html
- Reuse: This notebook is made available under a [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) license.
```

Spectral data are common in many domains and may arise from a variety of instruments and instrumental techniques. In 
many cases, a spectrum is a table of observed values as a single variable changes (wavelength, time, mass-to-charge 
ratio...) but in other cases can be more complex as or the number of variables or the resolution increases. 

## What data?

While we all share the mental image of a spectrum, and most of us have different mental images for an IR (usually a 
line with broad overlapping peaks) or for an MS spectrum (usually a set of vertical lines), we are often unaware of 
the data processing that leads to these results.

Any spectrum starts with some **raw data** collected by a set of sensors inside the instrument. While these unprocessed 
data set is rarely available, We must be aware that the data that usually comes out from the analytical instruments may 
have already been partially processed.

These data collected from the sensors are then processed to obtain many form of **processed spectral data**. Commonly 
the baseline is adjusted, noise is removed, and scales may be centered and scaled. These data still include data points 
for each possible of the independent variable (time, mass-to-charge ratio, wavelength...). 

For some analytical techniques, data undergo further processing in order to select the relevant peak. The spectral data 
are then reduced to a **peak list** by identifying the local maxima and using a threshold value to keep only significant signals.  

Additionally, in some cases, spectra are further simplified by keeping only the data that belong to one or more 
**regions of interest** (ROI). Further additional data can also be calculated, like integrals, coupling constants, etc., 
and included to the spectral data. 

While any of these data can be stored in the same formats independenly of the level of processing, it is important to 
properly encode the data manipulation steps being performed, and to understand what is stored in a data set. 

Last, sometimes this is presented in a chart (static or interactive) and/or saved as an image file.

The data in each of these processing steps offers different types of reusability. More on this is discussed, for NMR, in
-  Hanson, R. M., Jeannerat, D., Archibald, M., Bruno, I., Chalk, S., Davies, A. N., ... & Rzepa, H. S. (2021). FAIR enough?. Spectrosc. Europe, 33(2), 25-31. 

Therefore, consider including in your FAIR data more than one type of information, for example, raw data, a processed 
data file for the regions of interest and an image or PDF of the spectra.

## A simple minimal approach

We will approach below on to find appropriate formats for the many existant analytical techniques, but a common minimal 
approach that is always possible is to encode the data as one or more tables in a comma-separated text file (CSV) or in 
a tab-delimited text file (TSV) supplemented with the required metadata to undestand and properly interpreted the data. 
Metadata is usually encoded in XML or JSON data files, although other standard open formats may also be possible. 

More on this approach can be found at [Preparing Chemical Data for FAIR Sharing - A Minimalist Approach](PrepChemicalDataforSharing.md).

## What metadata?

Associated data is critical for reusing spectral data sets. Guidance on this is offered in the reports of the 
[FAIRSpec IUPAC project](https://iupac.org/project/2019-031-1-024/). Some details are also included in 
[Creating a UV/Vis (meta)data file structure for small molecule characterisation](uvvis_metadata.ipynb).

It is always important to include

- Contextual information about the data (references to papers or collections)
- Instrumental details, such as the instrument manufacturer and its model, and the parameters being used when operating it
- Sample information, using chemical identifiers in the case of known susbtances, mixtures identifiers if mixture is known, or best available description in other cases
- Analytical procedure/technique followed to prepare the data
- Authorship and licensing information

The more information is available and accessible, the more reusable will be the data set. The more standardized 
identifiers we use, the more findable it will be. And interoperability will be enhanced if we use standardized 
formats for the metadata.

## Plenty of formats (some are FAIRer than others)

Looking now into more specific data types for the different analytical techniques, we may be surprised by the large 
number of formats that are available. Many of them are described in

- NFDI4Chem. Data format standard. https://knowledgebase.nfdi4chem.de/knowledge_base/docs/topics/format_standards/
- Rauh, D., Blankenburg, C., Fischer, T., Jung, N., Kuhn, S., Schatzschneider, U., Schulze, T. & Neumann, S. (2022). 
- Data format standards in analytical chemistry. Pure and Applied Chemistry, 94(6), 725-736. https://doi.org/10.1515/pac-2021-3101

From a FAIR perspective, non-propietary, text-based and standard formats should be preferred.

For MS, a wider revision, centered in bioinformatics, is published as:
- Deutsch E. W. (2012). File formats commonly used in mass spectrometry proteomics. Molecular & cellular proteomics: 
- MCP, 11(12), 1612–1621. https://doi.org/10.1074/mcp.R112.019695


## Guidance for MS data
So, let's assume we have a set of experimental MS data from a coupled instrument (HPLC-MS, GC_MS, tandem MS...). 
How should we go with them.

Standard open text-based formats for MS data include
- [JCAMP-DX](https://iupac.org/what-we-do/digital-standards/jcamp-dx/), developed by IUPAC,
- [msp](https://chemdata.nist.gov/mass-spc/ms-search/docs/Ver20Man_11.pdf), a NIST format used, for instance, in the MoNA database, and
- mzML, https://doi.org/10.1002/pmic.200890049, published by American Society for Mass Spectrometry.

The first format is common for single MS, while msp and mzML are usual in the metabolomics and proteomics communities.


## MS databases and conversion software
Databases and software for converting into different formats. It worth checking the formats used to encode the MS spectra.

**Databases with MS spectra**
- [PubChem](https://pubchem.ncbi.nlm.nih.gov/)
- [MassBank of North America (MoNA)](https://mona.fiehnlab.ucdavis.edu/)
- [ChemSpider](http://www.chemspider.com/)
- [MassIVE](https://massive.ucsd.edu/ProteoSAFe/static/massive.jsp)

**Software**
- [Proteowizard](https://proteowizard.sourceforge.io/)
- [GNPS](https://gnps-quickstart.ucsd.edu/conversion)
- [RawConverter](http://fields.scripps.edu/rawconv/)

Python libraries and R packages also exist for reading and converting MS files.