# Pocket-Science-Lab
This repository hosts the programs for additional experiments and sensor plugins for ExpEYES. 

[![Build Status](https://travis-ci.org/fossasia/Pocket-Science-Lab.svg?branch=master)](https://travis-ci.org/fossasia/Pocket-Science-Lab)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/18fad6e7f96a49fe8ec531ad40149664)](https://www.codacy.com/app/mb/Pocket-Science-Lab?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=fossasia/Pocket-Science-Lab&amp;utm_campaign=Badge_Grade)

##Communication
Chat: [Pocket Science Slack Channel](http://fossasia.slack.com/messages/pocketscience/) | [Get an Invite](http://fossasia-slack.herokuapp.com/)

##Installation

#### 1. Install ExpEYES
You can install ExpEYES easily on any Linux machine. There are deb files available that we included in the repository. Please find details how to [install ExpEYES in the Readme.md](/ExpEYES/Readme.md).

### 2. Steps to install experiments

The software extension that are available in this repository in the folder /experiments can be installed as follows:
* Copy the programs in home folder

  ####ToDo : 
  Create makefile for installing programs in ExpEYEs directory and make these experiments available in a dropdown menu of main GUI.

### 3. How to run experiments

For Experiments various sensors and experimental setups are required. Typical steps are:
* Connect ExpEYES to your PC/Laptop
* Run Expeyes from Education Menue. The main ExpEYES GUI will popup. Check whether the device is detected.
* Then close the ExpEYES GUI.
* Open the terminal and run the program for e.g.

 `~ $ python coupledpendulum.py`


###4. How to collect and save data

In order to make the experiments useful you need to collect and save data.
* Please describe here how to collect data and to save and use it (TO DO)


## Sensors and Devices

Please check out our list of [supported devices](/sensors/Readme.md).

## Web Connectors

It is possible to collect data and publish it automatically on the web on your own web application or on social networks like Twitter and Facebook. Find more info [web connectors here](/web-connectors/Readme.md).

### Blog posts related to ExpEYES on FOSSASIA blog 
* [Sensor Plugins for ExpEYES](http://blog.fossasia.org/low-cost-laboratory-everyone-sensor-plug-ins-expeyes-measure-temperature-pressure-humidity-wind/)
