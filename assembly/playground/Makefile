start: $(filename)
	target/$(filename) '$(data)' $(shifter)

# Create binary file
$(filename): $(filename).o
	@ld target/$(filename).o -o target/$(filename)

# Create object main file
$(filename).o: $(filename).s
	@mkdir -p target/
	@as $(filename).s -o target/$(filename).o

# This one to clean up build files
clean:
	@rm target/$(filename).o target/$(filename)