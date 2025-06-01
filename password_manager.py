#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import getpass
from datetime import datetime
from cryptography.fernet import Fernet
from colorama import init, Fore, Back, Style
from rich.console import Console
from rich.table import Table
from rich import box
from tkinter import filedialog
import tkinter as tk

class PasswordManager:
    def __init__(self):
        self.banner = f"""
{Fore.CYAN}╔═══════════════════════════════════════════════════════════════════╗
║ {Fore.YELLOW}██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗{Fore.CYAN} ║
║ {Fore.YELLOW}██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗{Fore.CYAN} ║
║ {Fore.YELLOW}██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║{Fore.CYAN} ║
║ {Fore.YELLOW}██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║{Fore.CYAN} ║
║ {Fore.YELLOW}██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝{Fore.CYAN} ║
║ {Fore.YELLOW}╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝{Fore.CYAN}  ║
║                                                                   ║
║ {Fore.GREEN}███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗{Fore.CYAN}      ║
║ {Fore.GREEN}████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗{Fore.CYAN}     ║
║ {Fore.GREEN}██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝{Fore.CYAN}     ║
║ {Fore.GREEN}██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗{Fore.CYAN}     ║
║ {Fore.GREEN}██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║{Fore.CYAN}     ║
║ {Fore.GREEN}╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝{Fore.CYAN}     ║
║                                                                   ║
║ {Fore.RED}███████╗███████╗██████╗  ██████╗ ███████╗██╗██╗   ██╗███████╗{Fore.CYAN}     ║
║ {Fore.RED}╚══███╔╝██╔════╝██╔══██╗██╔═══██╗██╔════╝██║██║   ██║██╔════╝{Fore.CYAN}     ║
║ {Fore.RED}  ███╔╝ █████╗  ██████╔╝██║   ██║█████╗  ██║██║   ██║█████╗  {Fore.CYAN}     ║
║ {Fore.RED} ███╔╝  ██╔══╝  ██╔══██╗██║   ██║██╔══╝  ██║╚██╗ ██╔╝██╔══╝  {Fore.CYAN}     ║
║ {Fore.RED}███████╗███████╗██║  ██║╚██████╔╝██║     ██║ ╚████╔╝ ███████╗{Fore.CYAN}     ║
║ {Fore.RED}╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝  ╚═══╝  ╚══════╝{Fore.CYAN}     ║
║                                                                   ║
║      {Fore.MAGENTA}[{Fore.WHITE}❖{Fore.MAGENTA}] {Fore.YELLOW}zerofive_sec{Fore.WHITE} - {Fore.GREEN}febryan.000 {Fore.MAGENTA}[{Fore.WHITE}❖{Fore.MAGENTA}]{Fore.CYAN}                  ║
╚═══════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
        self.console = Console()
        self.storage_path = os.path.expanduser("~/.password_manager")
        self.db_path = os.path.join(self.storage_path, "passwords.enc")
        self.key_path = os.path.join(self.storage_path, "key.key")
        self.passwords = {}
        self.fernet = None
        self.initialize()
        # Initialize tkinter root window but keep it hidden
        self.root = tk.Tk()
        self.root.withdraw()

    def initialize(self):
        """Initialize the password manager, create necessary directories and files."""
        if not os.path.exists(self.storage_path):
            os.makedirs(self.storage_path)
        
        if not os.path.exists(self.key_path):
            key = Fernet.generate_key()
            with open(self.key_path, "wb") as key_file:
                key_file.write(key)
        
        with open(self.key_path, "rb") as key_file:
            self.fernet = Fernet(key_file.read())
        
        if os.path.exists(self.db_path):
            self.load_passwords()

    def load_passwords(self):
        """Load encrypted passwords from storage."""
        try:
            with open(self.db_path, "rb") as f:
                encrypted_data = f.read()
                if encrypted_data:
                    decrypted_data = self.fernet.decrypt(encrypted_data)
                    self.passwords = json.loads(decrypted_data)
        except Exception as e:
            print(f"{Fore.RED}[!] Error loading passwords: {str(e)}{Style.RESET_ALL}")

    def save_passwords(self):
        """Save passwords to encrypted storage."""
        try:
            encrypted_data = self.fernet.encrypt(json.dumps(self.passwords).encode())
            with open(self.db_path, "wb") as f:
                f.write(encrypted_data)
            print(f"{Fore.GREEN}[+] Passwords saved successfully{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[!] Error saving passwords: {str(e)}{Style.RESET_ALL}")

    def add_password(self, category, name, username, password, url="", notes=""):
        """Add a new password entry."""
        if category not in self.passwords:
            self.passwords[category] = []
        
        entry = {
            "name": name,
            "username": username,
            "password": password,
            "url": url,
            "notes": notes,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        
        self.passwords[category].append(entry)
        self.save_passwords()

    def list_passwords(self, category=None):
        """List all passwords or passwords in a specific category."""
        table = Table(title="Password Manager - Stored Passwords", box=box.DOUBLE_EDGE)
        
        table.add_column("Category", style="cyan")
        table.add_column("Name", style="yellow")
        table.add_column("Username", style="green")
        table.add_column("URL", style="blue")
        table.add_column("Last Updated", style="magenta")
        
        for cat in self.passwords if not category else [category]:
            if cat in self.passwords:
                for entry in self.passwords[cat]:
                    table.add_row(
                        cat,
                        entry["name"],
                        entry["username"],
                        entry["url"],
                        entry["updated_at"].split("T")[0]
                    )
        
        self.console.print(table)

    def get_password(self, category, name):
        """Retrieve a specific password."""
        if category in self.passwords:
            for entry in self.passwords[category]:
                if entry["name"] == name:
                    return entry
        return None

    def update_password(self, category, name, new_password):
        """Update an existing password."""
        if category in self.passwords:
            for entry in self.passwords[category]:
                if entry["name"] == name:
                    entry["password"] = new_password
                    entry["updated_at"] = datetime.now().isoformat()
                    self.save_passwords()
                    return True
        return False

    def delete_password(self, category, name):
        """Delete a password entry."""
        if category in self.passwords:
            self.passwords[category] = [
                entry for entry in self.passwords[category]
                if entry["name"] != name
            ]
            if not self.passwords[category]:
                del self.passwords[category]
            self.save_passwords()
            return True
        return False

    def export_passwords(self):
        """Export passwords to a JSON file using file dialog."""
        try:
            # Show file dialog to choose save location
            file_path = filedialog.asksaveasfilename(
                defaultextension=".json",
                filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
                title="Save Password File As"
            )
            
            if file_path:  # If a file path was selected
                with open(file_path, "w") as f:
                    json.dump(self.passwords, f, indent=4)
                print(f"{Fore.GREEN}[+] Passwords exported to {file_path}{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}[!] Export cancelled{Style.RESET_ALL}")
                
        except Exception as e:
            print(f"{Fore.RED}[!] Error exporting passwords: {str(e)}{Style.RESET_ALL}")

    def import_passwords(self):
        """Import passwords from a JSON file using file dialog."""
        try:
            # Show file dialog to choose file to import
            file_path = filedialog.askopenfilename(
                defaultextension=".json",
                filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
                title="Select Password File to Import"
            )
            
            if file_path:  # If a file was selected
                with open(file_path, "r") as f:
                    new_passwords = json.load(f)
                    for category in new_passwords:
                        if category not in self.passwords:
                            self.passwords[category] = []
                        self.passwords[category].extend(new_passwords[category])
                self.save_passwords()
                print(f"{Fore.GREEN}[+] Passwords imported successfully{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}[!] Import cancelled{Style.RESET_ALL}")
                
        except Exception as e:
            print(f"{Fore.RED}[!] Error importing passwords: {str(e)}{Style.RESET_ALL}")

def main():
    init()  # Initialize colorama
    pm = PasswordManager()
    print(pm.banner)
    
    while True:
        print(f"\n{Fore.CYAN}=== Menu Utama ==={Style.RESET_ALL}")
        print(f"{Fore.YELLOW}1. Tambah Password{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}2. Lihat Password{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}3. Update Password{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}4. Hapus Password{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}5. Export Password{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}6. Import Password{Style.RESET_ALL}")
        print(f"{Fore.RED}0. Keluar{Style.RESET_ALL}")
        
        choice = input(f"\n{Fore.GREEN}Pilihan Anda: {Style.RESET_ALL}")
        
        if choice == "1":
            category = input(f"{Fore.CYAN}Kategori: {Style.RESET_ALL}")
            name = input(f"{Fore.CYAN}Nama: {Style.RESET_ALL}")
            username = input(f"{Fore.CYAN}Username: {Style.RESET_ALL}")
            password = getpass.getpass(f"{Fore.CYAN}Password: {Style.RESET_ALL}")
            url = input(f"{Fore.CYAN}URL (opsional): {Style.RESET_ALL}")
            notes = input(f"{Fore.CYAN}Catatan (opsional): {Style.RESET_ALL}")
            
            pm.add_password(category, name, username, password, url, notes)
            print(f"{Fore.GREEN}[+] Password berhasil ditambahkan{Style.RESET_ALL}")
        
        elif choice == "2":
            category = input(f"{Fore.CYAN}Kategori (kosongkan untuk semua): {Style.RESET_ALL}")
            pm.list_passwords(category if category else None)
        
        elif choice == "3":
            category = input(f"{Fore.CYAN}Kategori: {Style.RESET_ALL}")
            name = input(f"{Fore.CYAN}Nama: {Style.RESET_ALL}")
            new_password = getpass.getpass(f"{Fore.CYAN}Password Baru: {Style.RESET_ALL}")
            
            if pm.update_password(category, name, new_password):
                print(f"{Fore.GREEN}[+] Password berhasil diupdate{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}[!] Password tidak ditemukan{Style.RESET_ALL}")
        
        elif choice == "4":
            category = input(f"{Fore.CYAN}Kategori: {Style.RESET_ALL}")
            name = input(f"{Fore.CYAN}Nama: {Style.RESET_ALL}")
            
            if pm.delete_password(category, name):
                print(f"{Fore.GREEN}[+] Password berhasil dihapus{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}[!] Password tidak ditemukan{Style.RESET_ALL}")
        
        elif choice == "5":
            print(f"{Fore.CYAN}[*] Membuka dialog pemilihan lokasi file...{Style.RESET_ALL}")
            pm.export_passwords()
        
        elif choice == "6":
            print(f"{Fore.CYAN}[*] Membuka dialog pemilihan file...{Style.RESET_ALL}")
            pm.import_passwords()
        
        elif choice == "0":
            print(f"\n{Fore.GREEN}Terima kasih telah menggunakan Password Manager!{Style.RESET_ALL}")
            sys.exit(0)
        
        else:
            print(f"{Fore.RED}[!] Pilihan tidak valid{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
