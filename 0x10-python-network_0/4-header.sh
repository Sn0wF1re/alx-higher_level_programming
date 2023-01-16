#!/bin/bash
# Takes URL as arg, sends GET request, displays body of response
curl -sH "X-School-User-Id: 98" -X GET "$1"
