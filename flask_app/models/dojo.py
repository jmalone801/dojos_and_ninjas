from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__( self, data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        dojo = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return dojo

    @classmethod
    def all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []

        for x in results:
            dojos.append(cls(x))
        return dojos

    @classmethod
    def dojo_ninjas_join(cls,data):
        query = "SELECT * FROM ninjas LEFT JOIN dojos ON dojos.id = ninjas.dojo_id WHERE dojo_id = %(id)s"
        query_results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        dojo = cls(query_results[0])
        
        for dojo_ninja in query_results:
            ninja_data = {
                "id":dojo_ninja["id"],
                "first_name":dojo_ninja["first_name"],
                "last_name":dojo_ninja["last_name"],
                "age":dojo_ninja["age"],
                "dojo_id":dojo_ninja["dojo_id"],
                "created_at":dojo_ninja["created_at"],
                "updated_at":dojo_ninja["updated_at"]
            }
            dojo.ninjas.append(Ninja(ninja_data))
        return dojo

        



