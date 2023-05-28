


async def merge_failed_api():
    """
    @brief: Called whenever a change has failed to merge.
    change-failed --change <change id>
                  --change-url <change url>
                  --change-owner <change owner>
                  --project <project name>
                  --branch <branch>
                  --topic <topic>
                  --submitter <submitter>
                  --commit <sha1>
                  --reason <reason>
    """
    return {"action": "merge_failed"}
