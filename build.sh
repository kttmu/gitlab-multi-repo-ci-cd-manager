#!/bin/bash

set -e

# C++プロジェクトのビルドを実行
mkdir -p build
cd build
cmake ..
make -j$(nproc)

if [ $? -eq 0 ]; then
  echo "Build succeeded."
else
  echo "Build failed." >&2
  exit 1
fi
