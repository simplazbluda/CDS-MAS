"""
MedicalAI Database Models

Stores patients, encounters,
clinical notes and AI recommendations.
"""


from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Boolean,
    DateTime,
    Date,
    ForeignKey
)

from sqlalchemy.orm import relationship

from .base import Base



class Patient(Base):
    """
    Patient demographic information.
    """

    __tablename__ = "patients"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    first_name = Column(
        String,
        nullable=False
    )


    last_name = Column(
        String,
        nullable=False
    )


    date_of_birth = Column(
        Date,
        nullable=True
    )


    gender = Column(
        String,
        nullable=True
    )


    phone = Column(
        String,
        nullable=True
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    encounters = relationship(
        "Encounter",
        back_populates="patient",
        cascade="all, delete"
    )



class Encounter(Base):
    """
    Represents a patient visit.
    """

    __tablename__ = "encounters"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    patient_id = Column(
        Integer,
        ForeignKey("patients.id"),
        nullable=False
    )


    chief_complaint = Column(
        Text,
        nullable=True
    )


    symptoms = Column(
        Text,
        nullable=True
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    patient = relationship(
        "Patient",
        back_populates="encounters"
    )


    clinical_note = relationship(
        "ClinicalNote",
        back_populates="encounter",
        uselist=False,
        cascade="all, delete"
    )


    recommendations = relationship(
        "AIRecommendation",
        back_populates="encounter",
        cascade="all, delete"
    )



class ClinicalNote(Base):
    """
    Stores AI-generated and doctor-edited notes.
    """

    __tablename__ = "clinical_notes"


    id = Column(
        Integer,
        primary_key=True
    )


    encounter_id = Column(
        Integer,
        ForeignKey("encounters.id"),
        nullable=False
    )


    ai_generated_note = Column(
        Text,
        nullable=True
    )


    doctor_edited_note = Column(
        Text,
        nullable=True
    )


    approved = Column(
        Boolean,
        default=False
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    encounter = relationship(
        "Encounter",
        back_populates="clinical_note"
    )



class AIRecommendation(Base):
    """
    Stores outputs from AI agents.
    """

    __tablename__ = "ai_recommendations"


    id = Column(
        Integer,
        primary_key=True
    )


    encounter_id = Column(
        Integer,
        ForeignKey("encounters.id"),
        nullable=False
    )


    agent_name = Column(
        String,
        nullable=True
    )


    recommendation = Column(
        Text,
        nullable=True
    )


    confidence = Column(
        String,
        nullable=True
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    encounter = relationship(
        "Encounter",
        back_populates="recommendations"
    )