#!/usr/bin/env python3
"""
JARVIS - Just A Rather Very Intelligent System
A voice-controlled personal assistant that can fully control your device
"""

import os
import sys
import subprocess
import webbrowser
import datetime
import platform
import json
from pathlib import Path

# Optional imports with fallbacks
try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False
    print("Warning: psutil not installed. System info features will be limited.")

try:
    import pyttsx3
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False
    print("Warning: pyttsx3 not installed. Text-to-speech will be disabled.")

try:
    import speech_recognition as sr
    SR_AVAILABLE = True
except ImportError:
    SR_AVAILABLE = False
    print("Warning: SpeechRecognition not installed. Voice mode will be disabled.")

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False
    print("Warning: requests not installed. Weather features will be disabled.")


class Jarvis:
    """Main Jarvis Assistant Class"""
    
    def __init__(self):
        """Initialize Jarvis with necessary components"""
        if TTS_AVAILABLE:
            try:
                self.engine = pyttsx3.init()
            except Exception as e:
                print(f"Warning: Could not initialize text-to-speech: {e}")
                self.engine = None
        else:
            self.engine = None
        
        if SR_AVAILABLE:
            self.recognizer = sr.Recognizer()
        else:
            self.recognizer = None
            
        self.config = self.load_config()
        
        if self.engine:
            self.setup_voice()
        
    def load_config(self):
        """Load configuration from config file"""
        config_path = Path(__file__).parent / "jarvis_config.json"
        if config_path.exists():
            with open(config_path, 'r') as f:
                return json.load(f)
        return {
            "wake_word": "jarvis",
            "voice_rate": 150,
            "voice_volume": 0.9,
            "weather_api_key": ""
        }
    
    def setup_voice(self):
        """Configure text-to-speech settings"""
        if not self.engine:
            return
            
        voices = self.engine.getProperty('voices')
        # Try to set male voice if available
        for voice in voices:
            if 'male' in voice.name.lower() and 'female' not in voice.name.lower():
                self.engine.setProperty('voice', voice.id)
                break
        
        self.engine.setProperty('rate', self.config.get('voice_rate', 150))
        self.engine.setProperty('volume', self.config.get('voice_volume', 0.9))
    
    def speak(self, text):
        """Convert text to speech"""
        print(f"Jarvis: {text}")
        if self.engine:
            try:
                self.engine.say(text)
                self.engine.runAndWait()
            except:
                pass  # If TTS fails, text output is already printed
    
    def listen(self):
        """Listen for voice commands"""
        if not SR_AVAILABLE or not self.recognizer:
            self.speak("Voice recognition not available. Please use text mode.")
            return ""
            
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                command = self.recognizer.recognize_google(audio).lower()
                print(f"You said: {command}")
                return command
            except sr.WaitTimeoutError:
                return ""
            except sr.UnknownValueError:
                return ""
            except sr.RequestError:
                self.speak("Sorry, speech service is unavailable")
                return ""
    
    def get_text_input(self):
        """Get text input from user"""
        return input("Enter command: ").lower()
    
    # ============= DEVICE CONTROL FEATURES =============
    
    def open_application(self, app_name):
        """Open applications on the device"""
        apps = {
            'notepad': 'notepad.exe' if platform.system() == 'Windows' else 'gedit',
            'calculator': 'calc.exe' if platform.system() == 'Windows' else 'gnome-calculator',
            'browser': 'chrome' if platform.system() == 'Windows' else 'google-chrome',
            'terminal': 'cmd.exe' if platform.system() == 'Windows' else 'gnome-terminal',
            'file explorer': 'explorer.exe' if platform.system() == 'Windows' else 'nautilus',
        }
        
        app = apps.get(app_name.lower())
        if app:
            try:
                if platform.system() == 'Windows':
                    subprocess.Popen(app)
                else:
                    subprocess.Popen([app])
                self.speak(f"Opening {app_name}")
                return True
            except Exception as e:
                self.speak(f"Could not open {app_name}")
                return False
        else:
            self.speak(f"I don't know how to open {app_name}")
            return False
    
    def shutdown_system(self):
        """Shutdown the computer"""
        self.speak("Shutting down the system")
        if platform.system() == 'Windows':
            os.system('shutdown /s /t 1')
        else:
            os.system('shutdown now')
    
    def restart_system(self):
        """Restart the computer"""
        self.speak("Restarting the system")
        if platform.system() == 'Windows':
            os.system('shutdown /r /t 1')
        else:
            os.system('reboot')
    
    def sleep_system(self):
        """Put the computer to sleep"""
        self.speak("Putting the system to sleep")
        if platform.system() == 'Windows':
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
        else:
            os.system('systemctl suspend')
    
    def adjust_volume(self, action):
        """Adjust system volume"""
        if platform.system() == 'Windows':
            if action == 'up':
                subprocess.run(['nircmd.exe', 'changesysvolume', '2000'])
            elif action == 'down':
                subprocess.run(['nircmd.exe', 'changesysvolume', '-2000'])
            elif action == 'mute':
                subprocess.run(['nircmd.exe', 'mutesysvolume', '1'])
            self.speak(f"Volume {action}")
        else:
            self.speak("Volume control not implemented for this OS")
    
    def get_system_info(self):
        """Get system information"""
        if not PSUTIL_AVAILABLE:
            self.speak("System monitoring not available. Please install psutil.")
            return
            
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        
        info = f"CPU usage is {cpu_percent} percent. "
        info += f"Memory usage is {memory.percent} percent. "
        info += f"Disk usage is {disk.percent} percent."
        
        self.speak(info)
        return info
    
    def list_running_processes(self):
        """List top running processes"""
        if not PSUTIL_AVAILABLE:
            self.speak("Process monitoring not available. Please install psutil.")
            return
            
        processes = []
        for proc in psutil.process_iter(['name', 'cpu_percent']):
            try:
                processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        
        # Sort by CPU usage
        processes.sort(key=lambda x: x['cpu_percent'] or 0, reverse=True)
        top_5 = processes[:5]
        
        self.speak("Top 5 processes by CPU usage:")
        for proc in top_5:
            print(f"- {proc['name']}: {proc['cpu_percent']}%")
    
    # ============= TASK EXECUTION FEATURES =============
    
    def get_time(self):
        """Get current time"""
        now = datetime.datetime.now()
        time_str = now.strftime("%I:%M %p")
        self.speak(f"The current time is {time_str}")
        return time_str
    
    def get_date(self):
        """Get current date"""
        now = datetime.datetime.now()
        date_str = now.strftime("%B %d, %Y")
        self.speak(f"Today is {date_str}")
        return date_str
    
    def search_web(self, query):
        """Search the web"""
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        self.speak(f"Searching for {query}")
    
    def open_website(self, url):
        """Open a specific website"""
        if not url.startswith('http'):
            url = 'https://' + url
        webbrowser.open(url)
        self.speak(f"Opening {url}")
    
    def get_weather(self, city=""):
        """Get weather information"""
        if not REQUESTS_AVAILABLE:
            self.speak("Weather feature not available. Please install requests library.")
            return
            
        api_key = self.config.get('weather_api_key', '')
        if not api_key:
            self.speak("Weather API key not configured")
            return
        
        if not city:
            city = "London"
        
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url, timeout=5)
            data = response.json()
            
            if response.status_code == 200:
                temp = data['main']['temp']
                desc = data['weather'][0]['description']
                self.speak(f"The temperature in {city} is {temp} degrees celsius with {desc}")
            else:
                self.speak("Could not fetch weather information")
        except Exception as e:
            self.speak("Error fetching weather data")
    
    def create_file(self, filename):
        """Create a new file"""
        try:
            Path(filename).touch()
            self.speak(f"File {filename} created")
        except Exception as e:
            self.speak(f"Could not create file {filename}")
    
    def create_folder(self, foldername):
        """Create a new folder"""
        try:
            Path(foldername).mkdir(exist_ok=True)
            self.speak(f"Folder {foldername} created")
        except Exception as e:
            self.speak(f"Could not create folder {foldername}")
    
    def take_screenshot(self):
        """Take a screenshot"""
        try:
            import pyautogui
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
            pyautogui.screenshot(filename)
            self.speak(f"Screenshot saved as {filename}")
        except ImportError:
            self.speak("Screenshot feature requires pyautogui. Please install it.")
        except Exception as e:
            self.speak("Could not take screenshot")
    
    # ============= COMMAND PROCESSING =============
    
    def process_command(self, command):
        """Process and execute commands"""
        if not command:
            return
        
        # Greetings
        if any(word in command for word in ['hello', 'hi', 'hey']):
            self.speak("Hello! How can I help you today?")
        
        # Time and Date
        elif 'time' in command:
            self.get_time()
        
        elif 'date' in command:
            self.get_date()
        
        # Applications
        elif 'open notepad' in command:
            self.open_application('notepad')
        
        elif 'open calculator' in command:
            self.open_application('calculator')
        
        elif 'open browser' in command:
            self.open_application('browser')
        
        elif 'open terminal' in command or 'open command prompt' in command:
            self.open_application('terminal')
        
        elif 'open file explorer' in command or 'open files' in command:
            self.open_application('file explorer')
        
        # System Control
        elif 'shutdown' in command:
            self.speak("Are you sure you want to shutdown? Say yes to confirm.")
            # In production, wait for confirmation
            # For now, just acknowledge
            self.speak("Shutdown command recognized but not executed for safety")
        
        elif 'restart' in command:
            self.speak("Restart command recognized but not executed for safety")
        
        elif 'sleep' in command or 'hibernate' in command:
            self.speak("Sleep command recognized but not executed for safety")
        
        elif 'system info' in command or 'system status' in command:
            self.get_system_info()
        
        elif 'running processes' in command or 'task manager' in command:
            self.list_running_processes()
        
        # Web functions
        elif 'search' in command:
            query = command.replace('search', '').strip()
            if query:
                self.search_web(query)
            else:
                self.speak("What would you like me to search for?")
        
        elif 'open youtube' in command:
            self.open_website('youtube.com')
        
        elif 'open google' in command:
            self.open_website('google.com')
        
        elif 'open github' in command:
            self.open_website('github.com')
        
        # File operations
        elif 'create file' in command:
            filename = command.replace('create file', '').strip()
            if filename:
                self.create_file(filename)
            else:
                self.speak("What should I name the file?")
        
        elif 'create folder' in command:
            foldername = command.replace('create folder', '').strip()
            if foldername:
                self.create_folder(foldername)
            else:
                self.speak("What should I name the folder?")
        
        elif 'screenshot' in command or 'take screenshot' in command:
            self.take_screenshot()
        
        # Weather
        elif 'weather' in command:
            city = command.replace('weather', '').strip()
            self.get_weather(city)
        
        # Exit
        elif any(word in command for word in ['exit', 'quit', 'goodbye', 'bye']):
            self.speak("Goodbye! Have a great day!")
            return False
        
        # Help
        elif 'help' in command or 'what can you do' in command:
            self.show_help()
        
        else:
            self.speak("I didn't understand that command. Say 'help' for available commands.")
        
        return True
    
    def show_help(self):
        """Show available commands"""
        help_text = """
        I can help you with the following:
        
        Time & Date:
        - What's the time?
        - What's the date?
        
        Applications:
        - Open notepad/calculator/browser/terminal/file explorer
        
        System Control:
        - System info / System status
        - Running processes
        - Shutdown / Restart / Sleep (confirmation required)
        
        Web:
        - Search [query]
        - Open YouTube/Google/GitHub
        
        File Operations:
        - Create file [filename]
        - Create folder [foldername]
        - Take screenshot
        
        Other:
        - Weather [city]
        - Help
        - Exit/Quit/Goodbye
        """
        print(help_text)
        self.speak("I've printed the help information on screen. I can help with time, applications, system control, web searches, file operations, and more.")
    
    def run_voice_mode(self):
        """Run in voice command mode"""
        if not SR_AVAILABLE:
            self.speak("Voice recognition not available. Please install SpeechRecognition and use text mode.")
            return
            
        self.speak("Jarvis initialized. Voice mode activated. Say 'help' for available commands.")
        
        while True:
            try:
                command = self.listen()
                if command:
                    should_continue = self.process_command(command)
                    if not should_continue:
                        break
            except KeyboardInterrupt:
                self.speak("Shutting down Jarvis")
                break
    
    def run_text_mode(self):
        """Run in text input mode"""
        self.speak("Jarvis initialized. Text mode activated. Type 'help' for available commands.")
        print("\n" + "="*50)
        print("JARVIS - Text Mode")
        print("="*50 + "\n")
        
        while True:
            try:
                command = self.get_text_input()
                if command:
                    should_continue = self.process_command(command)
                    if not should_continue:
                        break
            except KeyboardInterrupt:
                self.speak("Shutting down Jarvis")
                break


def main():
    """Main entry point"""
    print("""
    ╔════════════════════════════════════════════════╗
    ║                                                ║
    ║         JARVIS - Just A Rather Very            ║
    ║            Intelligent System                  ║
    ║                                                ║
    ║        Your Personal AI Assistant              ║
    ║                                                ║
    ╚════════════════════════════════════════════════╝
    """)
    
    jarvis = Jarvis()
    
    # Check if running with voice or text mode
    if len(sys.argv) > 1 and sys.argv[1] == '--text':
        jarvis.run_text_mode()
    else:
        print("\nMode Selection:")
        print("1. Voice Mode (requires microphone)")
        print("2. Text Mode")
        
        try:
            choice = input("\nSelect mode (1/2) [default: 2]: ").strip()
            
            if choice == '1':
                jarvis.run_voice_mode()
            else:
                jarvis.run_text_mode()
        except KeyboardInterrupt:
            print("\nGoodbye!")


if __name__ == "__main__":
    main()
