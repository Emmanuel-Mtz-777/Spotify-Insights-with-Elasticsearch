from elasticsearch import Elasticsearch
from elasticsearch import helpers
import json

class ElasticSearchProvider:

    def __init__(self):
        self.host = "http://localhost:9200"
        #self.user = str(user)
        #self.password = str(password)
        self.index = "spotify-insights"
        self.index_type ="_doc"
        self.connection = Elasticsearch(self.host)

    def __enter__(self):
        try:
            self.connection=Elasticsearch(self.host)
            return self
        except Exception as e:
            return{
                "StatusCode":500,
                "body":json.dumps({
                    "Message":str(e)
                })
            }

    def insertDataJson(self, file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    documents = [
                        {"_index": self.index, "_source": json.loads(line.strip())}
                        for line in file
                    ]
                if documents:
                    helpers.bulk(self.connection, documents)
                    print(f"{len(documents)} documentos insertados en {self.index}")
            except Exception as e:
                print(f"Error al insertar datos: {str(e)}")
    
    def showMostPopularbyGenre(self):
        try:
            response=self.connection.search(
                index=self.index,
                body={
                    "size": 0,
                    "aggs": {
                        "top_genres": {
                        "terms": {
                            "field": "genre",
                            "size": 10
                        },
                        "aggs": {
                            "top_tracks": {
                            "top_hits": {
                                "size": 10,
                                "_source": ["track_name", "artist_name", "popularity"]
                                }
                            }
                        }
                    }
                }
            }
            )
            return response
            
        except Exception as e:
            print(f"Error: {str(e)}")
            
    def showMostPopularbyArtist(self,name):
        try:
            response=self.connection.search(
                index=self.index,
                body={
                    "size": 5,
                    "query": {
                        "match": {
                        "artist_name": name 
                        }
                    },
                    "aggs": {
                        "top_tracks": {
                        "terms": {
                            "field": "track_name.keyword",  
                        },
                        "aggs": {
                            "popular_tracks": {
                            "top_hits": {
                                "size": 5,
                                "_source": ["track_name", "popularity"]
                            }
                            }
                        }
                        }
                    }
                }
            )
            return response
            
        except Exception as e:
            print(f"Error: {str(e)}")

    def __exit__(self, exception_type, exception_value, traceback):
        self.connection.transport.close()



