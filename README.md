# Kaldi-asr-server
This is a flask asr-service with server and client, which is based on the Vernacular-ai/kaldi-serve(https://github.com/Vernacular-ai/kaldi-serve).

**Key Features**:
- Real-time streaming (uni & bi-directional) audio recognition.
- support MFCC and Fbank when the corresponding file exists
- support i-vector input when the corresponding file exists
- Thread-safe concurrent Decoder queue for server environments.
- support RNNLM lattice rescoring when the corresponding file exists.
- N-best alternatives with AM/LM costs, word-level timings and confidence scores.

## Installation
* [Kaldi](https://kaldi-asr.org/)
* python==3.6.7(suggest conda install)

### Build from Source
```bash
cd build/
cmake .. -DBUILD_PYBIND11=ON -DBUILD_PYTHON_MODULE=ON -DPYTHON_EXECUTABLE=${which python}
make -j${nproc}
cp python/kaldiserve_pybind*.so ../python/kaldiserve/
cd ../python
pip install . -U
```
## Configuration

you should config the model files in "./resources/model-spec.toml" before you start the server. 

### Usage
```bash
cd python
Start the service: python server.py
Start the clinet with multithreading: python client_test.py

```
### Reference
－ https://github.com/Vernacular-ai/kaldi-serve
－ https://github.com/al-zatv/kaldi-serve

