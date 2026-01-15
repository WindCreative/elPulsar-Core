
import random
import datetime

class ElPulsarCore:
    def __init__(self, uri, user, password):
        from neo4j import GraphDatabase
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def ejecutar_latido(self, tx):
        hex_id = random.randint(1, 64)
        ahora = datetime.datetime.now()
        
        # Lógica de Secuencia: Buscamos el último latido para encadenar el nuevo
        query = """
        MATCH (h:Hexagrama {id: $hid})
        OPTIONAL MATCH (ultimo:Latido)
        WITH h, ultimo ORDER BY ultimo.timestamp DESC LIMIT 1
        CREATE (n:Latido {timestamp: $ts, id: $hid})-[:REPRESENTA]->(h)
        WITH n, ultimo
        FOREACH (_ IN CASE WHEN ultimo IS NOT NULL THEN [1] ELSE [] END |
            CREATE (n)-[:SIGUE_A]->(ultimo)
        )
        RETURN n.id
        """
        result = tx.run(query, hid=hex_id, ts=ahora)
        return result.single()[0]

    def obtener_datos_servicio(self, tx):
        # Traemos los últimos 10 latidos con su latencia simulada para Amelia
        query = """
        MATCH (l:Latido)
        RETURN l.id AS id, l.timestamp AS ts
        ORDER BY l.timestamp DESC LIMIT 10
        """
        res = tx.run(query)
        import datetime
        # Simulamos una latencia para el historial (en producción sería real)
        return [{'id': r['id'], 'ts': r['ts'].to_native(), 'lat': 0.05} for r in res]
