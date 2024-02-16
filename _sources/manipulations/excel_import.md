# Importing Chemical Data into Excel

```{dropdown} Culinary School Topic
- Author: [Stuart Chalk](https://orcid.org/0000-0001-6513-9140)
- Topics: Data Importing, Spreadsheets, Chemical Data
- Format: Markdown file
- Skills: You should be familiar with:
    - [Computer files and extensions](https://www.howtogeek.com/356448/what-is-a-file-extension/)
    - [Data Types](https://en.wikipedia.org/wiki/Data_type)
    - [Character Encoding](https://en.wikipedia.org/wiki/Character_encoding)
- Learning outcomes:  After completing this example you should understand:
    - How to import data into Microsoft Excel and Google Sheets
    - Understand the difference between .csv, .tsv and .txt files
    - Identify why data may be corrupted upon import a file
- Citation: 'Importing Chemical Data into Spreadsheet', Stuart Chalk, The IUPAC FAIR Chemistry Cookbook, Contributed: 
  2024-02-14 [https://w3id.org/ifcc/IFCC014](https://w3id.org/ifcc/IFCC014).
- Reuse: This notebook is made available under a [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) license.
```

## Summary
This tutorial focuses on importing data into spreadsheets.  This is a very common activity for chemists that results from 
downloading data from analytical instruments (e.g., as [JCAMP files](https://iupac.org/what-we-do/digital-standards/jcamp-dx/) - .jdx), 
from databases (e.g., MySQL), or from data websites (e.g., [PubChem](https://pubchem.ncbi.nlm.nih.gov)).  It also contextualizes
the general topic of delimited text [files](https://en.wikipedia.org/wiki/Delimiter-separated_values) and gives examples
of issues that can arises with data import into MS Excel and Google Sheets.

## 1 What data are you working with?
In research or in class (organic lab for instance) you may find yourself needing to a save a spectrum to a text file 
so that you can create a plot for a report.  Text files are extremely common for transferring data between computers,
can be written in different ways, and come with different extensions.  The reason text files are so popular is that
they are simple (it's just a file with text in it right?) and generally the best for 
[digital preservation](https://library.duke.edu/using/policies/recommended-file-formats-digital-preservation) (meaning
files that can be kept a long time and still be read by software).

However, there are situations where importing isn't easy, or worse where imported data gets corrupted. So, it is important
to know what data you are working with, and how best to important it accurately. First, you need to check the extension
(.xxx) that you are working with. While many files are text files they can have extension which dictates what type of
format the file is, and/or which type of software can open it.  Some common text file formats are:
- '.txt' : this is your basic text file which can be read by a general text editor such as; 'textedit' (macOS), 
  'Notepad' (Windows), 'textmate' ([macOS](https://macromates.com/)), 'Sublime Text' 
  ([macOS/Windows/Linux](https://www.sublimetext.com/))
- '.csv' : a text file that is specifically written to store data as 'comma separated variables'.  This means that data 
  is organized like a table.  Each row of the table is a line in the text file ends in a
  [newline character](https://en.wikipedia.org/wiki/Newline), which varies between different computer systems.  Then columns
  on the line are separated by a comma, with text in a column being surrounded by double quotes if there is a comma in
  the text.  On Windows a .csv file will automatically launch in MS Excel if present and into Apple Numbers if present
  and then MS Excel for Mac.  You can also read these files in the text editors above, but you have to pick the text editor,
  rather than just double-clicking the file, to use the text editor.
- '.tsv' : the same as '.csv' except the delimiter is a 'tab' character rather than a comma.
- '.json': a text file in the [JavaScript Object Notation (JSON)](https://en.wikipedia.org/wiki/JSON) format used to 
  store and identify data and metadata in a lightweight format that is commonly used to communicate between web browsers
  and servers in the background so content on the page can be updated without refreshing the page.  More recently, JSON 
  has become the de facto standard for serving data from websites [Application Programming Interface (API)](https://en.wikipedia.org/wiki/API)
  because it can be read by many programming languages and operating systems and can be made small without compression
  using the stringify feature, where extra space and newline characters can be removed.
- .xml : a text file in the [Extensible Markup Language (XML)](https://en.wikipedia.org/wiki/XML) format.  XML is a
  commonly used standard for encoding data in a tree structure using 'tags' like those used in HTML (see XHTML). XML
  has a large community of users, tools, and features like XPath [XML Path Language](https://en.wikipedia.org/wiki/XPath), 
  [XQuery (XML Query)](https://en.wikipedia.org/wiki/XQuery), 
  [XSLT (Extensible Stylesheet Language Transformations)](https://en.wikipedia.org/wiki/XSLT). Most important though is
  ability of XML documents to be validated against an [XML Schema](https://en.wikipedia.org/wiki/XML_schema), a set of 
  XML based rules that dictate what can be stored in an XML file that is an instance of a specific XML schema.
- '.jdx' : a JCAMP-DX text file that stores instrument data according to a specific format (see...). This is one of many
  chemical data file formats, many of which are discussed [here](https://en.wikipedia.org/wiki/Chemical_file_format).

Files with the extension .csv  or .tsv are examples of 'delimited' text files.  Delimiting simply means separating data
into chunks (e.g., columns in a table) in a text string or line of text in a file, using a specific character.  For a
.csv file the character is a comma (hence comma separated variable) and a .tsv file the character is a tab (hence tab 
separated variable).  Any character can be a delimiter, however in practice the comma and tab are the most common, and
many pieces of software, and scripting languages know how to read them.

## 2 Importing into Microsoft Excel
When dealing with chemical data it is important to make sure you don't corrupt the data as you process it.  This is
easier to do than you might think, and very difficult to find after the fact.  Here are some important pointers about
working with data in Microsoft Excel.

### 2.1 File encoding format
First, only text based files can be imported into a spreadsheet, so make sure that the file is not a binary file. Next,
it is good to check in a text editor what the file encoding is.  In Figure 1 below, Excel can handle many different
encoding formats, but in order to import them correctly you should use the .txt file extension as Excel will automatically
import .csv, .tsv and other files and not let you choose what the encoding is.  Depending on your computers' operating
system there may be some selections that won't work on your computer.

Figure 1
![fig1](../images/excel_import_fig1.jpg)
Caption: The Excel import dialog (a) and the options for 'File origin' (b)

Using the open file dialog is important if your text file contains unicode (e.g., UTF-8).  If you double-click on a .csv,
.tsv, or other file with an extension that Excel automatically recognizes, the file will be opened without giving you 
the option to choose UTF-8 as the encoding format.  This results in 'weird characters' (technical term ;) ) showing up in your 
imported file (see Figure 2a).  However, if you change the extension of such a file to '.txt' and then open it from within
Excel you will be able to use the dialog in Figure 1a to choose the correct encoding and make sure that the text shows
correctly in Excel (see Figure 2b).

Figure 2
![fig2](../images/excel_import_fig2.jpg)
Caption: Importing a unicode (UTF-8) '.csv' file into Excel directly (a), and using the Excel file oping dialog (b)

### 2.2 End of line characters
Although less of an issue these days, you may want to check the end-of-line encoding (Figure 3) that is used in the file.
This can result in extra blank lines begin added by Excel to the imported file when the file has both a 'carriage return'
CR character, and a 'line-feed' LF character is at the end of line.

Figure 3
![fig3](../images/excel_import_fig3.jpg)
Caption: Different end-of-line character options from a text file. 

### 2.3 Data types in Excel
During the import of a text file, via the open dialog, you are presented with other choices as you work through importing 
the file.  On the last dialog you get to choose the format of each column of data in the file.  Figure 4a shows the 
choices available, and you can click on the header of each column (or multiple columns) to assign a data type.  For
chemical data this is particularly important when importing CAS Registry Numbers (CASRN's), as some CASRN's can be
misinterpreted as dates if the column data type is left as 'General'.  In this situation, change the data format to 
'Text' and the CASRN's will all be imported correctly (see Figure 4a).  You can also force this in the .csv file by
addin quotes around the CASRN and adding a '='before the first quote (Figure 4b).

Figure 4
![fig4](../images/excel_import_fig4.jpg)
Caption: CASRNs in (4a) and advanced options for interpretting numeric values (4b)

```{Note}
If you want to find out how prevalent CASRN's being misinterpreted as dates, use this 
[link](https://query.wikidata.org/#%23All%20CAS%20registry%20numbers%20in%20Wikidata%0ASELECT%20DISTINCT%20%3Fcompound%20%3FcompoundLabel%20%3Fcas%0AWHERE%0A%7B%0A%20%20%3Fcompound%20wdt%3AP231%20%3Fcas%20.%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22en%22.%20%7D%0A%7D%0ALIMIT%201000) 
to run a SPARQL query (search) on Wikidata, that retrieves the first 1000 compounds with a CASRN.  Click the 'Run' 
button on the left of the page then export the data as .csv from the 'Download' menu on the right.  Open the file
in Excel and see how many of the 1000 compounds have CASRN's formatted as dates.
```

Figure 5b shows the dialog when you are importing a file in Excel and in Step 3 you click on the Advanced button. If you
receive data from collaborators in other countries, you may need to change the way Excel identifies numeric values, as 
there are differences between countries on the use of the full stop/period '.' and the comma as 
[formatting characters](https://en.wikipedia.org/wiki/Decimal_separator).

As an example, the value one thousand, two hundred and thirty-four point fifty-six is represented:
- In English-speaking countries and Asia as: 1,234.56
- In Latin America and continental Europe as: 1.234,56

Figure 5
![fig5](../images/excel_import_fig5.jpg)
Caption: Data types for columns in Excel (a) and advanced options for interpretting numeric values (b)


## 3 Importing into Google Sheets
In general Google Sheets is less susceptible to these issues, however if you are doing research at any level make sure
to check with your advisor about putting research data in Google sheets, as many advisors are reluctant to store
research data in a cloud based service (also, Dropbox, OneDrive, Box, etc.) for fear of others getting access.