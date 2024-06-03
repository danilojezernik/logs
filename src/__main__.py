"""
This script starts a FastAPI application using Uvicorn server.

Steps:
1. Imports necessary modules and libraries.
2. Configures FastAPI application with a base path and openapi tags.
3. Adds CORS middleware for handling Cross-Origin Resource Sharing.
4. Sets the secret key for the FastAPI application.
5. Includes various routers for different functionalities (blog, login, admin, mediji).
6. If the script is run directly (not imported), it drops the database and seeds it, then starts the Uvicorn server.
"""

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src import env
from src.routes import login
from src.routes.hsalen import loggs_hsalen
from src.routes.portfolio_dj import portfolio_dj
# from src.services import db
from src.tags_metadata import tags_metadata

app = FastAPI(openapi_tags=tags_metadata)

# Configure CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include various routers for different functionalities
app.include_router(loggs_hsalen.router, prefix="/logs_hsa", tags=['Hypnosis Studio Alen'])
app.include_router(portfolio_dj.router, prefix="/portfolio_dj", tags=['Hypnosis Studio Alen'])

app.include_router(login.router, prefix="/login")

print("this is the updated version")

if __name__ == '__main__':
    # Drop the database and seed it
    # db.drop_log()
    # db.seed_log()
    

    # Run the FastAPI application using Uvicorn server
    uvicorn.run(app, host="0.0.0.0", port=env.PORT)
