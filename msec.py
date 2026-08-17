#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔══════════════════════════════════════════════════════════════╗
║                    MSEC TOOLKIT v2.0                        ║
║            Cybersecurity Tools Collection Suite             ║
║                                                              ║
║              Developer: Eng.Malek Alastal                   ║
║              Platform: MSEC Security Framework               ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import random
import platform
import shutil
import subprocess

from colorama import init, Fore, Style

# ============================================================
# INITIALIZATION
# ============================================================

init(autoreset=True)

VERSION = "2.0"
CODENAME = "NEON CORE"
DEVELOPER = "Eng.Malek Alastal"

# ============================================================
# COLOR THEME
# ============================================================

CYAN = Fore.CYAN
BLUE = Fore.BLUE
MAGENTA = Fore.MAGENTA
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
RED = Fore.RED
WHITE = Fore.WHITE
DIM = Style.DIM
RESET = Style.RESET_ALL

# ============================================================
# TOOLS
# ============================================================

TOOLS = {
    "1": {
        "name": "Zphisher",
        "repo": "https://github.com/htr-tech/zphisher.git",
        "folder": "zphisher",
        "run": "bash zphisher.sh",
        "desc": "Phishing Framework",
        "emoji": "◈"
    },

    "2": {
        "name": "Storm Breaker",
        "repo": "https://github.com/ultrasecurity/Storm-Breaker.git",
        "folder": "Storm-Breaker",
        "run": "bash storm-breaker.sh",
        "desc": "Device Info Framework",
        "emoji": "⚡"
    },

    "3": {
        "name": "Sherlock",
        "repo": "https://github.com/sherlock-project/sherlock.git",
        "folder": "sherlock",
        "run": "python3 sherlock.py",
        "desc": "OSINT Username Tool",
        "emoji": "⌕"
    },

    "4": {
        "name": "Seeker",
        "repo": "https://github.com/thewhiteh4t/seeker.git",
        "folder": "seeker",
        "run": "python3 seeker.py",
        "desc": "Location Finder",
        "emoji": "⌖"
    }
}

# ============================================================
# TERMINAL UTILITIES
# ============================================================

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def terminal_width():
    try:
        return shutil.get_terminal_size().columns
    except Exception:
        return 50


def line(char="═", length=48, color=CYAN):
    print(f"{color}{char * length}")


def type_text(text, delay=0.012):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


# ============================================================
# STARTUP ANIMATION
# ============================================================

def matrix_effect(duration=1.2):
    clear_screen()
    chars = "01ABCDEF0123456789<>[]{}#$@"
    end_time = time.time() + duration

    while time.time() < end_time:
        width = min(terminal_width(), 48)
        text = "".join(random.choice(chars) for _ in range(width))
        print(f"{DIM}{GREEN}{text}")
        time.sleep(0.035)

    clear_screen()


def loading_animation(text="Initializing MSEC CORE", duration=1.8):
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end_time = time.time() + duration

    while time.time() < end_time:
        for frame in frames:
            sys.stdout.write(f"\r{CYAN}{frame} {WHITE}{text}...")
            sys.stdout.flush()
            time.sleep(0.07)

    sys.stdout.write(f"\r{GREEN}✓ {WHITE}{text} {GREEN}[ONLINE]{RESET}\n")


# ============================================================
# MAIN BANNER
# ============================================================

def show_banner():
    width = 46

    print()
    print(f"{BLUE}╔{'═' * width}╗")
    print(f"{BLUE}║{CYAN}{'MSEC SECURITY FRAMEWORK'.center(width)}{BLUE}║")
    print(f"{BLUE}╠{'═' * width}╣")

    # الشعار الاحترافي القوي (3D Heavy Block MSEC)
    logo_lines = [
        "███╗   ███╗███████╗███████╗██████╗ ",
        "████╗ ████║██╔════╝██╔════╝██╔════╝",
        "██╔████╔██║███████╗█████╗  ██║     ",
        "██║╚██╔╝██║╚════██║██╔══╝  ██║     ",
        "██║ ╚═╝ ██║███████║███████╗╚██████╗",
        "╚═╝     ╚═╝╚══════╝╚══════╝ ╚═════╝"
    ]

    for line_text in logo_lines:
        print(f"{BLUE}║{CYAN}{line_text.center(width)}{BLUE}║")

    print(f"{BLUE}╠{'═' * width}╣")

    info = [
        f"MSEC TOOLKIT v{VERSION}",
        f"{CODENAME}",
        f"{DEVELOPER}",
        f"SYS: {platform.system()} | {platform.machine()}"
    ]

    for text in info:
        print(f"{BLUE}║{WHITE}{text.center(width)}{BLUE}║")

    print(f"{BLUE}╚{'═' * width}╝")
    print()


# ============================================================
# STATUS PANEL
# ============================================================

def show_status():
    print(f"{DIM}{WHITE}┌{'─' * 46}┐")
    print(f"{DIM}{WHITE}│ {GREEN}● MSEC CORE{WHITE}  {GREEN}ONLINE{WHITE}{' ' * 22}│")
    print(f"{DIM}{WHITE}│ {CYAN}● PLATFORM{WHITE}   {platform.system()} {platform.machine()}{' ' * max(1, (31 - len(platform.system() + platform.machine())))}│")
    print(f"{DIM}{WHITE}│ {MAGENTA}● MODULES{WHITE}    {len(TOOLS)} security modules{' ' * 13}│")
    print(f"{DIM}{WHITE}└{'─' * 46}┘")
    print()


# ============================================================
# MENU
# ============================================================

def animate_menu():
    print(f"{CYAN}┌{'─' * 46}┐")

    for key, tool in TOOLS.items():
        time.sleep(0.04)
        name = tool["name"]
        desc = tool["desc"]
        emoji = tool["emoji"]

        line_content = f" [{key}] {emoji} {name:<13} {desc:<18}"
        print(f"{CYAN}│{MAGENTA}{line_content:<46}{CYAN}│")

    print(f"{CYAN}│{YELLOW} [5] ⚙ Install All Modules{' ' * 20}{CYAN}│")
    print(f"{CYAN}│{RED} [0] Exit MSEC{' ' * 32}{CYAN}│")
    print(f"{CYAN}└{'─' * 46}┘")


# ============================================================
# REQUIREMENTS
# ============================================================

def command_exists(command):
    return shutil.which(command) is not None


def install_requirements():
    print()
    line("─", 48, BLUE)
    print(f"{YELLOW}[*] Checking MSEC dependencies...")

    if not command_exists("git"):
        print(f"{YELLOW}[!] Git not found.")
        if os.name != "nt":
            os.system("pkg install git -y -q 2>/dev/null || apt install git -y -q 2>/dev/null")
    else:
        print(f"{GREEN}[✓] Git detected.")

    try:
        import colorama
        print(f"{GREEN}[✓] Colorama detected.")
    except ImportError:
        print(f"{YELLOW}[*] Installing colorama...")
        os.system(f"{sys.executable} -m pip install colorama -q")

    print()
    line("─", 48, BLUE)


# ============================================================
# INSTALL TOOL
# ============================================================

def install_tool(tool_key):
    tool = TOOLS[tool_key]
    print()
    line("═", 48, MAGENTA)
    print(f"{CYAN}◈ MODULE: {WHITE}{tool['emoji']} {tool['name']}")
    print(f"{DIM}{WHITE}{tool['desc']}")
    line("═", 48, MAGENTA)

    folder = tool["folder"]

    if os.path.exists(folder):
        print(f"{YELLOW}[!] Module already exists: {folder}")
        return True

    if not command_exists("git"):
        print(f"{RED}[✗] Git is not installed.")
        return False

    print(f"{CYAN}[*] Repository: {WHITE}{tool['repo']}")
    print(f"{CYAN}[*] Cloning module...")

    result = subprocess.run(
        ["git", "clone", tool["repo"]],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        print(f"{RED}[✗] Installation failed.")
        if result.stderr:
            print(f"{DIM}{RED}{result.stderr.strip()}")
        return False

    print(f"{GREEN}[✓] {tool['name']} installed successfully.")

    requirements = os.path.join(folder, "requirements.txt")
    if os.path.exists(requirements):
        print(f"{CYAN}[*] Installing Python requirements...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements, "-q"])
        print(f"{GREEN}[✓] Dependencies processed.")

    return True


# ============================================================
# RUN TOOL
# ============================================================

def run_tool(tool_key):
    tool = TOOLS[tool_key]
    folder = tool["folder"]

    if not os.path.exists(folder):
        print(f"{RED}[✗] {tool['name']} is not installed.")
        answer = input(f"{YELLOW}[?] Install it now? [y/N]: ").strip().lower()
        if answer != "y":
            return
        if not install_tool(tool_key):
            return

    print()
    line("═", 48, GREEN)
    print(f"{GREEN}▶ Launching {WHITE}{tool['name']}")
    print(f"{DIM}{WHITE}Module: {folder}")
    line("═", 48, GREEN)

    try:
        subprocess.run(tool["run"], shell=True, cwd=folder)
    except Exception as error:
        print(f"{RED}[✗] Runtime error: {error}")

    input(f"\n{YELLOW}[↩] Press Enter to return to MSEC...")


# ============================================================
# INSTALL ALL
# ============================================================

def install_all():
    print()
    line("═", 48, MAGENTA)
    print(f"{MAGENTA}⚡ MSEC MASS MODULE DEPLOYMENT")
    line("═", 48, MAGENTA)

    success = 0
    for key in TOOLS:
        if install_tool(key):
            success += 1
        time.sleep(0.4)

    print()
    line("─", 48, BLUE)
    print(f"{GREEN}[✓] Deployment complete.")
    print(f"{CYAN}[+] Successful modules: {WHITE}{success}/{len(TOOLS)}")
    line("─", 48, BLUE)


# ============================================================
# TOOL SUB-MENU
# ============================================================

def tool_menu(choice):
    tool = TOOLS[choice]

    while True:
        clear_screen()
        show_banner()

        width = 46
        print(f"{CYAN}╔{'═' * width}╗")
        print(f"{CYAN}║ {WHITE}{tool['emoji']} {tool['name']}{' ' * max(1, (width - 3 - len(tool['name'])))}║")
        print(f"{CYAN}╠{'═' * width}╣")
        print(f"{CYAN}║ {DIM}{WHITE}{tool['desc']}{' ' * max(1, (width - 1 - len(tool['desc'])))}║")
        print(f"{CYAN}╚{'═' * width}╝")
        print()

        print(f"{MAGENTA}[1] {WHITE}Install Module")
        print(f"{MAGENTA}[2] {WHITE}Launch Module")
        print(f"{MAGENTA}[3] {WHITE}Back")
        print()

        action = input(f"{CYAN}MSEC/{tool['name']} » {WHITE}").strip()

        if action == "1":
            install_tool(choice)
            input(f"\n{YELLOW}[↩] Press Enter...")
        elif action == "2":
            run_tool(choice)
        elif action == "3":
            break
        else:
            print(f"{RED}[✗] Invalid selection.")
            time.sleep(0.8)


# ============================================================
# MAIN
# ============================================================

def main():
    try:
        matrix_effect()
        show_banner()
        loading_animation("Booting MSEC Security Core", 1.5)
        loading_animation("Loading Security Modules", 1.2)
        install_requirements()
        time.sleep(0.5)

        while True:
            clear_screen()
            show_banner()
            show_status()
            animate_menu()
            print()

            choice = input(f"{CYAN}MSEC@CORE {MAGENTA}» {WHITE}").strip()

            if choice == "0":
                clear_screen()
                show_banner()
                print(f"{CYAN}[*] Shutting down MSEC CORE...")
                loading_animation("Closing modules", 0.8)
                print()
                type_text(f"{MAGENTA}MSEC SECURITY FRAMEWORK")
                type_text(f"{CYAN}Developer: {WHITE}{DEVELOPER}")
                type_text(f"{GREEN}Session terminated safely.")
                print()
                sys.exit(0)

            elif choice == "5":
                install_all()
                input(f"\n{YELLOW}[↩] Press Enter to continue...")

            elif choice in TOOLS:
                tool_menu(choice)

            else:
                print()
                print(f"{RED}[✗] Unknown command.")
                print(f"{DIM}{WHITE}Use 0-5 to navigate MSEC.")
                time.sleep(1)

    except KeyboardInterrupt:
        print(f"\n\n{RED}[!] MSEC session interrupted.")
        sys.exit(0)

    except Exception as error:
        print(f"\n\n{RED}[✗] Fatal error: {DIM}{WHITE}{error}")
        sys.exit(1)


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    if platform.system() == "Windows":
        print(f"{YELLOW}[!] MSEC is optimized for Termux/Linux.")
        input(f"{WHITE}Press Enter to continue...")
    main()
