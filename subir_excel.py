import os
import pandas as pd
from supabase import create_client

# 1. Configuracion (pon tus datos o usa variables de entorno)
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://TU_PROYECTO.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "TU_API_KEY")
BUCKET = "archivos"
ARCHIVO = "datos.xlsx"

# 2. Crear el Excel
df = pd.DataFrame({"nombre": ["Ana", "Luis"], "edad": [25, 30]})
df.to_excel(ARCHIVO, index=False)
print("Excel creado:", ARCHIVO)

# 3. Subirlo a Supabase Storage
sb = create_client(SUPABASE_URL, SUPABASE_KEY)
with open(ARCHIVO, "rb") as f:
    sb.storage.from_(BUCKET).upload(ARCHIVO, f.read(), {
        "content-type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "upsert": "true",
    })
print("Subido a Supabase en el bucket:", BUCKET)
