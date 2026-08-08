class TimeoutHandler:

    @staticmethod
    def expired(
        current_height: int,
        request_height: int,
        response_window: int,
    ) -> bool:

        return (current_height - request_height) > response_window

    @staticmethod
    def status(
        current_height: int,
        request_height: int,
        response_window: int,
    ) -> str:

        if TimeoutHandler.expired(
            current_height,
            request_height,
            response_window,
        ):
            return "TIMEOUT"

        return "ACTIVE"