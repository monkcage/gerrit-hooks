


async def change_merged_api():
    """
    @brief: Called whenever a change has been merge.
    change-merged --change <change id>
                  --change-url <change url>
                  --change-owner <change owner>
                  --project <project name>
                  --branch <branch>
                  --topic <topic>
                  --submitter <submitter>
                  --commit <sha1>
    """
    return {"action": "change_merged"}
