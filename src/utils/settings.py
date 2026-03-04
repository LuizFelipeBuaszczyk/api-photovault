import os
from dotenv import load_dotenv

load_dotenv()

# Necessário deixar explicito que não será DEBUG no ambiente de produção
DEBUG = os.getenv("DEBUG", True)

MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT", "")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY", "")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY", "")