
from MyDataBase import MyDatabase
from Constants import Constants

class CRUD:
    const = Constants()
    conn = MyDatabase(
            const.decrypt(Constants.e_host),
            int(const.decrypt(Constants.e_port)),
            const.decrypt(Constants.e_database),
            const.decrypt(Constants.e_user),
            const.decrypt(Constants.e_password)
        )
    
    def create_profile(self):
        sql  = '''
        CREATE TABLE IF NOT EXISTS defaultdb.profiles (
            idx INTEGER PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(255) NOT NULL,
            alias VARCHAR(255) NOT NULL,
            token VARCHAR(255) NOT NULL,
            birthdate DATE NOT NULL,
            email VARCHAR(255) NOT NULL,
            lang_code VARCHAR(10) NOT NULL,
            routine BOOLEAN NOT NULL,
            alarm BOOLEAN NOT NULL,
            inactivity_time INTEGER NOT NULL,
            inactivity_type VARCHAR(50) NOT NULL
        );  
'''
        result = self.conn.query(sql)
        print(result)

    def get_profile(self):
        sql = "SELECT idx, name, alias, token, birthdate, email, lang_code, `routine`, alarm, inactivity_time, inactivity_type" \
        " FROM defaultdb.profiles;"
        result = self.conn.query(sql) 
        print(result)

    def set_profile(self, name, alias, token, birthdate, email, lang_code, routine, alarm, inactivity_time, inactivity_type):
        sql = "INSERT INTO defaultdb.profiles " \
        "(name, alias, token, birthdate, email, lang_code, `routine`, alarm, inactivity_time, inactivity_type) " \
        "VALUES( '{}', '{}', '{}', '{}', '{}', '{}', {}, {}, {}, '{}');".format(
            name, alias, token, birthdate, email, lang_code, routine, alarm, inactivity_time, inactivity_type
            )
        result = self.conn.query(sql) 
        print(result)

    def update_profile(self, name, alias, token, birthdate, email, lang_code, routine, alarm, inactivity_time, inactivity_type, idx):
        sql = "UPDATE defaultdb.profiles " \
        "SET name='{}', alias='{}', token='{}', birthdate={}, email='{}', lang_code='{}', `routine`={}, alarm={}, inactivity_time={}, inactivity_type={} " \
        "WHERE idx={};".format(
            name, alias, token, birthdate, email, lang_code, routine, alarm, inactivity_time, inactivity_type, idx
            )

    def delete_profile(self, idx):
        sql = "DELETE FROM defaultdb.profiles " \
        "WHERE idx={};".format(idx)

crud = CRUD()
#crud.create_profile()
crud.set_profile("John Doe", "johndoe", "token123", "1990-01-01", "john.doe@example.com", "en", True, True, 300, "aaaa")
crud.set_profile("Juan Doe", "juandoe", "token12", "1981-03-09", "juan.doe@example.com", "en", True, True, 300, "bbbb")   
crud.set_profile("pedro Doe", "pedrodoe", "token13", "2008-06-28", "pedro.doe@example.com", "en", True, True, 300, "cccc")   
crud.set_profile("emma Doe", "emmadoe", "token14", "2001-11-17", "emma.doe@example.com", "en", True, True, 300, "dddd")   
crud.set_profile("gera Doe", "geradoe", "token15", "1996-02-06", "gera.doe@example.com", "en", True, True, 300, "eeee")   
crud.set_profile("cami Doe", "camidoe", "token16", "1972-04-07", "cami.doe@example.com", "en", True, True, 300, "ffff")   
crud.set_profile("alexa Doe", "alexadoe", "token17", "2004-08-15", "alexa.doe@example.com", "en", True, True, 300, "gggg")   
crud.set_profile("karen Doe", "karendoe", "token18", "1956-12-24", "karen.doe@example.com", "en", True, True, 300, "hhhh")   
crud.set_profile("jorge Doe", "jorgedoe", "token19", "1999-09-23", "jorge.doe@example.com", "en", True, True, 300, "iiii")   
crud.set_profile("deo Doe", "deodoe", "token20", "2002-01-18", "deo.doe@example.com", "en", True, True, 300, "jjjj")      