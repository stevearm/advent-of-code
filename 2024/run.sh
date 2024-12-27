#!/bin/sh
./scheme --load mylibs.scheme \
         --load 2024-01/process.scheme \
         --load 2024-02/process.scheme \
         --eval '(run-test)'
