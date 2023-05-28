


async def ref_updated_api():
    """
    @brief: This is called when a push request is received by Gerrit.
    ref-update --project <project name>
               --refname <refname>
               --uploader <uploader>
               --oldrev <sha1>
               --newrev <sha1>
    """
    return {"action": "ref_updated"}
