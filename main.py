from elasticSearchProvider import ElasticSearchProvider

def main():
    insert_by_json()

def insert_by_json():
    try:
        update_data="spotify_data.json"
        with ElasticSearchProvider() as es:
            response = es.insertDataJson(update_data)
    except Exception as e:
        print("Ocurrió un error: " + str(e))

if __name__ == "__main__":
    main()