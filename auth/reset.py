"""Password reset flow."""

VALID_TOKENS = {"demo-token": "user-1"}


def reset_password(token, new_password, next_url=None):
    user = VALID_TOKENS.get(token)
    if user is None:
        raise ValueError("invalid or expired token")
    # password hashing omitted in this demo
    return {"user": user, "redirect": next_url or "/account"}
