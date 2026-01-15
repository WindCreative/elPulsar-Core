
import datetime
from fpdf import FPDF

class AmeliaSentinel:
    def __init__(self, driver):
        self.driver = driver
        self.inicio = datetime.datetime.now()

    def reset_y_sutura(self, tx):
        # El Mantra Maestro para emergencias
        return tx.run("MERGE (u:Propietario {id: 'Owner_Master'}) SET u.mantra_activo = 'Vuelo Seguro elPulsar' RETURN '✅ Sistema Re-Suturado a Nivel Base.'").single()[0]

    def login_vocal(self, tx, mantra):
        res = tx.run("MATCH (u:Propietario {id: 'Owner_Master'}) RETURN u.mantra_activo AS m").single()
        lat = (datetime.datetime.now() - self.inicio).total_seconds()
        return (True, lat) if res and res['m'] == mantra else (False, lat)

    def ejecutar_auto_sutura(self, tx):
        nuevo_mantra = "EMERGENCIA_DELTA_9"
        tx.run("MATCH (u:Propietario {id: 'Owner_Master'}) SET u.mantra_activo = $m", m=nuevo_mantra)
        return f"🚨 AUTO-SUTURA: Mantra de seguridad elevado a {nuevo_mantra}"

    def analizar_memoria_selectiva(self, historial):
        if not historial: return "SISTEMA INICIADO", "NEUTRAL"
        actual = historial[0]['id']
        if len(historial) >= 2:
            previo = historial[1]['id']
            if actual % 2 != 0 and previo % 2 != 0:
                return "CRÍTICO: Inestabilidad detectada (Doble Impar).", "CRITICO"
        if actual == 52: return "ÓPTIMO: Sincronía Total.", "OPTIMO"
        return "ESTABLE: Flujo Dinámico.", "ESTABLE"

    def generar_reporte_consolidado(self, decision, nivel, historial, path):
        pdf = FPDF()
        pdf.add_page(); pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt="REPORTE DE SERVICIO ELPULSAR", ln=True, align='C')
        pdf.ln(10); pdf.set_font("Arial", 'B', 12)
        pdf.cell(200, 10, txt=f"DIAGNOSTICO: {decision}", ln=True)
        pdf.cell(200, 10, txt=f"NIVEL DE RIESGO: {nivel}", ln=True)
        pdf.ln(5); pdf.set_font("Arial", 'B', 10)
        pdf.cell(30, 8, "Hex", 1); pdf.cell(100, 8, "Timestamp", 1); pdf.cell(40, 8, "Latencia", 1); pdf.ln()
        pdf.set_font("Arial", size=9)
        for r in historial:
            pdf.cell(30, 7, str(r['id']), 1); pdf.cell(100, 7, r['ts'].strftime('%Y-%m-%d %H:%M:%S'), 1)
            pdf.cell(40, 7, f"{r['lat']:.4f}", 1); pdf.ln()
        pdf.output(path)
        return f"📄 Fuente de servicio guardada en: {path}"
