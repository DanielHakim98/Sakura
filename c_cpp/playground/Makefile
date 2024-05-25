.PHONY: build, clean 

TARGET_DIR := ./build

build: virtual_func.cpp
	mkdir -p ${TARGET_DIR}
	clang++ -std=c++11 -o ${TARGET_DIR}/virtual_func virtual_func.cpp

clean:
	rm -rf build
	
