# Resources

[docs](https://docs.tinygrad.org/)

# First Steps

Let's use jupyter notebooks (inside vscode) to test out basic stuff in tinygrad

```sh
uv init
uv venv --python 3.12

. ./script/setup.sh

uv pip install jupyterlab

# install tinygrad in .venv
cd ..
git clone https://github.com/tinygrad/tinygrad.git
cd tinygrad
uv pip install .
cd ../tinygrad_learnings 
```