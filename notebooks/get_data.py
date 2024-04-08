
import sqlalchemy
import api_info

username = api_info.USERNAME
password = api_info.PASSWORD
host = api_info.HOST
port = api_info.PORT
db_name = api_info.DB_NAME
endpoint = 'postgresql://' + username + ':' + password + '@' + host + ':' + port + '/' + db_name
engine = sqlalchemy.create_engine(endpoint)
