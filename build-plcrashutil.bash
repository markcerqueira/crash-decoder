#!/bin/bash

# builds plcrashutil from source
# modified from: https://github.com/mumble-voip/mumble-iphoneos/blob/master/Dependencies/plcrashreporter/build-plcrashutil.bash

# directory to check out the plcrashutil source
ROOT=$(mktemp -d -t plcrashutil)/src
WORKING_DIRECTORY=$(pwd)

mkdir -p ${ROOT}

svn checkout http://plcrashreporter.googlecode.com/svn/trunk/ ${ROOT}

cd ${ROOT}

# build it!
/Applications/Xcode.app/Contents/Developer/usr/bin/xcodebuild -project CrashReporter.xcodeproj -target plcrashutil build

mkdir -p ${HOME}/bin

cp -v ${ROOT}/build/Release-MacOSX/plcrashutil ${WORKING_DIRECTORY}/plcrashutil

# clean up by removing plcrashutil source
rm -rf ${ROOT}