filename := pair
output_dir := dist


run: $(filename).js
	@node $(output_dir)/$(filename).js
	@rm -r $(output_dir)/

$(filename).js: $(filename).ts tsconfig.json
	@tsc

clean:
	@rm -r $(output_dir)/