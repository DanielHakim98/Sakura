.PHONY: build, clean 

TARGET_DIR := ./build

build: ${SOURCE}.cpp
	mkdir -p ${TARGET_DIR}
	clang++ -std=c++11 -o ${TARGET_DIR}/${SOURCE} ${SOURCE}.cpp

clean:
	rm -rf build
	
