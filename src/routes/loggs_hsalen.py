"""
This module defines API routes for managing blogs.

Routes:
1. GET all blogs
2. GET blog by ID
3. ADD a new blog
4. Edit an existing blog by ID
5. Delete a blog by ID
"""

# Import necessary modules and classes
from fastapi import APIRouter

from src.services import db

# Logging
from src.domain.logging import Logging

# Create a router for handling Mediji related endpoints
router = APIRouter()


# GET ALL BLOG
@router.get("/", operation_id="get_all_logs_hsalen")
async def get_all_logs_hsalen() -> list[Logging]:
    """
    This route handles the retrieval of all blogs from the database.

    Behavior:
    - Retrieves all blogs from the database.
    - Returns a list of Blog objects.
    """

    # Retrieve all blogs from the database
    cursor = db.proces.logging.find()
    return [Logging(**document) for document in cursor]
