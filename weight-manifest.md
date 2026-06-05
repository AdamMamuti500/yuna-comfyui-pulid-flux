# Weight Manifest — Yuna PuLID Flux Image

Všetky weights sú public, sťahované počas Docker build (wget z HuggingFace).

## 1. PuLID Flux adapter
| Pole | Hodnota |
|------|---------|
| Súbor | `pulid_flux_v0.9.1.safetensors` |
| Umiestnenie v image | `/comfyui/models/pulid/pulid_flux_v0.9.1.safetensors` |
| Veľkosť | ~1.1 GB |
| Zdroj | `https://huggingface.co/lldacing/pulid_flux_v0.9.1/resolve/main/pulid_flux_v0.9.1.safetensors` |
| Node loader | `PulidFluxModelLoader` |

## 2. EVA-CLIP
| Pole | Hodnota |
|------|---------|
| Súbor | `EVA02_CLIP_L_336_psz14_s6B.pt` |
| Umiestnenie v image | `/comfyui/models/clip/EVA02_CLIP_L_336_psz14_s6B.pt` |
| Veľkosť | ~4.0 GB |
| Zdroj | `https://huggingface.co/QuanSun/EVA-CLIP/resolve/main/EVA02_CLIP_L_336_psz14_s6B.pt` |
| Node loader | `PulidFluxEvaClipLoader` |

## 3. InsightFace antelopev2 (5 ONNX files)
| Súbor | Veľkosť | Účel |
|-------|---------|------|
| `det_10g.onnx` | ~180 MB | Face detection |
| `w600k_r50.onnx` | ~170 MB | Face recognition (ArcFace) |
| `1k3d68.onnx` | ~23 MB | 3D landmark estimation |
| `2d106det.onnx` | ~16 MB | 2D landmark detection |
| `genderage.onnx` | ~9 MB | Gender + age estimation |
| **spolu** | **~400 MB** | |
| Umiestnenie | `/root/.insightface/models/antelopev2/` | |
| Node loader | `PulidFluxInsightFaceLoader` | |

## Celková veľkosť sťahovania počas build: ~5.5 GB

## Odhadovaná doba build: 15-25 minút (závisí od HF bandwidth)

## Overenie po build (`/object_info`)
| Node | Prítomný? |
|------|-----------|
| `PulidFluxModelLoader` | ✅ |
| `PulidFluxEvaClipLoader` | ✅ |
| `PulidFluxInsightFaceLoader` | ✅ |
| `ApplyPulidFlux` | ✅ |
| `FaceDetailer` | ✅ (z base image) |
| `UltralyticsDetectorProvider` | ✅ (z base) |
| `SAMLoader` | ✅ (z base) |
