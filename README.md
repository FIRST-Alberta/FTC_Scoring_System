# FTC_Scoring_System

This is a collection of scripts that will be built into software to implement a scoring system in a box that is mostly automated and user friendly

## Hardware Used

### Server
Intel NUC 11 with:
* Intel Celeron N5105 Quad Core 2GHz Processor
* 16 GB 3200 MHz SDRAM 
* 250 GB NVME Solid State Drive
* Ubuntu 22.04 LTS Operating System

### Network
* Router: D-Link AC3000 High Power Wi-Fi Tri Band Gigabit Mesh Router (DIR-3040)
* Booster(s): D-Link AC1200 Mesh Wi-Fi Range Extender (DAP-1610)

### Display
Raspberry Pi 4 (8GB) with:
* Case with Fan
* 32 GB Class 10 SD Card
* Dedicated 3A Power supply
* FullPageOS

## Server Setup
1. Install Ubuntu 22.04 with username ftc and password ftc
2. Install the [Raspberry Pi Imager](https://www.raspberrypi.com/software/).


### Package Requirements

* pip
    - PySimpleGui
* apt:
    - openjdk-18-jdk

# New FTC Live Installation for Linux

1. Navigate to https://ftc-scoring.firstinspires.org/local/2024. The site should register your operating system as Linux x86_64. Press Download.
2. Open a terminal and use the commands
```
> mkdir ~/Documents/FTCLiveLauncher
> tar -xvf FTCLive CENTERSTAGE 2024-5.0.1-linux_amd64.tar.gz --directory ~/Documents/FTCLiveLauncher
```

3. Rename the file "FTCLive CENTERSTAGE 2024" to "FTCLive"

4. Download a FIRST Tech Challenge logo in a PNG format and copy it to ~/Documents/FTCLiveLauncher/FTC_Logo.png

5. Using the terminal:
```
sudo vim ~/.local/share/applications/ftc_live.desktop
```

6. Copy the following except and paste it in by pressing i followed by CTRL+SHIFT+v. Once the text is pasted, press :x to save and exit.

```
[Desktop Entry]
Encoding=UTF-8
Version=1.0
Type=Application
Terminal=false
Exec=/home/ftc/Documents/FTCLiveLauncher/FTCLive
Name=FTC Live
Icon=/home/ftc/Documents/FTCLiveLauncher/FTC_Logo.png
```

7. Navigate to your applications and click FTC Live to launch the application and complete installation. The system will automatically be launched. Right click on the application in the applications pane to save it to favourites.