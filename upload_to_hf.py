import argparse
import os

from huggingface_hub import HfApi
from tqdm.auto import tqdm


def upload_folder_contents_to_hf_hub(
    base_folder, organization, hf_username, hf_password
):
    """
    Uploads all files in a given folder to a specific repository on the HuggingFace Model Hub.

    Args:
    - folder_path (str): Path to the folder containing files to upload.
    - hf_username (str): HuggingFace username.
    - hf_password (str): HuggingFace password.
    - repo_id (str): Repository ID on HuggingFace Hub (e.g., "username/repo_name" or "organization/repo_name").
    """
    api = HfApi()
    for folder_name in tqdm(os.listdir(base_folder), desc="Uploading Folder Contents"):
        full_path = os.path.join(base_folder, folder_name)
        repo_id = f"{organization}/{folder_name}"
        _ = api.create_repo(
                repo_id=repo_id,
                repo_type="model",
                private=False, # Set to True if you want to create a private repository
                exist_ok=True # Set to True to avoid errors if the repository already exists
            )
        api.upload_folder(
            repo_id=repo_id, folder_path=full_path, token=True
        )
        print(f"Uploaded {full_path} to {repo_id} successfully.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Upload folder contents to the HuggingFace Model Hub"
    )
    parser.add_argument(
        "--main_folder",
        type=str,
        help="Path to the main folder containing subfolders to upload",
    )
    parser.add_argument("--hf_username", type=str, help="HuggingFace username")
    parser.add_argument("--hf_password", type=str, help="HuggingFace password")
    parser.add_argument("--organization", type=str, help="HuggingFace organization name")

    args = parser.parse_args()
    upload_folder_contents_to_hf_hub(
        args.main_folder, args.organization, args.hf_username, args.hf_password
    )
