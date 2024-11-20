import psycopg2
from sqlalchemy import create_engine, insert, text

engine = create_engine("postgresql+psycopg2://sarvagya:sarvagya@dtt-db:5432/dtt_data", future=True)
conn = engine.connect()
print('Connection Estabilished')

def add_new_user(username, email, password):
    sql = f'''insert into users (username, email, password_hash) 
            values ('{username}', '{email}', '{password}');'''
    conn.execute(text(sql))
    conn.commit()
    return 

def user_login(username, password):
    sql = f'''select password_hash from users where username = '{username}';'''
    try: 
        result = conn.execute(text(sql)).fetchone()
        db_pass_hash = result['password_hash']
        if(password == db_pass_hash):
            return True
    except: 
        return False