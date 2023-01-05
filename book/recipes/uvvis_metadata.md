# Recipe: Creating a UV/Vis (meta)data file

- Author(s): [Sally Bloodworth](https://orcid.org/0000-0003-2219-3635), [Simon Coles](http://orcid.org/0000-0001-8414-9272) 
- Topic:	 Creating a UV/Vis (meta)data file structure for small molecule characterisation
- Format:	 Guidelines 

## 1.  Objectives
To provide guidance on the minimum set of metadata required for publishing UV/Vis spectroscopic data as supplementary
information to support compound characterisation using the Beer-Lambert Law. To apply the FAIR principles for data 
management to produce digital data objects that contain raw, spectral and metadata to enable current and future 
researchers in the reanalysis and visualisation of UV/Vis spectroscopic data.

###  1.1	Target audience
Researchers who routinely work with a user interface (spreadsheet) for preparation of supplementary material to support 
compound characterisation for publication: authors who aim to improve the FAIRness of their published supporting data.

## 2.	Resources
FAIR data management refers to the IUPAC FAIRSpec standard: IUPAC specifications for the findability, accessibility, 
interoperability and reusability of spectroscopic data in chemistry {cite} `Hanson2022`.

## 3.	Structuring the (meta)data 

### 3.1	File formats
Instrument–specific file formats should not be used for storage of the raw spectroscopic dataset. If JCAMP-DX is a 
fully supported format of the spectrophotometer, then the sample level metadata available in the raw data file could 
be user–defined or mandatory. The metadata content also depends on mapping from the spectrophotometer native software 
to JCAMP-DX{cite} `Davies2019`. Sample level metadata should be supplemented using the file structure defined in 3.2 below.

The file formats recommended here are not exhaustive. For data reuse and preservation, all file formats must be 
non-proprietary, and associated software open source (maintained). Files should be uncompressed and unencrypted.

### 3.2 File hierarchy

<table style="width: 100%">
    <thead>
        <tr style="font-weight: bold; background: #dddddd">
            <td colspan="4">Raw data</td>
        </tr>
    </thead>
    <tbody>
        <tr style="font-weight: bold;">
            <td>Content</td>
            <td>Definition</td>
            <td>Essential or desirable</td>
            <td>Format</td>
        </tr>
        <tr>
            <td>Data matrix (with or without column headings)</td>
            <td>Spectrophotometer output as tabular data (absorbance and wavelength)</td>
            <td>Essential</td>
            <td>CSV (.csv)<br/>JCAMP–DX (core LDR component)</td>
        </tr>
        <tr style="font-weight: bold; background: #dddddd">
            <td colspan="4">Sample level metadata</td>
        </tr>
        <tr>
            <td>Sample ID</td>
            <td>Identifier for the sample which is unique within the project</td>
            <td>Essential</td>
            <td rowspan="4" style="vertical-align: top">Plain text (.txt)
                <br/>XML (.xml)<br/>R Markdown (.rmd)<br/>Jupyter Notebook Markdown (.ipynb)</td>
        </tr>
        <tr>
            <td>Linking sample ID</td>
            <td>Provenance identifier for the sample in the associated process capture document (digital or paper notebook)</td>
            <td>Essential</td>
        </tr>
        <tr>
            <td>Data labels (if absent from the data matrix)</td>
            <td>Description and units for the tabular raw data columns</td>
            <td>Essential</td>
        </tr>
        <tr>
            <td>Sample concentration, solvent and optical pathlength</td>
            <td>Experimental parameters</td>
            <td>Essential</td>
        </tr>
        <tr>
            <td rowspan="2">Chemical structure</td>
            <td>Chemical structure identifier in the form of an alphanumeric text string</td>
            <td>Essential</td>
            <td>InChI<br/>SMILES</td>
        </tr>
        <tr>
            <td>SMILES validation</td>
            <td>Desirable</td>
            <td>Toolkit(version) identifier</td>
        </tr>
        <tr style="font-weight: bold; background: #dddddd">
            <td colspan="4">Analysis level metadata</td>
        </tr>
        <tr>
            <td>Content</td>
            <td>Definition</td>
            <td>Essential or desirable</td>
            <td>Format</td>
        </tr>
        <tr>
            <td>Processed data matrix</td>
            <td>Tabular data: absorbance, wavelength, and molar absorptivity (ε); with data labels and units</td>
            <td>Essential</td>
            <td>CSV (.csv)</td>
        </tr>
        <tr>
            <td>Data reporting:<br/>
                1.	Plot of the UV/Vis spectrum<br/>
                2.	𝜆max and associated molar extinction coefficient</td>
            <td>The two key outputs required for publication.</td>
            <td>Essential</td>
            <td>R Markdown (.rmd)</td>
        </tr>
        <tr style="font-weight: bold; background: #dddddd">
            <td colspan="4">Project level metadata</td>
        </tr>
        <tr>
            <td>Content</td>
            <td>Definition</td>
            <td>Essential or desirable</td>
            <td>Format</td>
        </tr>
        <tr>
            <td>Study ID</td>
            <td>Identifier(s) for the scientific study; funder’s project ID(s)</td>
            <td>Desirable</td>
            <td rowspan="2" style="vertical-align: top">Plain text (.txt)<br/>XML (.xml)<br/>R Markdown (.rmd)<br/>
                    Jupyter Notebook Markdown (.ipynb)<br/>Jupyter Notebook Markdown (.ipynb)</td>
        </tr>
        <tr>
            <td>Instrument ID</td>
            <td>Spectrophotometer vendor and version</td>
            <td>Desirable</td>
        </tr>
        <tr>
            <td>Data storage location</td>
            <td>Link to the data storage location</td>
            <td>Essential</td>
            <td rowspan="2" style="vertical-align: top">URL for an open access repository deposition</td>
        </tr>
        <tr>
            <td>Spectrophotometer calibration</td>
            <td>Link to structured calibration data</td>
            <td>Essential</td>
        </tr>
</tbody>
</table>

## 4.	Data reporting


## 5.	Glossary
- JCAMP–DX: IUPAC standard file format for spectral data{cite} `IUPAC2022`.
- LDR: Labelled–data–record, the basic element of a JCAMP–DX file.


## 6.	References
```{bibliography}
:filter: docname in docnames
:style: unsrt
```