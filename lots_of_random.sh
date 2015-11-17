#!/bin/sh
key=$(dd if=/dev/urandom bs=16 count=1 2>/dev/null | gmd5sum | gcut -d' ' -f1)
iv=$(dd if=/dev/urandom bs=16 count=1 2>/dev/null | gmd5sum | gcut -d' ' -f1)
# makes a bit over 1TB of pseudorandom data REALLY FAST
dd if=/dev/zero bs=65536 count=16384000 2>/dev/null | openssl aes-128-cbc -K $key -iv $iv
