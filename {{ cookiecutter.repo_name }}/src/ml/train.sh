#!/bin/bash
set -e

# conda env activation
source ~/anaconda3/etc/profile.d/conda.sh
conda activate {{ cookiecutter.repo_name }}

# training partial model and evaluating
python code/data.py
python code/features.py
python code/train.py
python code/predict.py
python code/evaluate.py

# conda env deactivation
conda deactivate
