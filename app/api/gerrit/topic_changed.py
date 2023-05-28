


async def topic_changed_api():
    """
    @brief: Called whenever a change's topic is changed from the Web UI or via the REST API.
    topic-changed --change <change id>
                  --change-onwer <change owner>
                  --project <project name>
                  --branch <branch>
                  --changer <changer>
                  --old-topic <old topic>
                  --new-topic <new topic>
    """
    return {"action": "topic_changed"}
