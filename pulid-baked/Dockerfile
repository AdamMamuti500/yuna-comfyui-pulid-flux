# Yuna ComfyUI PuLID Flux baked image.
# Base: yuna-comfyui-impact (Impact Pack + FaceDetailer + SAM).
# Adds PuLID Flux (balazik/ComfyUI-PuLID-Flux, 712⭐) for FLUX.1-dev + public weights.
# No Yuna LoRA, no gold references, no private tokens baked in.
FROM ghcr.io/adammamuti500/yuna-comfyui-impact:2026-06-04-base

ENV COMFYUI_PATH=/comfyui
ENV COMFYUI_MODEL_PATH=/comfyui/models
ENV PIP=/opt/venv/bin/pip
ENV PYTHON=/opt/venv/bin/python3

WORKDIR /comfyui

# -----------------------------------------------------------
# 1. PuLID Flux custom node (balazik/ComfyUI-PuLID-Flux, 712⭐)
#    FLUX.1-dev compatible. Node names:
#      PulidFluxModelLoader, PulidFluxInsightFaceLoader,
#      PulidFluxEvaClipLoader, ApplyPulidFlux
# -----------------------------------------------------------
RUN cd /comfyui/custom_nodes \
    && git clone --quiet --recursive \
        https://github.com/balazik/ComfyUI-PuLID-Flux.git \
    && echo "=== PuLID Flux (balazik) cloned ==="

# -----------------------------------------------------------
# 2. PuLID Python dependencies
# -----------------------------------------------------------
RUN if [ -f /comfyui/custom_nodes/ComfyUI-PuLID-Flux/requirements.txt ]; then \
        $PIP install --no-cache-dir -r /comfyui/custom_nodes/ComfyUI-PuLID-Flux/requirements.txt; \
    fi \
    && $PIP install --no-cache-dir insightface onnxruntime \
    && echo "=== PuLID deps installed ==="

# -----------------------------------------------------------
# 3. PuLID model weights
#    pulid_flux_v0.9.1.safetensors — FLUX.1-dev adapter (700MB)
# -----------------------------------------------------------
RUN mkdir -p /comfyui/models/pulid \
    && wget -q --no-check-certificate \
        -O /comfyui/models/pulid/pulid_flux_v0.9.1.safetensors \
        https://huggingface.co/balazik/pulid_flux/resolve/main/pulid_flux_v0.9.1.safetensors \
    && ls -lh /comfyui/models/pulid/ \
    && echo "=== pulid_flux_v0.9.1.safetensors OK ==="

# -----------------------------------------------------------
# 4. EVA-CLIP model
#    EVA02_CLIP_L_336_psz14_s6B.pt — for text+image conditioning
# -----------------------------------------------------------
RUN mkdir -p /comfyui/models/clip \
    && wget -q --no-check-certificate \
        -O /comfyui/models/clip/EVA02_CLIP_L_336_psz14_s6B.pt \
        https://huggingface.co/QuanSun/EVA-CLIP/resolve/main/EVA02_CLIP_L_336_psz14_s6B.pt \
    && ls -lh /comfyui/models/clip/ \
    && echo "=== EVA-CLIP OK ==="

# -----------------------------------------------------------
# 5. InsightFace antelopev2 (ALL 5 ONNX files)
#    PuLID Flux needs these for face embedding extraction.
# -----------------------------------------------------------
RUN mkdir -p /root/.insightface/models/antelopev2 \
    && wget -q --no-check-certificate \
        -O /root/.insightface/models/antelopev2/1k3d68.onnx \
        https://huggingface.co/monster-labs/insightface/resolve/main/antelopev2/1k3d68.onnx \
    && wget -q --no-check-certificate \
        -O /root/.insightface/models/antelopev2/2d106det.onnx \
        https://huggingface.co/monster-labs/insightface/resolve/main/antelopev2/2d106det.onnx \
    && wget -q --no-check-certificate \
        -O /root/.insightface/models/antelopev2/det_10g.onnx \
        https://huggingface.co/monster-labs/insightface/resolve/main/antelopev2/det_10g.onnx \
    && wget -q --no-check-certificate \
        -O /root/.insightface/models/antelopev2/genderage.onnx \
        https://huggingface.co/monster-labs/insightface/resolve/main/antelopev2/genderage.onnx \
    && wget -q --no-check-certificate \
        -O /root/.insightface/models/antelopev2/w600k_r50.onnx \
        https://huggingface.co/monster-labs/insightface/resolve/main/antelopev2/w600k_r50.onnx \
    && ls -lh /root/.insightface/models/antelopev2/ \
    && echo "=== antelopev2 (5/5) OK ==="

# -----------------------------------------------------------
# 6. Verify build
# -----------------------------------------------------------
RUN $PYTHON << 'PYEOF'
import insightface
import onnxruntime
import os
model_dir = "/root/.insightface/models/antelopev2"
files = set(os.listdir(model_dir))
expected = {"1k3d68.onnx", "2d106det.onnx", "det_10g.onnx", "genderage.onnx", "w600k_r50.onnx"}
missing = expected - files
if missing:
    raise RuntimeError(f"Missing antelopev2 files: {missing}")
print("insightface antelopev2: all 5 files verified")
for path, label in [
    ("/comfyui/models/pulid/pulid_flux_v0.9.1.safetensors", "pulid_flux"),
    ("/comfyui/models/clip/EVA02_CLIP_L_336_psz14_s6B.pt", "EVA-CLIP"),
]:
    if not os.path.exists(path):
        raise RuntimeError(f"Missing {label}: {path}")
    print(f"{label}: OK ({os.path.getsize(path)} bytes)")
print("=== PuLID Flux build verification PASSED ===")
PYEOF

# -----------------------------------------------------------
# 7. Disk usage
# -----------------------------------------------------------
RUN echo "=== Model weights disk ===" \
    && du -sh /comfyui/models/pulid/ \
    && du -sh /comfyui/models/clip/ \
    && du -sh /root/.insightface/ \
    && echo "=== Total ===" \
    && du -sh / | tail -1

# Keep base image ENTRYPOINT/CMD — RunPod worker manages ComfyUI lifecycle.
