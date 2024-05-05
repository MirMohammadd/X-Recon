import tamper.inverse


def apply_tamper(payload):
    if payload:
        return tamper.inverse.tamper(payload)
    return payload