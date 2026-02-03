# JARVIS Quick Start Guide

Get up and running with JARVIS in 5 minutes!

## ⚡ Quick Installation

### Linux / macOS

```bash
# 1. Clone or navigate to the repository
cd distortion-12

# 2. Run installation script
chmod +x install_jarvis.sh
./install_jarvis.sh

# 3. Start JARVIS
python3 jarvis.py --text
```

### Windows

```cmd
# 1. Open Command Prompt in repository folder

# 2. Run installation script
install_jarvis.bat

# 3. Start JARVIS
python jarvis.py --text
```

### Manual Installation

If the installation scripts don't work:

```bash
# Install dependencies
pip install pyttsx3 psutil requests

# Run in text mode (no additional dependencies needed)
python3 jarvis.py --text
```

## 🎯 First Commands to Try

Once JARVIS is running, try these commands:

```
1. "hello" - Greet JARVIS
2. "time" - Get current time
3. "date" - Get current date
4. "help" - See all available commands
5. "create file myfile.txt" - Create a file
6. "search Python tutorials" - Search the web
7. "open YouTube" - Open YouTube in browser
8. "exit" - Exit JARVIS
```

## 🎤 Voice Mode vs Text Mode

### Text Mode (Recommended for First Run)
- No microphone needed
- Type your commands
- Start with: `python3 jarvis.py --text`

### Voice Mode
- Requires microphone
- Speak your commands
- Start with: `python3 jarvis.py`
- Select option 1 when prompted

## 🔧 Troubleshooting

### "Module not found" errors
```bash
pip install -r requirements.txt
```

### Voice mode not working
- Use text mode instead: `python3 jarvis.py --text`
- Check microphone permissions
- Install system audio dependencies (see JARVIS_README.md)

### Text-to-speech not working
- JARVIS will still work, output will be text-only
- Linux: Install espeak with `sudo apt-get install espeak`
- macOS: Install with `brew install espeak`

## 📖 Learn More

- Full documentation: See `JARVIS_README.md`
- Example commands: Run `python3 jarvis_examples.py`
- Configuration: Edit `jarvis_config.json`

## 💡 Pro Tips

1. **Start with text mode** - It's more reliable and works everywhere
2. **Use natural language** - JARVIS understands context
3. **Be specific** - "Create file report.txt" works better than just "create file"
4. **Check help** - Type "help" anytime to see all commands
5. **Configure settings** - Edit `jarvis_config.json` to customize voice and behavior

## 🎉 You're Ready!

You now have a working AI assistant that can:
- ✅ Open applications
- ✅ Search the web
- ✅ Manage files and folders
- ✅ Tell time and date
- ✅ Monitor system status
- ✅ And much more!

Type `help` in JARVIS to see all available commands.

---

**Need help?** Check the full documentation in `JARVIS_README.md`
