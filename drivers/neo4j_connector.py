import os
from neo4j import GraphDatabase
from google.colab import userdata

class Neo4jPulsar:
    def __init__(self):
        self.uri = userdata.get('NEO4J_URI')
        self.user = userdata.get('NEO4J_USER')
        # Buscamos 'NEO4J_PASS' para coincidir con tus secretos
        self.password = userdata.get('NEO4J_PASS')
        self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))

    def close(self):
        self.driver.close()

    def registrar_latido(self, id_hex, latencia, msg):
        with self.driver.session() as session:
            return session.execute_write(self._crear_y_conectar_latido, id_hex, latencia, msg)

    @staticmethod
    def _crear_y_conectar_latido(tx, id_hex, latencia, msg):
        query = """
        MATCH (last:Latido)
        WITH last ORDER BY last.timestamp DESC LIMIT 1
        CREATE (new:Latido {
            id_hex: $id_hex,
            latencia: $latencia,
            mensaje: $msg,
            timestamp: datetime()
        })
        MERGE (new)-[:SIGUE_A]->(last)
        RETURN new
        """
        return tx.run(query, id_hex=id_hex, latencia=latencia, msg=msg).single()