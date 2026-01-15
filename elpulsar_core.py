import json
import time
from drivers.neo4j_connector import Neo4jPulsar

def ejecutar_latido_con_sentido():
    db = Neo4jPulsar()
    
    # Leemos tu herencia de GitHub
    with open('logic/hexagramas.json', 'r') as f:
        data = json.load(f)
        nodos = data['nodos_maestros']
    
    # Elegimos un nodo basado en tu protocolo (ej: el 1 CREATIVO)
    nodo_actual = nodos[0] 
    
    try:
        start_time = time.time()
        # Lógica de simulación de proceso...
        latencia = time.time() - start_time
        
        db.registrar_latido(
            id_hex=nodo_actual['id'],
            latencia=latencia,
            msg=f"Protocolo {data['protocolo']}: Actuando como {nodo_actual['tag']}"
        )
        print(f"✅ Latido resonante: {nodo_actual['tag']} ({nodo_actual['descripcion']})")
    finally:
        db.close()

if __name__ == "__main__":
    ejecutar_latido_con_sentido()