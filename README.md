# Yuna ComfyUI PuLID Flux — baked image

Base image: `ghcr.io/adammamuti500/yuna-comfyui-impact:2026-06-04-base`
Adds: PuLID Flux (lldacing fork) + EVA-CLIP + InsightFace antelopev2

## Build

```bash
# Manual trigger via GitHub Actions:
# 1. Push this repo to GitHub (AdamMamuti500/yuna-comfyui-pulid-flux)
# 2. Actions → Build Yuna PuLID Flux Image → Run workflow
#    tag: 2026-06-05-pulid
```

## Smoke test (after build)

```bash
# 1. Create RunPod pod with the new image (no volume needed for smoke)
# 2. Check /object_info:
#    - PulidFluxModelLoader ✅
#    - ApplyPulidFlux ✅
#    - PulidFluxEvaClipLoader ✅
#    - PulidFluxInsightFaceLoader ✅
#    - FaceDetailer ✅ (from base)
#    - UltralyticsDetectorProvider ✅
#    - SAMLoader ✅
# 3. Verify PuLID model weights load:
#    - pulid_flux_v0.9.1.safetensors in /comfyui/models/pulid/
#    - EVA02_CLIP_L_336_psz14_s6B.pt in /comfyui/models/clip/
#    - antelopev2 (5 ONNX files) in ~/.insightface/models/antelopev2/
# 4. Terminate pod → RUNPOD_ACTIVE 0
```

## Contents

| Path | Source | Purpose |
|------|--------|---------|
| pulid-baked/Dockerfile | this repo | Build recipe |
| .github/workflows/build-yuna-pulid-flux.yml | this repo | GHA workflow |

## Model weights (public, downloaded during build)

| File | Size | Source |
|------|------|--------|
| pulid_flux_v0.9.1.safetensors | ~1.2 GB | huggingface.co/lldacing/pulid_flux_v0.9.1 |
| EVA02_CLIP_L_336_psz14_s6B.pt | ~4.0 GB | huggingface.co/QuanSun/EVA-CLIP |
| antelopev2 (5 ONNX) | ~600 MB | huggingface.co/monster-labs/insightface |

## Node names in /object_info (lldacing fork)

- `PulidFluxModelLoader` — loads pulid_flux_v0.9.1.safetensors
- `PulidFluxEvaClipLoader` — loads EVA02 CLIP model
- `PulidFluxInsightFaceLoader` — loads insightface antelopev2
- `ApplyPulidFlux` — applies PuLID face embedding to FLUX conditioning

## Notes

- No Yuna LoRA, no gold references, no tokens baked into public image.
- Yuna assets (LoRA, refs) are provided via RunPod volume or startup script.
- lldacing fork includes the `timestep_zero_index` fix — no extra patch needed.
- InsightFace is used for test (best identity); FaceNet switch possible before production.
