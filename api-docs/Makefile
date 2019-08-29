default:
	@echo 'Targets:'
	@echo ' build    Build documentation from sources.'

view: build
	@firefox html/index.html &

build:
	@-rm -rf ../docs/
	@doxygen
