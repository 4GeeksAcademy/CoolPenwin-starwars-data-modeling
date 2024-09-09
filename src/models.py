import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Enum, create_engine
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    nick_name = Column(String(250))
    first_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250))
    liked_items = relationship("Liked", back_populates="user")

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String(250))
    population = Column(Integer)
    climate = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(Integer)
    films = relationship("Films", back_populates="planets")
    liked_items = relationship("Liked", back_populates="planets")

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    starship_class = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(String(250))
    length = Column(String(250))
    crew = Column(String(250))
    passengers = Column(String(250))
    max_atmosphering_speed = Column(Integer)
    hyperdrive_rating = Column(String(250))
    MGLT = Column(String(250))
    cargo_capacity = Column(String(250))
    consumables = Column(String(250))
    pilots = Column(String(250))
    films = relationship("Films", back_populates="starships")
    liked_items = relationship("Liked", back_populates="starships")

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height = Column(String(250))
    mass = Column(String(250))
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))
    homeworld = Column(String(250))
    force_side = Column(String(250))
    films = relationship("Films", back_populates="characters")
    liked_items = relationship("Liked", back_populates="characters")

class Films(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    episode_num = Column(Integer)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    starships_id = Column(Integer, ForeignKey('starships.id'))
    vehicles_id = Column(Integer)
    species_id = Column(Integer, ForeignKey('species.id'))
    release_date = Column(Integer)
    director = Column(String(250))
    
    characters = relationship('Characters', back_populates="films")
    planets = relationship('Planets', back_populates="films")
    starships = relationship('Starships', back_populates="films")
    species = relationship('Species', back_populates="films")

class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    classification = Column(String(250))
    designation = Column(String(250))
    average_height = Column(String(250))
    average_lifespan = Column(String(250))
    hair_colors = Column(String(250))
    skin_colors = Column(String(250))
    eye_colors = Column(String(250))
    homeworld = Column(String(250))
    language = Column(String(250))
    people_id = Column(Integer)
    films = relationship("Films", back_populates="species")
    liked_items = relationship("Liked", back_populates="species")

class Liked(Base):
    __tablename__ = 'liked'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    item_id = Column(Integer, primary_key=True)
    
    user = relationship('User', back_populates="liked_items")
    characters = relationship('Characters', back_populates="liked_items")
    planets = relationship('Planets', back_populates="liked_items")
    starships = relationship('Starships', back_populates="liked_items")
    species = relationship('Species', back_populates="liked_items")


## Draw from SQLAlchemy base
try:

    result = render_er(Base, 'diagram.png')
    print("FUKING Success! Check the diagram.png file")
except Exception as e:
    print("There was a FUKING problem generating the FUKING diagram")
    raise e