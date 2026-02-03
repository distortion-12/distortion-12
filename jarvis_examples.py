#!/usr/bin/env python3
"""
JARVIS Examples - Demonstration of various commands and features
"""

def print_examples():
    """Print example commands for JARVIS"""
    
    examples = """
    ╔════════════════════════════════════════════════════════════╗
    ║            JARVIS - Example Commands Guide                  ║
    ╚════════════════════════════════════════════════════════════╝
    
    📱 BASIC INTERACTIONS
    ─────────────────────────────────────────────────────────────
    "Hello Jarvis"
    "Hi there"
    "Hey Jarvis, how are you?"
    
    ⏰ TIME & DATE QUERIES
    ─────────────────────────────────────────────────────────────
    "What's the time?"
    "Tell me the current time"
    "What time is it?"
    "What's today's date?"
    "Tell me the date"
    
    🖥️ OPENING APPLICATIONS
    ─────────────────────────────────────────────────────────────
    "Open notepad"
    "Launch calculator"
    "Open my browser"
    "Open terminal"
    "Open file explorer"
    
    🌐 WEB BROWSING & SEARCH
    ─────────────────────────────────────────────────────────────
    "Search for Python tutorials"
    "Search artificial intelligence"
    "Open YouTube"
    "Open Google"
    "Open GitHub"
    
    📊 SYSTEM INFORMATION
    ─────────────────────────────────────────────────────────────
    "System status"
    "Show system info"
    "What's my CPU usage?"
    "Show running processes"
    "Task manager"
    
    📁 FILE OPERATIONS
    ─────────────────────────────────────────────────────────────
    "Create file test.txt"
    "Create folder Documents"
    "Make a new file report.pdf"
    "Create folder MyProjects"
    "Take a screenshot"
    
    🌤️ WEATHER INFORMATION
    ─────────────────────────────────────────────────────────────
    "What's the weather?"
    "Weather in New York"
    "Tell me the weather in London"
    "Weather in Tokyo"
    
    🔌 SYSTEM POWER (Safety confirmations required)
    ─────────────────────────────────────────────────────────────
    "Shutdown the computer"
    "Restart my system"
    "Put computer to sleep"
    
    ❓ HELP & EXIT
    ─────────────────────────────────────────────────────────────
    "Help"
    "What can you do?"
    "Show me your capabilities"
    "Exit"
    "Goodbye Jarvis"
    "Quit"
    
    
    💡 TIPS FOR BEST RESULTS
    ═══════════════════════════════════════════════════════════
    
    1. SPEAK CLEARLY in voice mode
    2. USE NATURAL LANGUAGE - Jarvis understands context
    3. BE SPECIFIC with file names and search queries
    4. WAIT FOR CONFIRMATION before destructive actions
    5. USE TEXT MODE if voice recognition has issues
    
    
    🎯 EXAMPLE SESSIONS
    ═══════════════════════════════════════════════════════════
    
    SESSION 1: Morning Routine
    ──────────────────────────────────────────────────────────
    You: "Hello Jarvis"
    Jarvis: "Hello! How can I help you today?"
    
    You: "What's the time?"
    Jarvis: "The current time is 9:30 AM"
    
    You: "What's the weather in New York?"
    Jarvis: "The temperature in New York is 22 degrees celsius with clear sky"
    
    You: "Open browser"
    Jarvis: "Opening browser"
    
    
    SESSION 2: Work Mode
    ──────────────────────────────────────────────────────────
    You: "System status"
    Jarvis: "CPU usage is 45 percent. Memory usage is 60 percent..."
    
    You: "Create folder ProjectFiles"
    Jarvis: "Folder ProjectFiles created"
    
    You: "Open notepad"
    Jarvis: "Opening notepad"
    
    You: "Take a screenshot"
    Jarvis: "Screenshot saved as screenshot_20240203_093045.png"
    
    
    SESSION 3: Research Mode
    ──────────────────────────────────────────────────────────
    You: "Search machine learning algorithms"
    Jarvis: "Searching for machine learning algorithms"
    
    You: "Open GitHub"
    Jarvis: "Opening https://github.com"
    
    You: "What's the date?"
    Jarvis: "Today is February 3, 2026"
    
    
    🔧 CUSTOMIZATION
    ═══════════════════════════════════════════════════════════
    
    Edit jarvis_config.json to customize:
    
    {
        "wake_word": "jarvis",
        "voice_rate": 150,        // Speech speed (100-200)
        "voice_volume": 0.9,      // Volume level (0.0-1.0)
        "weather_api_key": "",    // Your OpenWeather API key
        "user_name": "Sir"        // How Jarvis addresses you
    }
    
    
    📚 ADVANCED USAGE
    ═══════════════════════════════════════════════════════════
    
    Chaining Commands:
    - Complete one task, then immediately give another command
    - Jarvis will execute sequentially
    
    Error Recovery:
    - If a command fails, Jarvis will inform you
    - Try rephrasing or check system permissions
    
    Background Tasks:
    - Some operations run in background (opening apps)
    - You can continue giving commands immediately
    
    
    ⚠️ SAFETY NOTES
    ═══════════════════════════════════════════════════════════
    
    - Shutdown/Restart commands are disabled by default for safety
    - Enable in code only if you trust the implementation
    - Always have work saved before power commands
    - File operations cannot be undone easily
    - Review weather API terms before using
    
    ─────────────────────────────────────────────────────────────
    """
    
    print(examples)


if __name__ == "__main__":
    print_examples()
