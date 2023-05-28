


async def cla_signed_api():
    """
    @brief: Called whenever a user signs a contributor license agreement.
    cla-signed --submitter <submitter>
               --user-id <user_id>
                --cla-id <cla_id>
    """
    return {"action": "cla_signed"}
