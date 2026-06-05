# Weight Manifest — Yuna PuLID Flux (FLUX.1-dev)

Source: `balazik/ComfyUI-PuLID-Flux` (⭐712) — FLUX.1-dev compatible.

## 1. PuLID Flux adapter
| Pole | Hodnota |
|------|---------|
| Súbor | `pulid_flux_v0.9.1.safetensors` (~700 MB) |
| Umiestnenie | `/comfyui/models/pulid/pulid_flux_v0.9.1.safetensors` |
| Zdroj | `https://huggingface.co/balazik/pulid_flux/resolve/main/pulid_flux_v0.9.1.safetensors` |
| Node loader | `PulidFluxModelLoader` |

## 2. EVA-CLIP
| Pole | Hodnota |
|------|---------|
| Súbor | `EVA02_CLIP_L_336_psz14_s6B.pt` (~4.0 GB) |
| Umiestnenie | `/comfyui/models/clip/EVA02_CLIP_L_336_psz14_s6B.pt` |
| Zdroj | `https://huggingface.co/QuanSun/EVA-CLIP/resolve/main/EVA02_CLIP_L_336_psz14_s6B.pt` |
| Node loader | `PulidFluxEvaClipLoader` |

## 3. InsightFace antelopev2 (5 ONNX files)
| Súbor | Veľkosť |
|-------|---------|
| `det_10g.onnx` | ~180 MB (face detection) |
| `w600k_r50.onnx` | ~170 MB (face recognition) |
| `1k3d68.onnx` | ~23 MB (3D landmarks) |
| `2d106det.onnx` | ~16 MB (2D landmarks) |
| `genderage.onnx` | ~9 MB (gender/age) |
| **spolu** | **~400 MB** |
| Umiestnenie | `/root/.insightface/models/antelopev2/` |
| Zdroj | `monster-labs/insightface` |
| Node loader | `PulidFluxInsightFaceLoader` |

## Total download: ~5.1 GB

## Node names (/object_info)

| Node name | Display name |
|-----------|-------------|
| `PulidFluxModelLoader` | Load PuLID Flux Model |
| `PulidFluxEvaClipLoader` | Load Eva Clip (PuLID Flux) |
| `PulidFluxInsightFaceLoader` | Load InsightFace (PuLID Flux) |
| `ApplyPulidFlux` | Apply PuLID Flux |

Plus from base image: `FaceDetailer`, `UltralyticsDetectorProvider`, `SAMLoader`, `CheckpointLoaderSimple`, `LoraLoaderModelOnly`.
