"""
List of common ignored process that are running on a usual installation. I don't run
all of Windows so are likely stuff missing...
"""
IGNORE_LIST = [
    # This process is used by Windows to host application frames.
    "ApplicationFrameHost.exe",
    # not sure
    "audiodg.exe"
    #  This is a process that is used by the Visual Studio Code editor.
    "Code.exe",
    # todo(matt): could be WSLv2 I dont use it
    # start git bash instead - dont allow direct bash
    "bash.exe",
    # This is a process that is used to host a command prompt window.
    "conhost.exe",
    # This is a process that is used by Google Chrome to handle crashes.
    "crashpad_handler.exe",
    # It is a critical Windows process that is responsible for managing the Windows
    # Session Manager.
    "csrss.exe",
    # This is a process that is used by the Microsoft Defender Application Guard.
    "dasHost.exe",
    #
    "DataExchangeHost.exe"
    # This is a process that is used by Windows to host dynamic-link libraries (DLLs).
    "dllhost.exe",
    #  This is a process that is used by Windows
    "dwm.exe",
    # is the Windows Explorer process. It is responsible for managing the Windows
    # desktop, taskbar, and Start menu. It is a legitimate Windows process and it
    # should not be deleted or modified.
    "explorer.exe",
    # is the Free Download Manager process. It is a legitimate Windows application
    # that is used to download files from the internet. It is not a virus or malware,
    # and it should not be deleted or modified.
    "fdm.exe",
    # fontdrvhost.exe is a font driver host process that is used to manage fonts
    # on Windows.
    "fontdrvhost.exe",
    # fsnotifier.exe is a file system notification service that is used to notify
    # applications of changes to files and folders.
    "fsnotifier.exe",
    # google member benefits
    "googleone.exe",
    # This is a process that is used by Google Chrome to handle crashes.
    "GoogleCrashHandler.exe",
    # This is a 64-bit version of the GoogleCrashHandler.exe process.
    "GoogleCrashHandler64.exe",
    # This is a service that manages storage on your computer.
    "IAStorDataMgrSvc.exe",
    # This try area application
    "IAStorIcon.exe",
    # This is a service that is used by the Windows Defender Application Guard.
    "LDSvc.exe",
    #  This is a process that is used by the Windows Lock Screen.
    "LockApp.exe",
    # is the Local Security Authority Subsystem Service process. It is a critical
    # Windows process that is responsible for managing user accounts and passwords.
    "lsass.exe",
    # This is a process that is used by the Antimalware Service Executable
    # (MsMpEng.exe) to scan your computer for malware.
    "MsMpEng.exe",
    # This is a service that is used by the Windows Server Message Block (SMB) protocol.
    "NisSrv.exe",
    "Registry",
    # This is a process that is used by Windows to manage background apps.
    "RuntimeBroker.exe",
    # This is a service that is used by the Microsoft Security Client service.
    "SMSvcHost.exe",
    # This is a process that is used by the Windows Search app.
    "SearchApp.exe",
    # This is a process that is used by the Windows Search service to index your
    # computer so that you can search for files and folders more quickly.
    "SearchIndexer.exe",
    # This is a service that is used by Windows Defender to scan your
    # computer for malware.
    "SecurityHealthService.exe",
    # This is an icon that is used to represent the SecurityHealthService.exe service.
    "SecurityHealthSystray.exe",
    # This is a service that is used by Windows to manage Group Policy.
    "SgrmBroker.exe",
    # This is a process that is used by Windows to host the Windows Shell Experience.
    "ShellExperienceHost.exe",
    # This is a process that is used by Windows to host the
    # Windows Start Menu Experience.
    "StartMenuExperienceHost.exe",
    # This is a process that represents the time that the CPU is not being
    # used by other processes.
    "System Idle Process",
    # This is a process that is used by Windows to manage the operating system.
    "System",
    # This is a process that is used to open the Windows Settings app.
    "SystemSettings.exe",
    # This is a process that is used by Windows to manage text input.
    "TextInputHost.exe",
    # This is a service that is used by Windows to manage Windows Driver
    # Foundation (WDF) drivers.
    "WUDFHost.exe",
    # is a terminal emulator for Windows that is used to run Linux command-line
    # tools on Windows.
    "mintty.exe",
    # python is python
    "python.exe",
    #  is a dynamic-link library (DLL) that is used to load and run other DLLs.
    "rundll32.exe",
    # This service indexes your computer so that you can search for files and
    # folders more quickly.
    "SearchIndexer.exe",
    # is the Services Manager process that is used to manage Windows services.
    "services.exe",
    # This service hosts various Windows driver-related services.
    "svchost.exe",
    # is the Session Initialization Host process that is used to initialize
    # Windows sessions.
    "sihost.exe",
    # is a system process that is responsible for starting the Windows Security System.
    "smss.exe",
    # is the Print Spooler service process that is used to manage print jobs.
    "spoolsv.exe",
    # is a system process that hosts multiple Windows tasks.
    "taskhostw.exe",
    # This service synchronizes the time on your computer with other computers
    # on the network.
    "w32time.exe",
    # This service manages audio playback and recording.
    "wdmaud.exe",
    # is a system process that initializes Windows.
    "wininit.exe",
    #  is the Windows Logon process that is responsible for logging on to Windows.
    "winlogon.exe",
    # is a Windows Wireless LAN Extensibility Framework process that is used to
    # manage wireless network connections.
    "wlanext.exe",
    # This service downloads and installs Windows updates.
    "wuauclt.exe",
    # This service repairs problems with Windows Update.
    "wuauserv.exe",
]
