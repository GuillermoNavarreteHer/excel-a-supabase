# Excel a Supabase

Crea un archivo Excel con Python y lo sube a Supabase Storage.

## Archivos

| Archivo | Para que sirve |
|---|---|
| `subir_excel.ipynb` | Notebook para abrir en Google Colab |
| `codigo_inicial.py` | El codigo original de 2 celdas (+ opcion de tabla) |
| `subir_excel.py` | El mismo codigo como script normal |
| `requirements.txt` | Librerias necesarias |

## Preparar Supabase (una sola vez)

1. **Project Settings → API**: copia la *Project URL*.
2. **Project Settings → API Keys**: copia la *service_role* / *secret key*.
3. **Storage → New bucket**: crea uno llamado `archivos`.

## Usar en Colab

1. Abre [colab.research.google.com](https://colab.research.google.com) → *Archivo → Subir notebook* → `subir_excel.ipynb`.
2. Pega tu URL y tu clave en la celda de configuracion.
3. Ejecuta las celdas en orden.
4. Revisa en Supabase: **Storage → archivos → datos.xlsx**.

## Usar en tu computadora

```bash
pip install -r requirements.txt
export SUPABASE_URL="https://TU_PROYECTO.supabase.co"
export SUPABASE_KEY="TU_API_KEY"
python subir_excel.py
```

> ⚠️ Nunca subas tu clave secreta a GitHub.
