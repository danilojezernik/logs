from datetime import timedelta
from typing import Annotated

from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from src.api.token import Token
from src.services.security import authenticate_user, create_access_token

# Create a new APIRouter instance for this module
router = APIRouter()


# Route for user authentication and obtaining an access token
@router.post("/", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    """
    This route handles user authentication by validating the provided credentials (username and password).
    If the credentials are correct, it generates an access token and returns it to the client.

    Args:
        form_data (OAuth2PasswordRequestForm): The user's credentials.

    Returns:
        dict: A dictionary containing the access token and its type.
    """

    # Authenticate the user using the provided username and password
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        # Raise an exception if the authentication fails
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Set the expiration time for the access token to 30 minutes
    access_token_expires = timedelta(minutes=30)

    # Create an access token for the authenticated user
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    # Return the access token and token type
    return {"access_token": access_token, "token_type": "bearer"}
