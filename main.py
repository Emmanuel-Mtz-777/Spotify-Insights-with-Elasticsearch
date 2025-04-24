from elasticSearchProvider import ElasticSearchProvider

def main():
    instance1()

def insert_by_json():
    try:
        update_data="spotify_data.json"
        with ElasticSearchProvider() as es:
            response = es.insertDataJson(update_data)
    except Exception as e:
        print("Ocurrió un error: " + str(e))
        
def instance1():
    provider = ElasticSearchProvider()
    response = provider.showMostPopularbyGenre()
    if response:
        print("Respuesta obtenida:")
        print(response)
    else:
        print("No se obtuvo respuesta válida.")

if __name__ == "__main__":
    main()