#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me that causes server to respond with  message containing You got me! in the body of the response
curl -sLH "Origin: HolbertonSchool" -d "user_id=98" -X PUT 0:5000/catch_me
