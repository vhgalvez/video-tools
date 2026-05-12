# Video Tools

A collection of Python scripts for video processing and manipulation using MoviePy.

## Description

This project provides tools for working with video files using the MoviePy library. The main script `unir_clips.py` demonstrates how to concatenate video clips into a single video file.

## Features

- Easy video clip concatenation
- Simple command-line interface
- Cross-platform compatibility
- Dependency management guide

## Prerequisites

Before running the scripts, you'll need to install Anaconda or Miniconda.

## Installation

### Using Anaconda/Miniconda (Recommended)

1. **Create a virtual environment:**
   ```bash
   conda create -n video-tools python=3.11 -y
   ```

2. **Activate the environment:**
   ```bash
   conda activate video-tools
   ```

3. **Install required packages:**
   ```bash
   pip install moviepy imageio-ffmpeg
   ```

4. **Verify installation:**
   ```bash
   python -c "import moviepy; print(moviepy.__version__)"
   ```

### Alternative Installation (if conda is not available)

If you don't have Anaconda/Miniconda installed:
1. Install Python 3.11 or higher
2. Install the required packages using pip:
   ```bash
   pip install moviepy imageio-ffmpeg
   ```

## Usage

1. **Activate the environment:**
   ```bash
   conda activate video-tools
   ```

2. **Run the script:**
   ```bash

   cd C:\video-tools\unir_clips_crossfade.py
   python unir_clips_crossfade.py
   ```

3. **Deactivate when finished:**
   ```bash
   conda deactivate
   ```

## Troubleshooting

### If `conda activate` doesn't work in PowerShell

1. Initialize conda for PowerShell:
   ```bash
   conda init powershell
   ```

2. Close and reopen PowerShell

3. Activate the environment:
   ```bash
   conda activate video-tools
   ```

4. Verify the environment is active:
   ```bash
   conda env list
   ```

## Requirements

- Python 3.11 or higher
- MoviePy library
- imageio-ffmpeg package

## Project Structure

```
video-tools/
├── unir_clips_crossfade.py     # Main video processing script
├── README.md                   # This file
└── requirements.txt            # Optional requirements file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Created with ❤️ for video processing enthusiasts