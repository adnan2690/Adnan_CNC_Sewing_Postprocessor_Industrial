import os
import subprocess
from PyInstaller.__main__ import run as pyinstaller_run

class IndustrialInstaller:
    def build_executables(self):
        # Build unified application
        self._build_exe(
            "Application_Entry/quantum_unified_loader.py",
            "Adnan_CNC_Suite.exe",
            icon="assets/main_icon.ico"
        )
        
        # Build stitching processor
        self._build_exe(
            "Application_Entry/stitching_launcher.py",
            "Adnan_Stitching_Processor.exe",
            icon="assets/stitch_icon.ico"
        )
        
        # Build template processor
        self._build_exe(
            "Application_Entry/template_launcher.py",
            "Adnan_Template_Processor.exe",
            icon="assets/template_icon.ico"
        )
    
    def _build_exe(self, script, output_name, icon=None):
        args = [
            '--onefile',
            '--windowed',
            f'--name={output_name}',
            '--add-data=Quantum_Core_Engine;Quantum_Core_Engine',
            '--add-data=Military_Grade_UI;Military_Grade_UI',
            '--add-data=Industrial_Export_System;Industrial_Export_System',
            '--distpath=./dist/industrial',
            '--workpath=./build',
            '--specpath=./specs'
        ]
        
        if icon:
            args.append(f'--icon={icon}')
            
        args.append(script)
        pyinstaller_run(args)
    
    def create_installer(self):
        """Create professional Windows installer"""
        iss_script = """
[Setup]
AppName=Adnan CNC Sewing Suite
AppVersion=2.0
AppPublisher=Adnan Abdulmalek CNC Solutions
DefaultDirName={autopf}\\AdnanCNC
DefaultGroupName=Adnan CNC
OutputDir=./dist
OutputBaseFilename=AdnanCNC_Installer
Compression=lzma2
SolidCompression=yes

[Files]
Source: "./dist/industrial/*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs

[Icons]
Name: "{group}\\Adnan CNC Suite"; Filename: "{app}\\Adnan_CNC_Suite.exe"
Name: "{group}\\Stitching Processor"; Filename: "{app}\\Adnan_Stitching_Processor.exe"
Name: "{group}\\Template Processor"; Filename: "{app}\\Adnan_Template_Processor.exe"
Name: "{commondesktop}\\Adnan CNC Suite"; Filename: "{app}\\Adnan_CNC_Suite.exe"
"""
        with open("installer.iss", "w") as f:
            f.write(iss_script)
            
        subprocess.run(["iscc", "installer.iss"], check=True)
        print("Installer created: ./dist/AdnanCNC_Installer.exe")