"""Password reset flow."""

VALID_TOKENS = {"demo-token": "user-1"}


def reset_password(token, new_password):
    user = VALID_TOKENS.get(token)
    if user is None:
        raise ValueError("invalid or expired token")
    # password hashing omitted in this demo
    return {"user": user, "redirect": "/account"}
