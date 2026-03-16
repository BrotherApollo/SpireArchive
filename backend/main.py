from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from pydantic import BaseModel
from datetime import datetime
import os

# DB connection
DATABASE_URL = os.getenv("DATABASE_URL", "")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True)
    played_at = Column(DateTime, default=datetime.now())
    difficulty = Column(String(50), nullable=False)
    won = Column(Boolean, nullable=False)
    floors_cleared = Column(Integer, nullable=False)
    elites_killed = Column(Integer, nullable=False)
    gold_gained = Column(Integer, nullable=False)

class MatchPlayer(Base):
    __tablename__ = "match_players"

    id = Column(Integer, primary_key=True)
    match_id = Column(Integer, ForeignKey("matches.id"), nullable=False)
    player_id = Column(Integer, ForeignKey("players.id"), nullable=False)
    character = Column(String(50), nullable=False)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

# Schemas
class PlayerCreate(BaseModel):
    name: str

class PlayerResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

# Routes
@app.post("/players", response_model=PlayerResponse)
def create_player(player: PlayerCreate, db: Session = Depends(get_db)):
    db_player = Player(name=player.name)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player