# 中国版多因子模型的构建、检验与对比
主要参考文献：




## Features
This application does everything required for h-encore related to your PC. This means:
 
 - Automatically installs and configures QCMA if it is not already installed.
 - Automatically installs QCMA USB drivers if necessary.
 - Gets AID and QCMA directory from QCMA automatically.
 - Automatically downloads required tools (psvimgtools, pkg2zip, bittersmile demo and h-encore itself).
 - Allows user to import necessary files if they've already downloaded them *(optional)*.
 - Grabs CMA encryption key from your account ID.
 - Unpackages bittersmile and repackages it with your encryption key and h-encore.
 - Trims excess bittersmile demo files to reduce h-encore file size from ~240MB to ~13MB **without breaking trophy fix** *(optional)*.
 - Moves finished files to your QCMA directory for copying to your PS Vita.
 - Holds your hand along the way.
 
Basically, you just need to read and interact with your Vita.

## Usage

The application has been verified working on all PS Vita models (including PSTV).

Requires .NET 4.5.2 or higher (Windows should automatically download it or link you to it if you don't have it).

Download and extract the [latest release](https://github.com/noahc3/auto-h-encore/releases "latest release") and run it. Further instructions are included in the application itself.

If the application crashes or h-encore fails to install, please [submit an issue](http://https://github.com/noahc3/auto-h-encore/issues "submit an issue"), **do not create an issue on the h-encore Github**, it probably isn't their fault.

## Build

Clone the repository and open the solution in Visual Studio. Build from there.

## Contributing

If you know C and are willing to help out, it would be appreciated if you could help [integrate libVitaMTP into this application](https://github.com/noahc3/auto-h-encore/issues/1).

Other changes are also welcome through pull requests.

## Thanks
