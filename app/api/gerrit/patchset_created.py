



async def patchset_created_api():
    """
    @brief: This is called whenever a patchset is created(this includes new changes and drafts)
    patchset-created --change <change id>
                     --is-draft <boolean>
                     --kind <change kind>
                     --change-url <change url>
                     --change-ower <change owner>
                     --project <project name>
                     --branch <branch>
                     --topic <topic>
                     --uploader <uploader>
                     --commit <sha1>
                     --patchset <patchset id>
        change kind represents kind of change uploaded,
            REWORK - Nontrivial content changes.
            TRIVIAL_REBASE - Conflict-free merge between the new parent and prior patch set.
            NO_CODE_CHANGE - No code changed; same tree and same parent tree.
            NO_CHANGE - No changes; same commit message, same tree and same parent tree.
    """
    return {"action": "patchset_created"}
