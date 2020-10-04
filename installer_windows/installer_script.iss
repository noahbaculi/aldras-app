; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Aldras"
#define MyAppVersion "2020.2"
#define MyAppPublisher "Aldras"
#define MyAppURL "https://aldras.com/"
#define MyAppExeName "Aldras.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{F49A6057-F3F6-474E-9D93-AAA96A11542E}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DisableProgramGroupPage=yes
LicenseFile=C:\Users\Noah Baculi\Documents\aldras\data\license.txt
; Remove the following line to run in administrative install mode (install for all users.)
PrivilegesRequired=lowest
; PrivilegesRequiredOverridesAllowed=dialog ; Disabled to only allow installation for single user due to permission issues attempting to access globally installed resources
SetupIconFile=C:\Users\Noah Baculi\Documents\aldras\data\aldras.ico
WizardStyle=modern
SolidCompression=yes
Compression=lzma2/ultra64
LZMAUseSeparateProcess=yes
LZMADictionarySize=1048576
LZMANumFastBytes=273    
OutputBaseFilename=aldras-setup-2020-2

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\Noah Baculi\Documents\aldras\dist\Aldras\Aldras.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Noah Baculi\Documents\aldras\dist\Aldras\*"; Excludes: "data\settings.json"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\Noah Baculi\Documents\aldras\dist\Aldras\data\settings.json"; DestDir: "{app}\data"; Flags: ignoreversion onlyifdoesntexist
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
; Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

