import json
import time
import os
from drivers.neo4j_connector import Neo4jPulsar

def ejecutar_latido_con_sentido():
    db = Neo4jPulsar()
    
    # Ruta absoluta al JSON de hexagramas
    ruta_json = "/content/drive/MyDrive/elPulsar_Project/logic/hexagramas.json"
    
    with open(ruta_json, 'r') as f:
        data = json.load(f)
        nodos = data['nodos_maestros']

    # Nodo 1: CREATIVO
    nodo_actual = nodos[0]

    try:
        start_time = time.time()
        time.sleep(0.1) 
        latencia = time.time() - start_time

        db.registrar_latido(
            id_hex=nodo_actual['id'],
            latencia=latencia,
            msg=f"Protocolo {data['protocolo']}: Actuando como {nodo_actual['tag']}"
        )
        print(f"✅ Latido resonante: {nodo_actual['tag']} ({nodo_actual['descripcion']})")
    except Exception as error_latido:
        print(f"❌ Error al registrar en Neo4j: {error_latido}")
    finally:
        db.close()

if __name__ == "__main__":
    ejecutar_latido_con_sentido()