import os

root = os.getenv('MODEL_PATH', "")
network_name = "dense-fire-1"
model_path = os.path.join(root, "models", network_name)
