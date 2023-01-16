#!/bin/bash
# takes in a URL, sends request to that URL, displays size of body of response
curl -sI "$1" | grep -i Content-Length | cut -d ' ' -f 2 
