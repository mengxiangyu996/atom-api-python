from src.dal.database import _Database
from src.dal.redis import _Redis

db: _Database | None = None
rds: _Redis | None = None


def init_dabatase(db_url: str):
    global db
    db = _Database(db_url)

def close_database():
    if db:
        db.close()

def init_redis(rds_url: str):
    global rds
    rds = _Redis(rds_url)

def close_redis():
    if rds:
        rds.close()