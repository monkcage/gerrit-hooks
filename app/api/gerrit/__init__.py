
from fastapi import APIRouter
from .change_abandoned import change_abandoned_api
from .change_merged import change_merged_api
from .change_restored import change_restored_api
from .cla_signed import cla_singed_api
from .comment_added import comment_added_api
from .draft_published import draft_published_api
from .hashtags_changed import hashtags_changed_api
from .merge_failed import merge_failed_api
from .patchset_created import patchset_created_api
from .ref_updated import ref_updated_api
from .reviewer_added import reviewer_added_api
from .topic_changed import topic_changed_api

router = APIRouter(
    prefix = "/hook"
)


router.add_api_route("/change_abandoned", change_abandoned_api, methods=["POST"])
router.add_api_route("/change_merged", change_merged_api, methods=["POST"])
router.add_api_route("/change_restored", change_restored_api, methods=["POST"])
router.add_api_route("/cla_signed", cla_signed_api, methods=["POST"])
router.add_api_route("/comment_added", comment_added_api, methods=["POST"])
router.add_api_route("/draft_published", draft_published_api, methods=["POST"])
router.add_api_route("/hashtags_changed", hashtags_changed_api, methods=["POST"])
router.add_api_route("/merge_failed", merge_failed_api, methods=["POST"])
router.add_api_route("/patchset_created", patchset_created_api, methods=["POST"])
router.add_api_route("/ref_updated", ref_updated_api, methods=["POST"])
router.add_api_route("/reviewer_added", reviewer_added_api, methods=["POST"])
router.add_api_route("/topic_changed", topic_changed_api, methods=["POST"])
