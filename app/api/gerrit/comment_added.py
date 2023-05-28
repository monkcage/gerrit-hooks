


async def comment_added_api():
    """
    @brief: This is called whenever a comment is added to a change.
    comment-added --change <change id>
                  --is-draft <boolean>
                  --change-url <change url>
                  --change-owner <change owner>
                  --project <project name>
                  --brach <branch>
                  --topic <topic>
                  --author <comment author>
                  --commit <commit>
                  --comment <comment>
                  [--<approval category id> <score> ...]
    """
    return {"action": "comment_added"}
