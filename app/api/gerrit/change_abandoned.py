


async def change_abandoned_api():
    """
    @brief: Called whenever a change has been abandoned.
    change-abandoned --change <change id>
                     --change-url <change url>
                     --change-owner <change owner>
                     --project <project name>
                     --branch <branch>
                     --topic <topic>
                     --abandoner <abandoner>
                     --commit <sha1>
                     --reason <reason>
    """
    return {"action": "change_abandoned"}
