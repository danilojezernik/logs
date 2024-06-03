# Import necessary modules and functions
from datetime import datetime, timedelta

from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from fastapi import Depends, HTTPException, status

from src.domain.user import User
from src import env
from src.domain.user_in_db import UserInDB
from src.api.token_data import TokenData
from src.services import db

# Initialize a password context with bcrypt hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Define OAuth2 password bearer scheme for authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Function to verify the provided plain password against the hashed password
def verify_password(plain_password, hashed_password):
    """
    This function verifies the provided plain password against the hashed password.

    Parameters:
    - plain_password: The plain password to verify.
    - hashed_password: The hashed password to compare against.

    Behavior:
    - It uses the verify method from the passlib context to compare the plain password with the hashed password.
    - Returns True if the plain password matches the hashed password, otherwise returns False.
    """
    return pwd_context.verify(plain_password, hashed_password)


# Function to get a user from the database based on the provided username
def get_user(username: str):
    """
    This function retrieves a user from the database based on the provided username.

    Parameters:
    - username (str): Username of the user to retrieve.

    Behavior:
    - It queries the database to find a user with the given username using the find_one method.
    - If a user is found, it constructs a UserInDB instance using the retrieved data and returns it.
    - If no user is found, it returns None.
    """
    user = db.proces.user_dict.find_one({"username": username})
    if user:
        return UserInDB(**user)


# Function to authenticate a user based on the provided username and password
def authenticate_user(username: str, password: str):
    """
    This function authenticates a user by validating the provided username and password.

    Parameters:
    - username (str): Username of the user to authenticate.
    - password (str): Password of the user to authenticate.

    Behavior:
    - It retrieves the user based on the provided username using the get_user function.
    - If a user is found and the provided password matches the stored hashed password, the user is considered authenticated and returned.
    - If no user is found or the password doesn't match, it returns None, indicating authentication failure.
    """
    user = get_user(username)
    if user and verify_password(password, user.hashed_password):
        return user
    return None


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """
    This function is responsible for creating an access token (JWT) using the jwt.encode function from the jose library.

    Parameters:
    - data: A dictionary containing the data to be encoded into the token (e.g., user information).
    - expires_delta: An optional parameter indicating the expiration time for the token.

    Behavior:
    - Calculates the expiration time for the token based on the provided expires_delta or defaults to 15 minutes if no expiration is provided.
    - Updates the data dictionary with the expiration time.
    - Encodes the updated data into a JWT using the jwt.encode function with the provided SECRET_KEY and ALGORITHM.

    Returns:
    - The encoded JWT (access token) as the result of the function.
    """

    # Make a copy of the data to encode
    to_encode = data.copy()

    # Calculate the expiration time for the token
    if expires_delta:
        # If an expiration delta is provided, calculate the expiration time
        expire = datetime.utcnow() + expires_delta
    else:
        # If no expiration delta is provided, default to 15 minutes expiration
        expire = datetime.utcnow() + timedelta(minutes=60)

    # Update the data with the expiration time
    to_encode.update({"exp": expire})

    # Encode the data into a JWT using the provided SECRET_KEY and algorithm
    encoded_jwt = jwt.encode(to_encode, env.SECRET_KEY, algorithm=env.ALGORITHM)

    # Return the encoded JWT (access token)
    return encoded_jwt


async def get_payload(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, env.SECRET_KEY, algorithms=["HS256"])
    except JWTError:
        raise credentials_exception
    return payload


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    """
    Asynchronously retrieves the current user based on the provided token.

    Steps:
    1. Creates an exception to handle authentication failures (credentials_exception).
    2. Decodes the token to extract the username (subject), handling potential exceptions.
    3. Attempts to retrieve the user from the database based on the extracted username.
    4. If the user is not found, raises an exception indicating authentication failure.
       Otherwise, the user is returned.
    """

    # Create an exception for handling authentication failures
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        # Decode the token and extract the username (subject)
        payload = jwt.decode(token, env.SECRET_KEY, algorithms=[env.ALGORITHM])
        username: str = payload.get("sub")

        if username is None:
            # Raise an exception if username is not found in the token
            raise credentials_exception

        # Create token data based on the extracted username
        token_data = TokenData(username=username)
    except JWTError:
        # Raise an exception if token decoding fails
        raise credentials_exception

    # Get user based on the username extracted from the token
    user = get_user(token_data.username)

    if user is None:
        # Raise an exception if the user is not found in the database
        raise credentials_exception

    return user


async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    """
    This asynchronous function checks if the provided user is active.

    Behavior:
    - If the user is inactive (disabled), it raises an exception indicating an inactive user.
    - Otherwise, if the user is active, it simply returns the current user.
    """

    # Check if the user is inactive
    if current_user.disabled:
        # Raise an exception if the user is inactive
        raise HTTPException(status_code=400, detail="Inactive user")

    # Return the current user if active
    return current_user
