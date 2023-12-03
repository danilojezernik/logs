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
@router.get("/", operation_id="get_all_logs_hsa")
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


# Add blog for Admin
@router.post("/", operation_id="add_log_hsa")
async def post_one_log(logs: Logging) -> Logging | None:
    """
    This route adds a new log to the database.

    Parameters:
    - logs (Logging): The log object to be added.

    Behavior:
    - Adds a new log to the database.
    - Returns the added Logging object if successful, or None if unsuccessful.
    """

    # Add a new blog to the database
    log_dict = logs.dict(by_alias=True)
    insert_result = db.proces.logging.insert_one(log_dict)

    # Check if the insertion was acknowledged and update the blog's ID
    if insert_result.acknowledged:
        log_dict['_id'] = str(insert_result.inserted_id)
        return Logging(**log_dict)
    else:
        return None
