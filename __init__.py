"""ComfyUI-IdolGlue: write a native ComfyUI gaussian splat to a .ply on disk and return its path as a STRING,
so it can be handed to path-based exporters (e.g. Meshsmuggler's SmuggleMeshAsImage)."""

from comfy_api.latest import ComfyExtension
from typing_extensions import override

from .nodes import NODES


class IdolGlueExtension(ComfyExtension):
    @override
    async def get_node_list(self):
        return NODES


async def comfy_entrypoint():
    return IdolGlueExtension()
