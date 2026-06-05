# Yuna ComfyUI PuLID Flux — baked image (FLUX.1-dev)

Base: `ghcr.io/adammamuti500/yuna-comfyui-impact:2026-06-04-base`
Adds: `balazik/ComfyUI-PuLID-Flux` (⭐712) + EVA-CLIP + InsightFace antelopev2

## Build
```bash
# Push to GitHub, then GHA:
gh workflow run build-yuna-pulid-flux.yml -f tag="2026-06-05-pulid"
```

## Smoke test
1. Create pod: `imageName=ghcr.io/adammamuti500/yuna-comfyui-pulid-flux:2026-06-05-pulid`
2. Check /object_info for: PulidFluxModelLoader, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, ApplyPulidFlux, FaceDetailer
3. Terminate pod → RUNPOD_ACTIVE 0

## Node names
- `PulidFluxModelLoader` — loads pulid_flux_v0.9.1.safetensors
- `PulidFluxEvaClipLoader` — loads EVA02_CLIP_L_336_psz14_s6B.pt
- `PulidFluxInsightFaceLoader` — loads insightface antelopev2
- `ApplyPulidFlux` — applies PuLID face embedding to FLUX conditioning

## Weights (all public, downloaded during build)
- pulid_flux_v0.9.1.safetensors (~700 MB) — HF balazik/pulid_flux
- EVA02_CLIP_L_336_psz14_s6B.pt (~4 GB) — HF QuanSun/EVA-CLIP
- antelopev2 5×ONNX (~400 MB) — HF monster-labs/insightface
