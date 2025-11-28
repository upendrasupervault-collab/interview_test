
# Define a custom exception InvalidOrderException with fields order_id and reason.
# Raise this exception from endpoint /orders/{order_id} if order_id < 1000.
# Use FastAPI’s app.exception_handler to handle this globally.
# Return a structured JSON response:


class InvalidOrderException(Exception):
    def __init__(self, order_id: int, reason: str):
        self.order_id = order_id
        self.reason = reason
    def __str__(self):
        return f"Order ID: {self.order_id}, Reason: {self.reason}"

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.status import HTTP_429_TOO_MANY_REQUESTS
from starlette.middleware.base import BaseHTTPMiddleware
from time import time
from collections import defaultdict
app = FastAPI()
@app.exception_handler(InvalidOrderException)
async def invalid_order_exception_handler(request: Request, exc: InvalidOrderException):
    return JSONResponse(
        status_code=400,
        content={
            "error": "Invalid Order",
            "order_id": exc.order_id,
            "reason": exc.reason
        }
    )
@app.get("/orders/{order_id}")
async def get_order(order_id: int):
    if order_id < 1000:
        raise InvalidOrderException(order_id, "Order ID must be >= 1000")
    return {"order_id": order_id, "status": "valid"}

# Implement a custom rate limiter middleware for FastAPI.
class RateLimiterMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, max_requests: int, window_seconds: int):
        super().__init__(app)
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.clients = defaultdict(list)

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        current_time = time()
        request_times = self.clients[client_ip]

        # Remove timestamps outside the current window
        while request_times and request_times[0] <= current_time - self.window_seconds:
            request_times.pop(0)

        if len(request_times) >= self.max_requests:
            return JSONResponse(
                status_code=HTTP_429_TOO_MANY_REQUESTS,
                content={"message": "Too Many Requests"}
            )

        request_times.append(current_time)
        response = await call_next(request)
        return response
app.add_middleware(RateLimiterMiddleware, max_requests=5, window_seconds=10)
@app.get("/data")
async def get_data():
    return {"message": "Request successful"}

