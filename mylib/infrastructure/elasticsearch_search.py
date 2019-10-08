from elasticsearch import Elasticsearch


class ElasticsearchSearch:

    def __init__(self, elasticsearch: Elasticsearch, index: str):
        self._elasticsearch = elasticsearch
        self._index = index

    def search(self, query: str) -> dict:
        results = self._elasticsearch.search(
            index=self._index,
            body={
                "query": {
                    "simple_query_string" : {
                        "query" : "{0}".format(query)
                    }
                }
            }
        )

        documents = []
        for r in results['hits']['hits']:
            documents.append({
                "id": r['_id'],
                "file_path": r['_source']['original_file_path']
            })

        return documents
