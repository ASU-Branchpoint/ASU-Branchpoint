#!/bin/bash

# 1. Pull the newest version of the game from the ASU-Branchpoint registry
docker pull ghcr.io/asu-branchpoint/incident-response-game:latest

# 2. Stop and remove the old game container (if it exists)
docker stop cir-game || true
docker rm cir-game || true

# 3. Start the newly downloaded game on port 8080
docker run -d -p 8080:80 --name cir-game ghcr.io/asu-branchpoint/incident-response-game:latest

# 4. Clean up old, unused docker images to save hard drive space
docker image prune -f

# NOTE~ This is for the host, for now intended to be Chris's Spare Laptop