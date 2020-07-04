import json
with open('keys.json') as f:
    data = json.load(f)

username=data['username']
pswd=data['pswd']
host=data['host']
port=5432
database=data['database']
cnxn_string=f"""postgresql+psycopg2://{username}:{pswd}@{host}:{port}/{database}"""
engine = create_engine(cnxn_string)
