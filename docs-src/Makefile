default:
	@echo 'Targets:'
	@echo ' view     View documentation in Firefox.'
	@echo ' build    Build documentation from sources.'

view: build
	@firefox ../docs/index.html &

build:
	@-rm -rf ../docs/
	@doxygen
