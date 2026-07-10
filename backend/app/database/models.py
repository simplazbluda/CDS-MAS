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
        String
    )

    gender = Column(
        String
    )

    phone = Column(
        String
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    encounters = relationship(
        "Encounter",
        back_populates="patient"
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
        ForeignKey("patients.id")
    )

    chief_complaint = Column(
        Text
    )

    symptoms = Column(
        Text
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
        uselist=False
    )


    recommendations = relationship(
        "AIRecommendation",
        back_populates="encounter"
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
        ForeignKey("encounters.id")
    )


    ai_generated_note = Column(
        Text
    )


    doctor_edited_note = Column(
        Text
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
        ForeignKey("encounters.id")
    )


    agent_name = Column(
        String
    )


    recommendation = Column(
        Text
    )


    confidence = Column(
        String
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    encounter = relationship(
        "Encounter",
        back_populates="recommendations"
    )