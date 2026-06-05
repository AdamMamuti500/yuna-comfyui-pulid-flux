import os, sys
root='/root/.insightface'
d=os.path.join(root,'models','antelopev2')
try:
    from insightface.app import FaceAnalysis
    FaceAnalysis(name='antelopev2', root=root)
    print('FaceAnalysis init OK')
except Exception as e:
    print('FaceAnalysis init raised (download likely completed, load ignored):', repr(e)[:170])
onnx = [f for f in os.listdir(d) if f.endswith('.onnx')] if os.path.isdir(d) else []
if not onnx:
    print('No onnx at', d, '- searching tree...')
    hits=[]
    for r,_,fs in os.walk(root):
        for f in fs:
            if f.endswith('.onnx'): hits.append(os.path.join(r,f))
    print('onnx found in tree:', hits)
    sys.exit('antelopev2 onnx NOT found')
print('antelopev2 OK:', onnx)
