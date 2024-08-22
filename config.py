import utils

db_password = utils.get_db_password('db_pass.txt')

db_config = {
    'uri': f'mongodb+srv://{db_password}@cluster0.x1x8qhv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0',  
    'dbname': 'inzynierka',
    'collection': 'sample_airbnb'
}

db_query = {"property_type": "house"}

results_path = 'results'
downloads_path = 'downloads'
statistics_path = 'statistics'
test_data_path = 'test_data'