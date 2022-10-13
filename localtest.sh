#!/bin/bash
# Builds and runs the docker container locally for testing.
docker build -t nicholasjgraham/nickjgraham.com:latest .
docker run nicholasjgraham/nickjgraham.com:latest

