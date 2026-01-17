
import random
import datetime
from drivers.neo4j_connector import Neo4jPulsar

class ElPulsarCore:
    def __init__(self):
        self.db = Neo4jPulsar()

    def close(self):
        self.db.close()

    def gates_h5_sync(self):
        """H5: Sincronización Ocular - Captura de metadato temporal"""
        return datetime.datetime.now().isoformat()

    def zipper_h56_validation(self, id_evento):
        """H56: Cierre de Licitud (Zipper) - Blindaje final"""
        # Según el Tomo Maestro, todo proceso WORK debe cerrar aquí.
        print(f"🔒 [H56-ZZ] ZIPPER: Validación de salida para evento {id_evento}.")
        return "[H56-ZZ]"

    def work_h6_process(self, hex_id, ts):
        """H6: Conflicto/Trabajo - Escritura en el STACK de Neo4j"""
        with self.db.driver.session() as session:
            query = """
            MATCH (h:Hexagrama {id_hex: $hid})
            OPTIONAL MATCH (ultimo:Latido)
            WITH h, ultimo ORDER BY ultimo.timestamp DESC LIMIT 1
            CREATE (n:Latido {
                timestamp: datetime($ts),
                id_hex: $hid,
                token: "[H06-50]"
            })
            CREATE (n)-[:REPRESENTA]->(h)
            WITH n, ultimo
            FOREACH (_ IN CASE WHEN ultimo IS NOT NULL THEN [1] ELSE [] END |
                CREATE (n)-[:SIGUE_A]->(ultimo)
            )
            RETURN n.token as token
            """
            result = session.run(query, hid=hex_id, ts=ts)
            record = result.single()
            return record['token'] if record else "[H06-50]"

    def ejecutar_ciclo_maestro_con_mask(self, hex_id, intensidad_evento):
        """Implementación del Filtro H52 (The Mask) en el flujo de trabajo"""

        # 1. GATES (H5): Sincronización inicial
        ts = self.gates_h5_sync()

        # 2. MASK (H52): Evaluación de Quietud vs Acción
        # Si la intensidad es baja, Amelia impone Quietud para proteger los 12GB RAM
        if intensidad_evento < 0.5:
            print(f"🏔️ [Q52-00] MASK: Quietud impuesta (Hexagrama {hex_id}). Evento filtrado.")
            return "[Q52-00]"

        # 3. WORK (H6): Solo si la MASK es superada se procede al registro
        token_work = self.work_h6_process(hex_id, ts)
        print(f"✨ [H06-50] WORK: Latido registrado en el grafo.")

        # 4. ZIPPER (H56): Validación de salida obligatoria
        token_zip = self.zipper_h56_validation(hex_id)

        return f"{token_work} >> {token_zip}"
