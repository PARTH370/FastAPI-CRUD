import os
import orjson
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv(".env")

Base = declarative_base()

def orjson_serializer(obj):
    return orjson.dumps(
        obj, option=orjson.OPT_SERIALIZE_NUMPY | orjson.OPT_NAIVE_UTC
    ).decode()

SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    json_serializer=orjson_serializer,
    json_deserializer=orjson.loads,
    connect_args={},
)

SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
)

async def get_db():
    async with SessionLocal() as session:
        yield session
