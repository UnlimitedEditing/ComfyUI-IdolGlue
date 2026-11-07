import os

import folder_paths
from comfy_api.latest import IO


class IdolSplatSavePLYPath(IO.ComfyNode):
    @classmethod
    def define_schema(cls):
        return IO.Schema(
            node_id="IdolSplatSavePLYPath",
            display_name="Idol Splat -> PLY Path",
            category="3d/idol",
            description="Serializes a gaussian splat (batch item 0) to a standard 3DGS .ply in the output folder "
                        "and returns the file path as a STRING.",
            inputs=[
                IO.Splat.Input("splat"),
                IO.String.Input("filename_prefix", default="idol_splat"),
            ],
            outputs=[IO.String.Output(display_name="ply_path")],
        )

    @classmethod
    def execute(cls, splat, filename_prefix) -> IO.NodeOutput:
        # Reuse ComfyUI's own writer so the file matches Save Splat / Create 3D File exactly.
        from comfy_extras.nodes_gaussian_splat import _gaussian_ply_bytes, _real_len

        end = _real_len(splat, 0)
        data = _gaussian_ply_bytes(splat.positions[0, :end], splat.scales[0, :end], splat.rotations[0, :end],
                                   splat.opacities[0, :end], splat.sh[0, :end])
        out_dir, name, counter, _sub, _prefix = folder_paths.get_save_image_path(
            filename_prefix, folder_paths.get_output_directory())
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, f"{name}_{counter:05}_.ply")
        with open(path, "wb") as f:
            f.write(data)
        return IO.NodeOutput(path)


NODES = [IdolSplatSavePLYPath]
