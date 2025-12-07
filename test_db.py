from dotenv import load_dotenv
import os, psycopg2, sys

load_dotenv()  # reads .env in project root if present

# DEBUG: PRINT WHAT .env LOADED
print("\n### ENV VALUES LOADED ###")
print("POSTGRES_USER:", os.getenv("POSTGRES_USER"))
print("POSTGRES_PASSWORD:", os.getenv("POSTGRES_PASSWORD"))
print("POSTGRES_DB:", os.getenv("POSTGRES_DB"))
print("POSTGRES_HOST:", os.getenv("POSTGRES_HOST"))
print("POSTGRES_PORT:", os.getenv("POSTGRES_PORT"))
print("DATABASE_URL:", os.getenv("DATABASE_URL"))
print("#########################\n")

# Prefer explicit DATABASE_URL, fallback to components
dsn = os.getenv("DATABASE_URL") or (
    f"postgresql://{os.getenv('POSTGRES_USER','admin')}:"  
    f"{os.getenv('POSTGRES_PASSWORD','admin123')}@"
    f"{os.getenv('POSTGRES_HOST','localhost')}:" 
    f"{os.getenv('POSTGRES_PORT','5432')}/"
    f"{os.getenv('POSTGRES_DB','bloodwork')}"
)

print("DSN:", dsn)
try:
    conn = psycopg2.connect(dsn)
    print("Connected (status):", conn.status)
    conn.close()
    sys.exit(0)
except Exception as e:
    print("Connection failed:", type(e).__name__, e)
    sys.exit(1)

