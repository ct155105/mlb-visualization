from pymongo import MongoClient

client = MongoClient('mongo-db')
db = client.mlb


def write_day_to_db(year: int, day: dict) -> str:
    '''Writes the day document to a collection called "year_" with the year parameter as suffix
    
    Args:
        year: The year of the season the day belongs to
        day: The day dictionary object that contains the teams / current standings / etc

    Returns:
        The ID of the row inserted
    '''


    collection = db['year_' + str(year)]
    post_id = collection.insert_one(day).inserted_id
    return post_id


def print_season(year: int) -> None:
    '''prints to console the specified season results
    
    Args:
        year: The year of the season to print

    Returns:
        None
    '''

    collection = db['year_' + str(year)]
    for c in collection.find():
        print(c)

def get_season(year: int) -> list:
    '''Returns a list of dict objects for the specified season results
    
    Args:
        year: The year of the season to print

    Returns:
        list: A list of dictionary objects. Each dictionary is a given day of the season.
    '''

    collection = db['year_' + str(year)]

    results = []
    for c in collection.find({},{'_id':0}):
        results.append(c)

    results.sort(key=lambda x: (x['date']['year'] * 10000) + (x['date']['month'] * 100) + (x['date']['day']) )

    return results