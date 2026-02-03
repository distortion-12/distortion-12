# JARVIS - Just A Rather Very Intelligent System

A sophisticated voice-controlled personal assistant that can fully control your device and perform various tasks on command.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## 🌟 Features

### Device Control
- **Application Management**: Open and control applications (Notepad, Calculator, Browser, Terminal, File Explorer)
- **System Commands**: Shutdown, Restart, Sleep/Hibernate (with confirmation)
- **Volume Control**: Adjust system volume up/down or mute
- **System Monitoring**: Check CPU, Memory, and Disk usage
- **Process Management**: View top running processes

### Task Execution
- **Time & Date**: Get current time and date
- **Web Search**: Search anything on Google
- **Website Navigation**: Quick access to popular websites (YouTube, Google, GitHub)
- **Weather Information**: Get weather updates for any city
- **File Operations**: Create files and folders
- **Screenshots**: Capture screen on command

### Intelligent Interaction
- **Voice Control**: Natural voice command processing
- **Text Mode**: Type commands if voice is unavailable
- **Context Awareness**: Understands various phrasings of commands
- **Feedback**: Speaks responses and confirmations

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- Microphone (for voice mode)
- Internet connection (for voice recognition and web features)

### Step 1: Clone or Download
```bash
# If this is part of a repository
cd distortion-12

# Or download the jarvis.py file directly
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

**Note for Linux users**: You may need to install additional dependencies for PyAudio:
```bash
sudo apt-get install portaudio19-dev python3-pyaudio
```

**Note for macOS users**:
```bash
brew install portaudio
pip install pyaudio
```

### Step 3: Configuration (Optional)
Edit `jarvis_config.json` to customize:
- Voice rate and volume
- Weather API key (get free key from OpenWeatherMap)
- User preferences

## 📖 Usage

### Voice Mode (Default)
```bash
python jarvis.py
```
Select option 1 for voice mode, then speak your commands clearly.

### Text Mode
```bash
python jarvis.py --text
```
Or select option 2 when prompted, then type your commands.

## 🎤 Available Commands

### Greetings & Help
- "Hello" / "Hi" / "Hey" - Greet Jarvis
- "Help" / "What can you do" - Show all available commands

### Time & Date
- "What's the time?"
- "What's the date?"
- "Tell me the time"
- "What day is it?"

### Applications
- "Open notepad"
- "Open calculator"
- "Open browser"
- "Open terminal" / "Open command prompt"
- "Open file explorer" / "Open files"

### System Control
- "System info" / "System status" - View CPU, RAM, Disk usage
- "Running processes" / "Task manager" - View top processes
- "Shutdown" / "Restart" / "Sleep" - System power commands (requires confirmation)

### Web & Search
- "Search [your query]" - Search on Google
- "Open YouTube"
- "Open Google"
- "Open GitHub"

### File Operations
- "Create file [filename]" - Create a new file
- "Create folder [foldername]" - Create a new folder
- "Take screenshot" / "Screenshot" - Capture screen

### Weather
- "Weather" - Get weather for default city
- "Weather in [city name]" - Get weather for specific city

### Exit
- "Exit" / "Quit" / "Goodbye" / "Bye" - Close Jarvis

## 🔧 Configuration

Edit `jarvis_config.json` to customize Jarvis:

```json
{
    "wake_word": "jarvis",
    "voice_rate": 150,
    "voice_volume": 0.9,
    "weather_api_key": "your_api_key_here",
    "user_name": "Sir",
    "theme": "default"
}
```

### Getting Weather API Key
1. Visit [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Generate an API key
4. Add it to `jarvis_config.json`

## 🛠️ Troubleshooting

### Microphone Issues
If voice recognition isn't working:
1. Check microphone permissions
2. Test microphone with other applications
3. Adjust ambient noise threshold in the code
4. Use text mode as alternative

### PyAudio Installation Errors
If you encounter errors installing PyAudio:
- **Windows**: Download wheel file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
- **Linux**: `sudo apt-get install portaudio19-dev python3-pyaudio`
- **macOS**: `brew install portaudio`

### Application Opening Issues
Some applications may have different names on different systems. Modify the `apps` dictionary in `open_application()` method to match your system.

## 🔐 Safety Features

- **Confirmation Required**: Destructive actions (shutdown, restart) require confirmation
- **Error Handling**: Graceful handling of errors and exceptions
- **Permission Management**: Only executes safe commands by default

## 🎯 Future Enhancements

- [ ] AI-powered natural language understanding
- [ ] Custom command creation
- [ ] Smart home integration
- [ ] Email management
- [ ] Calendar integration
- [ ] Reminder and alarm system
- [ ] Music playback control
- [ ] Advanced automation workflows

## 🤝 Contributing

Feel free to fork this project and add your own features! Some ideas:
- Add more device control features
- Integrate with smart home devices
- Add AI/ML capabilities for better understanding
- Create GUI interface
- Add more language support

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Ramakant Singh Chouhan**
- GitHub: [@distortion-12](https://github.com/distortion-12)
- LinkedIn: [ramchouhan](https://linkedin.com/in/ramchouhan)

## 🙏 Acknowledgments

Inspired by Iron Man's JARVIS and building upon the LYRA Voice Assistant project.

---

**Note**: This is a powerful tool that can control your system. Use responsibly and understand each command before executing. Always backup important data before using system control features.
