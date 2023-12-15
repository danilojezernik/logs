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
from fastapi import APIRouter, HTTPException, Depends, Query, status
from fastapi.responses import JSONResponse
from typing import Dict

import httpx
import asyncio

from src.domain.hsalen.backend import BackendLogs
from src.services import db

# Logging
from src.domain.hsalen.private import LoggingPrivate
from src.domain.hsalen.public import LoggingPublic

from src.services.security import get_current_user

# Create a router for handling Mediji related endpoints
router = APIRouter()


# ROUTES FOR PRIVATE PAGES

# GET ALL PRIVATE LOGS
@router.get("/private", operation_id="get_all_private_logs_hsa")
async def get_all_private_logs_hsalen(current_user: str = Depends(get_current_user)) -> list[LoggingPrivate]:
    """
    This route handles the retrieval of all blogs from the database.

    Behavior:
    - Retrieves all blogs from the database.
    - Returns a list of Blog objects.
    """

    # Retrieve all blogs from the database
    cursor = db.proces.logging_private.find()
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
    insert_result = db.proces.logging_private.insert_one(log_dict)

    # Check if the insertion was acknowledged and update the log's ID
    if insert_result.acknowledged:
        log_dict['_id'] = str(insert_result.inserted_id)
        return LoggingPrivate(**log_dict)
    else:
        return None


# DELETE PRIVATE LOG BY ID
@router.delete("/private/{_id}", operation_id="delete_private_log_admin")
async def delete_private_log_admin(_id: str, current_user: str = Depends(get_current_user)):
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
    delete_result = db.proces.logging_private.delete_one({'_id': _id})

    # Check if the blog was successfully deleted
    if delete_result.deleted_count > 0:
        return {"message": "Log deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail=f"Log by ID:({_id}) not found")


# DELETE ALL PRIVATE LOGS
@router.delete("/private", operation_id="delete_all_private_logs")
async def delete_all_private_logs(current_user: str = Depends(get_current_user)):
    result = db.proces.logging_private.delete_many({})
    return {"deleted_count": result.deleted_count}


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
    cursor = db.proces.logging_public.find()
    return [LoggingPublic(**document) for document in cursor]


# GET COUNT OF LOGS CONTAINING DEVICE TYPE IN CONTENT
@router.get("/count_logs_with_desktop", operation_id="count_logs_with_desktop")
async def count_logs_with_desktop(
        device_type: str = Query(..., description="Specify the device type (e.g., 'Mobile' or 'Desktop')")) -> Dict[
    str, int]:
    """
    This route handles the counting of logs containing a specified device type in the content.

    Behavior:
    - Counts the number of logs with the specified device type in the content.
    - Returns a dictionary with the count.
    """

    # Count logs with the specified device type in the content
    count = db.proces.logging_public.count_documents({"content": {"$regex": device_type, "$options": "i"}})

    return {"count": count}


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
    insert_result = db.proces.logging_public.insert_one(log_dict)

    # Check if the insertion was acknowledged and update the log's ID
    if insert_result.acknowledged:
        log_dict['_id'] = str(insert_result.inserted_id)
        return LoggingPublic(**log_dict)
    else:
        return None


# DELETE PUBLIC LOG BY ID
@router.delete("/public/{_id}", operation_id="delete_public_log_admin")
async def delete_public_log_admin(_id: str, current_user: str = Depends(get_current_user)):
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
    delete_result = db.proces.logging_public.delete_one({'_id': _id})

    # Check if the blog was successfully deleted
    if delete_result.deleted_count > 0:
        return {"message": "Log deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail=f"Log by ID:({_id}) not found")


# DELETE ALL PUBLIC LOGS
@router.delete("/public", operation_id="delete_all_public_logs")
async def delete_all_public_logs(current_user: str = Depends(get_current_user)):
    result = db.proces.logging_public.delete_many({})
    return {"deleted_count": result.deleted_count}


# ROUTES FOR BACKEND PAGES

# GET ALL BACKEND LOGS
@router.get("/backend", operation_id="get_all_backend_logs_hsa")
async def get_all_backend_logs_hsalen() -> list[BackendLogs]:
    """
    This route handles the retrieval of all blogs from the database.

    Behavior:
    - Retrieves all blogs from the database.
    - Returns a list of Blog objects.
    """

    # Retrieve all blogs from the database
    cursor = db.proces.backend_logs.find()
    return [BackendLogs(**document) for document in cursor]


# ADD NEW BACKEND LOG
@router.post("/backend", operation_id="add_backend_log_hsa")
async def post_one_backend_log(logs: BackendLogs) -> BackendLogs | None:
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
    insert_result = db.proces.backend_logs.insert_one(log_dict)

    # Check if the insertion was acknowledged and update the log's ID
    if insert_result.acknowledged:
        log_dict['_id'] = str(insert_result.inserted_id)
        return BackendLogs(**log_dict)
    else:
        return None


# DELETE BACKEND LOG BY ID
@router.delete("/backend/{_id}", operation_id="delete_backend_log_admin")
async def delete_backend_log_admin(_id: str, current_user: str = Depends(get_current_user)):
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
    delete_result = db.proces.backend_logs.delete_one({'_id': _id})

    # Check if the blog was successfully deleted
    if delete_result.deleted_count > 0:
        return {"message": "Log deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail=f"Log by ID:({_id}) not found")


# DELETE ALL BACKEND LOGS
@router.delete("/backend", operation_id="delete_all_backend_logs")
async def delete_all_backend_logs(current_user: str = Depends(get_current_user)):
    result = db.proces.backend_logs.delete_many({})
    return {"deleted_count": result.deleted_count}


# GET UNIQUE CLIENT HOSTS WITH VISIT COUNTS
@router.get("/unique_client_hosts", operation_id="get_unique_client_hosts")
async def get_unique_client_hosts():
    """
    This route handles the retrieval of unique client hosts and their visit counts.

    Behavior:
    - Returns a list of dictionaries containing client_host and count fields.
    """
    cursor = db.proces.backend_logs.find()
    unique_client_hosts = {}

    for document in cursor:
        client_host = document["client_host"]
        if client_host in unique_client_hosts:
            unique_client_hosts[client_host]["count"] += 1
        else:
            unique_client_hosts[client_host] = {"client_host": client_host, "count": 1}

    response_data = list(unique_client_hosts.values())
    return JSONResponse(content=response_data, status_code=200)


@router.get("/get_geolocation")
async def get_geolocation_route():
    try:
        # Fetch client hosts from the backend_logs collection
        client_hosts = db.proces.backend_logs.distinct("client_host")
        print(client_hosts)

        # Function to get geolocation data for a given IP address
        async def get_geolocation(ip_address: str) -> dict:
            url = f"https://ipinfo.io/{ip_address}/json"
            async with httpx.AsyncClient() as client:
                response = await client.get(url)
                if response.status_code == 200:
                    return response.json()
                else:
                    print('ERROR')
                    raise HTTPException(status_code=response.status_code, detail="Failed to fetch geolocation data function.")

        # Use asyncio.gather to concurrently fetch geolocation data for all client hosts
        tasks = [get_geolocation(client_host) for client_host in client_hosts]
        geolocation_data_list = await asyncio.gather(*tasks)

        # Return the list of geolocation data
        return geolocation_data_list

    except Exception as e:
        # Log the exception or handle it as needed
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to fetch geolocation data. Error: {str(e)}"
        )
