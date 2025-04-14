import httpx
from fastapi import Depends, HTTPException, Header, status

USER_SERVICE_URL = "http://localhost:8002"  # Adjust based on your User Service host/port

async def verify_token(Authorization: str = Header(...)):
    try:
        headers = {"Authorization": Authorization}
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{USER_SERVICE_URL}/validate", headers=headers)

        if response.status_code != 200:
            raise HTTPException(status_code=401, detail="Invalid or expired token")

        return response.json()  # contains email, username, etc.

    except httpx.RequestError:
        raise HTTPException(status_code=500, detail="User service unavailable")
