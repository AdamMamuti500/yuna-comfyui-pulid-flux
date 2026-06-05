# Yuna PuLID Flux — presný workflow/nody pre /object_info

## Node names (lldacing fork)

| Node name | Typ | Účel |
|-----------|-----|-------|
| `PulidFluxModelLoader` | model loader | Načíta `pulid_flux_v0.9.1.safetensors` do UNET |
| `PulidFluxEvaClipLoader` | clip loader | Načíta `EVA02_CLIP_L_336_psz14_s6B.pt` |
| `PulidFluxInsightFaceLoader` | face analysis loader | Načíta insightface antelopev2 pre face embedding |
| `ApplyPulidFlux` | conditioning | Aplikuje face embedding na FLUX conditioning |

## Pracovný workflow JSON (pre neskorší render)

```
LoadImage (Yuna face ref #1)
LoadImage (Yuna face ref #2) → voliteľné pre viac anchorov
  │
  ▼
PulidFluxInsightFaceLoader → extrahuje face embedding z obrázkov
  │
  ▼
PulidFluxEvaClipLoader → načíta EVA-CLIP
  │
  ▼
CheckpointLoaderSimple (flux1-dev-fp8) → model + CLIP + VAE
  │
  ▼
PulidFluxModelLoader (pulid_flux_v0.9.1.safetensors) → PuLID adapter
  │
  ▼
ApplyPulidFlux → skombinuje:
  - face embedding (z insightface)
  - CLIP text conditioning (z promptu)
  - PuLID adapter
  → conditioning ready
  │
  ▼
KSampler (seed X, steps 28, cfg 3.5)
  │
  ▼
VAEDecode → SaveImage
```

## Dôležité

- `ApplyPulidFlux` nahrádza bežný CLIPTextEncode — conditioning output ide priamo do KSampleru
- Negatívny prompt ide samostatne cez CLIPTextEncode (nezmenené)
- LoRA (yuna-lora-v2-core-step900) je voliteľná pomocná vrstva s nízkym weight (0.45-0.65)
- FaceDetailer je posledný refine krok (denoise 0.05-0.10)
