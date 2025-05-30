#!/usr/bin/env python
"""
CodeLlama to OpenVINO Converter
-------------------------------
This script downloads and converts the CodeLlama-7B model to OpenVINO IR format
with a progress bar to track the conversion process.
"""

import os
import sys
from pathlib import Path
import time
from tqdm import tqdm

# Ensure the directories exist
models_dir = Path("models")
codellama_dir = models_dir / "codellama"
openvino_dir = models_dir / "codellama-openvino"

def download_model():
    """Download the CodeLlama model if needed"""
    if not codellama_dir.exists():
        print("Creating model directory...")
        codellama_dir.mkdir(parents=True, exist_ok=True)
        
        print("\n=== Downloading CodeLlama-7B model ===")
        print("Note: This is a large model (>13GB) and may take time.")
        print("You can interrupt and resume later if needed.")
        
        # For a more controlled download, we'll use Hugging Face's transformers library
        from huggingface_hub import snapshot_download
        
        with tqdm(total=100, desc="Downloading", unit="%") as pbar:
            def progress_callback(progress):
                if progress.total:
                    pbar.n = int(100 * progress.downloaded / progress.total)
                    pbar.refresh()
            
            snapshot_download(
                repo_id="codellama/CodeLlama-7b-hf",
                local_dir=str(codellama_dir),
                local_dir_use_symlinks=False,
                progress_callback=progress_callback
            )
    else:
        print("CodeLlama model directory already exists.")

def convert_to_openvino():
    """Convert the model to OpenVINO IR format with progress tracking"""
    print("\n=== Converting CodeLlama-7B to OpenVINO IR format ===")
    
    if not openvino_dir.exists():
        openvino_dir.mkdir(parents=True, exist_ok=True)
    
    # Import optimum libraries here to avoid errors if not installed
    try:
        from optimum.exporters.openvino import export_model, main_export
        from optimum.exporters.openvino.utils import _get_submodels_and_export_configs
        from transformers import AutoConfig
    except ImportError:
        print("Error: Required libraries not found. Please install:")
        print("pip install optimum[openvino] transformers")
        sys.exit(1)
    
    # Custom progress tracking for the conversion process
    print("Preparing model for conversion...")
    
    # Create a wrapper around export_model to show progress
    original_export = export_model
    
    def export_with_progress(*args, **kwargs):
        print("Starting conversion (this will take some time)...")
        
        # Create a progress bar that pulses
        with tqdm(total=100, desc="Converting", bar_format='{l_bar}{bar}| {elapsed}/{remaining}') as pbar:
            # Setup progress tracking
            start_time = time.time()
            last_update = start_time
            
            # Create a progress update function
            def update_progress():
                nonlocal last_update
                current_time = time.time()
                if current_time - last_update > 0.5:  # Update every half second
                    elapsed = current_time - start_time
                    # Estimate progress based on typical conversion time
                    # This is an approximation since we don't know the actual progress
                    progress = min(95, (elapsed / 1200) * 100)  # Assuming ~20 minutes for full conversion
                    pbar.n = int(progress)
                    pbar.refresh()
                    last_update = current_time
            
            # Patch some internal functions to track progress
            original_call = AutoConfig.__call__
            
            def patched_call(*call_args, **call_kwargs):
                update_progress()
                return original_call(*call_args, **call_kwargs)
            
            # Apply the patch
            AutoConfig.__call__ = patched_call
            
            try:
                # Perform the actual export
                result = original_export(*args, **kwargs)
                pbar.n = 100
                pbar.refresh()
                return result
            finally:
                # Restore original function
                AutoConfig.__call__ = original_call
    
    # Replace the original function with our progress-tracking version
    export_model = export_with_progress
    
    # Now call the export process
    try:
        export_model(
            model_id_or_path=str(codellama_dir),
            output_dir=str(openvino_dir),
            device="NPU"  # Use NPU for acceleration
        )
        print("\n✅ Conversion complete! Model saved to:", openvino_dir)
        print("OpenVINO model files:")
        for file in openvino_dir.glob("*"):
            print(f"  - {file.name}")
    except Exception as e:
        print(f"\n❌ Error during conversion: {str(e)}")
        print("Try running the conversion manually using optimum-cli.")

def main():
    """Main function to orchestrate the download and conversion process"""
    print("=" * 80)
    print("CodeLlama-7B to OpenVINO Converter")
    print("=" * 80)
    
    # Step 1: Download the model if needed
    download_model()
    
    # Step 2: Convert to OpenVINO format
    convert_to_openvino()
    
    # Step 3: Provide next steps
    print("\n=== Next Steps ===")
    print("1. Update your .env file with the following:")
    print("   AI_CHAT_PROVIDER=openvino")
    print("   OPENVINO_CHAT_MODEL=models/codellama-openvino/openvino_model.xml")
    print("   OPENVINO_DEVICE=NPU")
    print("   OPENVINO_MODEL_CACHE=TRUE")
    print("\n2. Start your application to use the OpenVINO-accelerated model")

if __name__ == "__main__":
    main()
