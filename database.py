from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ✅ Connexion directe à la base PostgreSQL (sans .env)
DATABASE_URL = "postgresql://postgres:saif12345@localhost:5432/moviedb"

# Création du moteur de connexion SQLAlchemy
engine = create_engine(DATABASE_URL)

# Création de la session pour gérer les transactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Déclaration de la base pour les modèles ORM
Base = declarative_base()

# Fonction pour obtenir une session de DB (avec gestion du contexte)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
