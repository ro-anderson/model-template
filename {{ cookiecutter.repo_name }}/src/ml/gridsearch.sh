#!/bin/bash
set -e

# conda env activation
source ~/anaconda3/etc/profile.d/conda.sh
conda activate {{ cookiecutter.repo_name }}


# generating list of parameters combination
PARAMS_LIST=(
    '''{"max_num_features":  10, "n_trees": 100, "max_depth": 3}'''
    '''{"max_num_features":  50, "n_trees":  50, "max_depth": 4}'''
    '''{"max_num_features": 100, "n_trees":  25, "max_depth": 5}'''
    )

# making dataset
python code/data.py

# looping
for val in "${PARAMS_LIST[@]}"
do

    python code/features.py --params "$val"
    python code/train.py --params "$val"
    python code/predict.py
    python code/evaluate.py

done

# conda env deactivation
conda deactivate
