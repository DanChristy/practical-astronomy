default:
	@echo 'Targets:'
	@echo ' build    Build documentation from sources.'
	@echo ' clean    Remove generated documentation.'

view: build
	@firefox html/index.html &

build:
	@doxygen

clean:
	@-rm -rf html/
	@echo 'Finished'
