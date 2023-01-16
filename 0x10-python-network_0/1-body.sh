#!/bin/bash
# Takes in URL, sends GET, displays body of response
curl -sLX GET "$1"
