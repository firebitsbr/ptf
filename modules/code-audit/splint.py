#!/usr/bin/env python
#####################################
# Installation module for splint
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Mauro Risonho de Paula Assumpcao (firebits)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update splint, a tool for static C/C++ Code"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="http://git.code.sf.net/p/flawfinder/code" 

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="splint"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="gcc,make,gzip,tar,automake"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},make install"

LAUNCHER="cfr"
