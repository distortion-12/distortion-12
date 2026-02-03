#!/bin/bash
# JARVIS Installation Script
# This script will set up JARVIS assistant on your system

echo "╔════════════════════════════════════════════════╗"
echo "║                                                ║"
echo "║         JARVIS Installation Script             ║"
echo "║                                                ║"
echo "╚════════════════════════════════════════════════╝"
echo ""

# Check Python version
echo "Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Found Python $python_version"

# Check if Python 3.7+
required_version="3.7"
if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" = "$required_version" ]; then 
    echo "✓ Python version is compatible"
else
    echo "✗ Python 3.7 or higher is required"
    exit 1
fi

echo ""
echo "Installing required packages..."

# Install system dependencies based on OS
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "Detected Linux OS"
    echo "Installing system dependencies..."
    
    # Check if running with sudo
    if [ "$EUID" -ne 0 ]; then
        echo "Note: You may need to enter your password for system package installation"
        sudo apt-get update
        sudo apt-get install -y portaudio19-dev python3-pyaudio espeak espeak-ng
    else
        apt-get update
        apt-get install -y portaudio19-dev python3-pyaudio espeak espeak-ng
    fi
    
elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo "Detected macOS"
    echo "Installing system dependencies..."
    
    # Check if Homebrew is installed
    if ! command -v brew &> /dev/null; then
        echo "Homebrew not found. Please install Homebrew first:"
        echo "https://brew.sh"
        exit 1
    fi
    
    brew install portaudio espeak
    
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    echo "Detected Windows"
    echo "Note: On Windows, some dependencies may need manual installation"
fi

echo ""
echo "Installing Python packages..."

# Create virtual environment (optional but recommended)
read -p "Create a virtual environment? (recommended) [Y/n]: " create_venv
create_venv=${create_venv:-Y}

if [[ $create_venv =~ ^[Yy]$ ]]; then
    echo "Creating virtual environment..."
    python3 -m venv jarvis_env
    
    # Activate virtual environment
    if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
        source jarvis_env/Scripts/activate
    else
        source jarvis_env/bin/activate
    fi
    
    echo "✓ Virtual environment created and activated"
fi

# Install Python packages
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "╔════════════════════════════════════════════════╗"
echo "║                                                ║"
echo "║         Installation Complete!                 ║"
echo "║                                                ║"
echo "╚════════════════════════════════════════════════╝"
echo ""
echo "To run JARVIS:"
echo "  Text Mode:  python3 jarvis.py --text"
echo "  Voice Mode: python3 jarvis.py"
echo ""
echo "For help:     python3 jarvis_examples.py"
echo "Documentation: See JARVIS_README.md"
echo ""

if [[ $create_venv =~ ^[Yy]$ ]]; then
    echo "Note: Remember to activate the virtual environment before running:"
    if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
        echo "  source jarvis_env/Scripts/activate"
    else
        echo "  source jarvis_env/bin/activate"
    fi
fi

echo ""
echo "Enjoy your personal AI assistant! 🚀"
