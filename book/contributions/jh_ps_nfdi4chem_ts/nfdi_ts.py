""" Code to create a NFDI4Chem Terminology Service search class based on the service API """
# The code below has been formatted using the best practices for coding in Python
# found at https://peps.python.org/pep-0008/  "PEP 8 – Style Guide for Python Code"

# import the Python packages needed to run this code
import requests
import urllib.parse


#
class ChemSearch:
    def __init__(self, query, exactMatch, page, size):
        """ Initialize (configure) parameters for the API search """
        self.query = urllib.parse.quote_plus(query)
        self.exactMatch = exactMatch
        self.rows = size
        self.start = page
        self.collection = "NFDI4CHEM"
        self.base_api_url = "https://service.tib.eu/ts4tib/api/search?groupField = iri & & schema = collection"
        self.search_result = []
        self.search_facet = []

    def run(self):
        """ Run the search on the terminology server and load results into the 'search_result' attribute """
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
        """ Display the number results are found """
        print(self.search_result['numFound'])
        return True

    def get_results(self):
        """ Display the search result data """
        for res in self.search_result['docs']:
            print("Iri: " + res['iri'])
            print("short_form: " + res['short_form'])
            print("ontology_name: " + res['ontology_name'])
            print("Type: " + res['type'])
        return True

    """ Its not clear what this code does """
    # def get_facet(self):
    #     for facet_name, facet_values in self.search_facet.items():
    #         print("Facet Field Name: " + facet_name)
    #         for i in range(len(facet_values)):
    #             if i % 2 == 0:
    #                 print("facet item: " + facet_values[i])
    #             else:
    #                 print("count: " + str(facet_values[i]))
    #     return True


# This code uses the Class developed above to run a search for the term "mass concentration"
search = ChemSearch("mass concentration", True, 0, 40)
search.run()
search.get_number_of_found_result()
search.get_results()
