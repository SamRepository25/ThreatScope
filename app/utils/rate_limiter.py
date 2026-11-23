import time

# Stores: {user_id: {command: last_used_timestamp}}
_user_cooldowns = {}


def is_rate_limited(user_id: int, command: str, cooldown: int):
    """
    Check whether a user is currently rate limited.

    Returns:
        (True, seconds_left)  -> if still on cooldown
        (False, 0)            -> if command can be used
    """

    now = time.time()

    user_data = _user_cooldowns.setdefault(user_id, {})
    last_used = user_data.get(command)

    if last_used is not None:
        elapsed = now - last_used

        if elapsed < cooldown:
            remaining = int(cooldown - elapsed) + 1
            return True, remaining

    user_data[command] = now
    return False, 0