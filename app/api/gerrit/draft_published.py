


async def draft_published_api():
    """
    @brief: This is called whenever a draft change is published.
    draft-published --change <change id>
                    --change-url <change url>
                    --change-owner <change owner>
                    --project <project name>
                    --branch <brach>
                    --topic <topic>
                    --uploader <uploader>
                    --commit <sha1>
                    --patchset <patchset id>
    """
    return {"action": "draft_published"}
