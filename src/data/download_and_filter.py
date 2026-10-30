import os
import pandas as pd

# Rutas locales dentro de la estructura del proyecto
METADATA_DIR = os.path.join("data", "metadata")
RAW_CSV_PATH = os.path.join(METADATA_DIR, "cryptic_metadata_raw.csv")

# URL oficial de la EBI (compendio 2024)
EBI_URL = "https://ftp.ebi.ac.uk/pub/databases/cryptic/release_june2022/reuse/CRyPTIC_reuse_table_20240917.csv"

def obtener_datos():
    """Carga la tabla desde el disco local si existe; si no, la descarga de la EBI."""
    os.makedirs(METADATA_DIR, exist_ok=True)
    
    if os.path.exists(RAW_CSV_PATH):
        print(f"✔ Cargando datos desde el disco local: {RAW_CSV_PATH}")
        df = pd.read_csv(RAW_CSV_PATH)
    else:
        print("--> Archivo no encontrado en disco. Descargando desde el servidor de la EBI...")
        df = pd.read_csv(EBI_URL)
        df.to_csv(RAW_CSV_PATH, index=False)
        print(f"✔ Descarga guardada en: {RAW_CSV_PATH}")
        
    return df

if __name__ == "__main__":
    df = obtener_datos()
    print(f"✔ Total de registros: {df.shape[0]} muestras x {df.shape[1]} columnas")