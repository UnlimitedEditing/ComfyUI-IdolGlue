# ComfyUI-IdolGlue

Tiny glue node for running [Idol](https://huggingface.co/speridlabs/idol) (image to 3D gaussian splat) on headless
ComfyUI hosts. **Idol Splat -> PLY Path** writes a native ComfyUI splat to a `.ply` and returns the path as a STRING,
so path-based exporters can pick it up. The model itself runs on ComfyUI's native TripoSplat nodes plus
[Nynxz/ComfyUI-Idol](https://github.com/Nynxz/ComfyUI-Idol); weights: [Comfy-Org/Idol](https://huggingface.co/Comfy-Org/Idol).
Requires ComfyUI with `comfy_extras.nodes_gaussian_splat` (v0.43+). License: Apache-2.0.
