# Yuna ComfyUI PuLID Flux baked image.
# Base: yuna-comfyui-impact (Impact Pack + FaceDetailer + SAM).
# Adds PuLID Flux (balazik, FLUX.1-dev) + public weights. No private data baked.
FROM ghcr.io/adammamuti500/yuna-comfyui-impact:2026-06-04-base

ENV PIP=/opt/venv/bin/pip
ENV PYTHON=/opt/venv/bin/python3
WORKDIR /comfyui

# 1. PuLID Flux custom node (balazik - FLUX.1-dev)
RUN cd /comfyui/custom_nodes \
    && git clone --quiet --recursive https://github.com/balazik/ComfyUI-PuLID-Flux.git \
    && echo "PuLID Flux cloned"

# 2. PuLID python deps
RUN if [ -f /comfyui/custom_nodes/ComfyUI-PuLID-Flux/requirements.txt ]; then \
        $PIP install --no-cache-dir -r /comfyui/custom_nodes/ComfyUI-PuLID-Flux/requirements.txt; \
    fi \
    && $PIP install --no-cache-dir insightface onnxruntime facexlib \
    && echo "PuLID deps installed"

# 3. PuLID Flux adapter weight (guozinan/PuLID)
RUN mkdir -p /comfyui/models/pulid \
    && wget -q -O /comfyui/models/pulid/pulid_flux_v0.9.0.safetensors \
        https://huggingface.co/guozinan/PuLID/resolve/main/pulid_flux_v0.9.0.safetensors \
    && echo "pulid weight OK"

# 4. EVA-CLIP
RUN mkdir -p /comfyui/models/clip \
    && wget -q -O /comfyui/models/clip/EVA02_CLIP_L_336_psz14_s6B.pt \
        https://huggingface.co/QuanSun/EVA-CLIP/resolve/main/EVA02_CLIP_L_336_psz14_s6B.pt \
    && echo "eva-clip OK"

# 5. InsightFace antelopev2 via SDK auto-download
RUN $PYTHON -c "from insightface.utils import storage; print('antelopev2:', storage.ensure_available('models', 'antelopev2', root='/root/.insightface'))"

# 6. Verify (single clean line, no nested-quote hell)
RUN $PYTHON -c "import os,insightface; assert os.path.exists('/comfyui/models/pulid/pulid_flux_v0.9.0.safetensors'),'pulid'; assert os.path.exists('/comfyui/models/clip/EVA02_CLIP_L_336_psz14_s6B.pt'),'eva'; assert os.path.exists('/root/.insightface/models/antelopev2/det_10g.onnx'),'antelope'; print('=== PuLID build verify OK ===')"

# Keep base ENTRYPOINT/CMD - RunPod worker manages ComfyUI.
