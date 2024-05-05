def tamper(payload,**kwargs):
    retVal = payload
    if payload:
        return payload[::-1]

    return retVal

