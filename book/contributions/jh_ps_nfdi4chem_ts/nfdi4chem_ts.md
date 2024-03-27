Authors: [Johannes Hunold](https://orcid.org/0000-0002-4378-6061), [Philip Strömert](https://orcid.org/0000-0002-1595-3213)

# About NFDI4Chem

[NFDI4Chem](https://www.nfdi4chem.de/) is the Chemistry Consortium in the National Research Data Infrastructure for Germany [NFDI](https://www.nfdi.de/?lang=en) (German: **N**ationale **F**orschungs**D**aten**I**nfrastruktur), a project launched in 2018 and funded by the German government to build a national research data infrastructure in Germany for a wide range of scientific disciplines. The vision of NFDI4Chem is to digitize all key steps in chemical research to support scientists in their efforts to collect, store, process, analyze, publish, and reuse research data. Actions to promote open science and research data management (RDM) in line with the [FAIR data principles](https://www.go-fair.org/fair-principles/) are fundamental objectives of NFDI4Chem to provide the chemistry community with a holistic approach to research data access. To this end, the overall goal is to develop and maintain innovative and user-friendly services and novel scientific approaches based on the reuse of research data. NFDI4Chem aims to represent all disciplines of chemistry in academia and therefore works closely with thematically related NFDI consortia.

# NFDI4Chem Terminology Service

Research data is not just a collection of numbers or images in a scientific journal article, experimental section, or supplementary information. To fully comprehend the deduction of results and enable the exploration of new data-driven, interdisciplinary research questions, access to the raw data and knowledge of how it was generated, processed, and analyzed is essential. Research data needs to be FAIR (**F**indable, **A**ccessible, **I**nteroperable, **R**eusable) for both humans and machines. Achieving machine-usable FAIR research data requires extensive metadata annotation, which describes the data and its context. To semantically describe research data, ontologies, taxonomies, terminologies, or vocabularies can be used, playing an important role in creating semantically rich, discipline-specific metadata. In addition, consensual definitions of entities are formed, ensuring conceptual alignment across domains, even if the nomenclature of the individual domains is different. Please visit the [NFDI4Chem Knowledge Base article about Ontology](https://knowledgebase.nfdi4chem.de/knowledge_base/docs/ontology/?_highlight=terminol#sources-and-further-information) to learn more about this topic.

Using terminologies for data annotation presents a significant challenge as it requires selecting the appropriate terms from the available terminologies. To make an informed decision, one must either possess prior knowledge of the suitable terminologies and terms for a specific scientific context and use case or acquire this knowledge by browsing the available terminologies. A terminology service is a tool for browsing terminologies that aims to make them understandable to humans. Therefore, it should provide detailed information about the terminologies and the terms they contain. This is particularly important when comparing multiple terminologies that cover the same or overlapping areas of knowledge. Terminology users must be able to recognize the semantic differences and similarities, as well as the interdependencies between terminologies, to make informed decisions. Although there are many sophisticated terminology services available, such as the [Basic Register of Thesauri, Ontologies & Classifications (BARTOC)](https://bartoc.org/) or the [Ontology Lookup Service (OLS)](https://www.ebi.ac.uk/ols4), they contain a large selection of different terminologies and ontologies that can overwhelm domain experts.

The [NFDI4Chem Terminology Service (TS)](https://terminology.nfdi4chem.de/ts/) only indexes terminologies that are most relevant to chemistry using various parameters such as subject area relevance and license to facilitate domain experts' selection. Additionally, the NFDI4Chem TS provides functions that go beyond simple search and provision of ontologies, enabling collaborative curation and management. To minimize the risk of losing track, users can list or write GitHub issues directly from the TS. If an ontology is not maintained on GitHub or if additional contextual information is desired, users can write notes at the ontology or term level to make open issues, recommendations, or insights more visible to themselves and others.

Using the example of "[mass concentration](https://terminology.nfdi4chem.de/ts/search?and=false&sorting=title&page=1&size=10&q=mass+concentration)", a search in the NFDI4Chem TS yields almost 6,000 results. However, selecting the "Exact Match" option reduces the number of results to 6 (see [Figure 1](../images/NFDI4Chem_TS_fig1.png)).

![Figure 1: Screenshot of the result list obtained by searching for the term "mass concentration" in the NFDI4Chem TS with the "Exact Match" option.](../images/NFDI4Chem_TS_fig1.png)

Of the 6 results, the option "Unit of Mass Concentration" is unsuitable as it only describes the unit. Therefore, only 5 options remain, all of which are in principle suitable for semantically describing the term "mass concentration". However, the term ["mass concentration" defined in the Chemical Methods Ontology (CHMO)](https://terminology.nfdi4chem.de/ts/ontologies/chmo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHMO_0002821&obsoletes=false) appears to be the most appropriate, as it is already used by another ontology, as indicated by the "Also in" field. This example briefly illustrates how the NFDI4Chem TS assists chemists in identifying and selecting the most appropriate terminology for their specific use case.
In addition to the previously described use case of using the NFDI4Chem TS through the Graphical User Interface (GUI), the TS can also be utilized by other services, such as [Electronic Lab Notebooks (ELNs)](https://knowledgebase.nfdi4chem.de/knowledge_base/docs/eln/), through the provided [Application Programming Interface (API)](https://terminology.nfdi4chem.de/ts/api). In addition to the search functionality, the Terminology Service API provides other functions for interacting with indexed ontologies. For example, the autocomplete or direct select function can be used to populate forms or dropdown menus. The interactive [Swagger documentation](https://service.tib.eu/ts4tib/swagger-ui.html#/) documents all available API functions and allows for live testing.

To implement the search example above in Python using the NFDI4Chem TS API, follow these steps:

```
import requests
import urllib

class ChemSearch:
def __init__(self, query, exactMatch, page, size):
    	self.query = urllib.parse.quote_plus(query)
    	self.exactMatch = exactMatch
    	self.rows = size
    	self.start = page
    	self.collection = "NFDI4CHEM"
self.base_api_url = "https://service.tib.eu/ts4tib/api/
			search?groupField=iri&&schema=collection"
    	search_result = []
    	search_facet = []
    
    
	def run(self):
    	params = "&q={}&exact={}&start={}&rows={}&classification={}".format(
self.query, 
self.exactMatch, 
self.start, 
self.rows, 
self.collection)
    	searchUrl = self.base_api_url + params
    	result = requests.get(searchUrl)
    	if result.status_code == 200:       	 
        	result = result.json()
        	self.search_result = result['response']
        	self.search_facet = result['facet_counts']['facet_fields']
        	return True

    	return False
   
    
	def get_number_of_found_result(self):
    	print(self.search_result['numFound'])
    	
return True
    
    
	def get_results(self):
    	for res in self.search_result['docs']:
        	print("Iri: " + res['iri'])
        	print("short_form: " + res['short_form'])
        	print("ontology_name: " + res['ontology_name'])
        	print("Type: " + res['type'])
    	
return True
    
    
	def get_facet(self):
    	for facet_name, facet_values in self.search_facet.items():
        	print("Facet Field Name: " + facet_name)
        	for i in range(len(facet_values)):
            	if i % 2 == 0:
                	print("facet item: " + facet_values[i])
            	else:
                	print("count: " + str(facet_values[i]))
   	 
    	return True
            	 
# running the above code
search = ChemSearch("mass concentration", True, 0, 40)
search.run()
search.get_number_of_found_result()
search.get_results()
search.get_facet()
```
