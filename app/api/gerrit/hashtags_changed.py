


async def hashtags_changed_api():
    """
    @brief: Called whenever hashtags are added to or removed from a change from the Web UI or via the REST API.
    hashtags-changed --change <change id>
                     --change-owner <change owner>
                     --project <project name>
                     --branch <branch>
                     --editor <editor>
                     --added <hashtag>
                     --removed <hashtag>
                     --hashtag <hashtag>
    """
    return {"action": "hashtags_changed"}
