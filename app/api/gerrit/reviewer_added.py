


async def reviewer_added_api():
    """
    @brief: Called whenever a reviewer is added to a change
    reviewer-added --change <change id>
                   --change-url <change url>
                   --change-owner <change owner>
                   --project <project name>
                   --branch <branch>
                   --reviewer <reviewer>
    """
    return {"action": "reviewer_added"}
