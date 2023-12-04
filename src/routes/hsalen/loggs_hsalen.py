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
from fastapi import APIRouter, HTTPException

from src.services import db

# Logging
from src.domain.hsalen.private import LoggingPrivate
from src.domain.hsalen.public import LoggingPublic

# Create a router for handling Mediji related endpoints
router = APIRouter()


# ROUTES FOR PRIVATE PAGES

# GET ALL PRIVATE LOGS
@router.get("/private", operation_id="get_all_private_logs_hsa")
async def get_all_private_logs_hsalen() -> list[LoggingPrivate]:
    """
    This route handles the retrieval of all blogs from the database.

    Behavior:
    - Retrieves all blogs from the database.
    - Returns a list of Blog objects.
    """

    # Retrieve all blogs from the database
    cursor = db.private_hsa.logging_private.find()
    return [LoggingPrivate(**document) for document in cursor]


# ADD NEW PRIVATE LOG
@router.post("/private", operation_id="add_private_log_hsa")
async def post_one_private_log(logs: LoggingPrivate) -> LoggingPrivate | None:
    """
    This route adds a new log to the database.

    Parameters:
    - logs (Logging): The log object to be added.

    Behavior:
    - Adds a new log to the database.
    - Returns the added Logging object if successful, or None if unsuccessful.
    """

    # Add a new log to the database
    log_dict = logs.dict(by_alias=True)
    insert_result = db.private_hsa.logging_private.insert_one(log_dict)

    # Check if the insertion was acknowledged and update the log's ID
    if insert_result.acknowledged:
        log_dict['_id'] = str(insert_result.inserted_id)
        return LoggingPrivate(**log_dict)
    else:
        return None


# DELETE PRIVATE LOG BY ID
@router.delete("/private/{_id}", operation_id="delete_private_log_admin")
async def delete_private_log_admin(_id: str):
    """
    Route to delete a log by its ID from the database.

    Arguments:
        _id (str): The ID of the log to be deleted.
        current_user (str): The current authenticated user.

    Returns:
        dict: A message indicating the status of the deletion.

    Raises:
        HTTPException: If the log is not found for deletion.
        :param _id: ID of the log
    """

    # Attempt to delete the log from the database
    delete_result = db.private_hsa.logging_private.delete_one({'_id': _id})

    # Check if the blog was successfully deleted
    if delete_result.deleted_count > 0:
        return {"message": "Log deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail=f"Log by ID:({_id}) not found")


# DELETE ALL PRIVATE LOGS
@router.delete("/private", operation_id="delete_all_private_logs")
async def delete_all_private_logs():
    return db.private_hsa.logging_private.drop()


# ROUTES FOR PUBLIC PAGES

# GET ALL PUBLIC LOGS
@router.get("/public", operation_id="get_all_public_logs_hsa")
async def get_all_public_logs_hsalen() -> list[LoggingPublic]:
    """
    This route handles the retrieval of all blogs from the database.

    Behavior:
    - Retrieves all blogs from the database.
    - Returns a list of Blog objects.
    """

    # Retrieve all blogs from the database
    cursor = db.public_hsa.logging_public.find()
    return [LoggingPublic(**document) for document in cursor]


# ADD NEW PUBLIC LOG
@router.post("/public", operation_id="add_public_log_hsa")
async def post_one_public_log(logs: LoggingPublic) -> LoggingPublic | None:
    """
    This route adds a new log to the database.

    Parameters:
    - logs (Logging): The log object to be added.

    Behavior:
    - Adds a new log to the database.
    - Returns the added Logging object if successful, or None if unsuccessful.
    """

    # Add a new log to the database
    log_dict = logs.dict(by_alias=True)
    insert_result = db.public_hsa.logging_public.insert_one(log_dict)

    # Check if the insertion was acknowledged and update the log's ID
    if insert_result.acknowledged:
        log_dict['_id'] = str(insert_result.inserted_id)
        return LoggingPublic(**log_dict)
    else:
        return None


# DELETE PUBLIC LOG BY ID
@router.delete("/public/{_id}", operation_id="delete_public_log_admin")
async def delete_public_log_admin(_id: str):
    """
    Route to delete a log by its ID from the database.

    Arguments:
        _id (str): The ID of the log to be deleted.
        current_user (str): The current authenticated user.

    Returns:
        dict: A message indicating the status of the deletion.

    Raises:
        HTTPException: If the log is not found for deletion.
        :param _id: ID of the log
    """

    # Attempt to delete the log from the database
    delete_result = db.public_hsa.logging_public.delete_one({'_id': _id})

    # Check if the blog was successfully deleted
    if delete_result.deleted_count > 0:
        return {"message": "Log deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail=f"Log by ID:({_id}) not found")


# DELETE ALL PUBLIC LOGS
@router.delete("/public", operation_id="delete_all_public_logs")
async def delete_all_public_logs():
    return db.public_hsa.logging_public.drop()
