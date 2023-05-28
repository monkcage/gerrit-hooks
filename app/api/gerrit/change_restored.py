


async def change_restored_api():
    """
    @brief: Called whenever a change has been restored.
    change-restored --change <change id>
                    --change-url <change url>
                    --change-owner <change owner>
                    --project <project name>
                    --branch <branch>
                    --topic <topic>
                    --restorer <restorer>
                    --commit <sha1>
                    --reason <reason>
    """
    return {"action": "change_restored"}
