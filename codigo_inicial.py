# ===== Celda 1: crear el Excel =====
# !pip install supabase openpyxl -q   (quita el # si lo corres en Colab)
import pandas as pd

df = pd.DataFrame({"nombre": ["Ana", "Luis"], "edad": [25, 30]})
df.to_excel("datos.xlsx", index=False)

# ===== Celda 2: subirlo a Supabase (Storage) =====
from supabase import create_client

sb = create_client("https://TU_PROYECTO.supabase.co", "TU_API_KEY")

with open("datos.xlsx", "rb") as f:
    sb.storage.from_("archivos").upload("datos.xlsx", f.read(),
        {"content-type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "upsert": "true"})

# ===== Opcion: guardar los datos en una tabla en vez del archivo =====
# (la tabla "personas" debe existir con las columnas nombre y edad)
# sb.table("personas").insert(df.to_dict("records")).execute()
