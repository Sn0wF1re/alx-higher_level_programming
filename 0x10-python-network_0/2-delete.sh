#!/bin/bash
# sends DELETE to URL passed as first arg, displays body of the response
curl -sLX DELETE "$1"
