from protocol.timeout import TimeoutHandler
from config import RESPONSE_WINDOW

request_height = 10

print("=== Timeout Experiment ===\n")

for current_height in [20, 40, 60, 80]:
    status = TimeoutHandler.status(
        current_height=current_height,
        request_height=request_height,
        response_window=RESPONSE_WINDOW,
    )

    print(
        f"Current Height: {current_height:2d} | "
        f"Status: {status}"
    )