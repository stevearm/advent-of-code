#!/bin/sh
./scheme --load mylibs.scheme --load 2024-02/process.scheme --eval '(run-test)'
