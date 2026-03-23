from fastapi import HTTPException, Request
import time


# configurable limits
UPLOAD_LIMIT = 3 # Max files per user in time frame
TIME_FRAME = 180  # 3 minutes

# Stores upload timestamps per user.
user_upload_log = {}


def check_upload_limit(request: Request, num_files: int):
    user_id = request.client.host
    now = time.time()

    # initialize user log if not exists
    if user_id not in user_upload_log:
        user_upload_log[user_id] = []

    # remove old uploads outside time frame for this user
    user_upload_log[user_id] = [
        t for t in user_upload_log[user_id] if now - t < TIME_FRAME
    ]

    # here we're checking if the user has exceeded the upload limit by comparing the number of files they are trying to upload with the number of uploads they have made within the defined time frame.
    if len(user_upload_log[user_id]) + num_files > UPLOAD_LIMIT:
        raise HTTPException(
            status_code=429,
            detail=f" You have exceeded the upload limit: max {UPLOAD_LIMIT} files per {TIME_FRAME//60} minutes"
        )

    # record upload
    user_upload_log[user_id].extend([now] * num_files)