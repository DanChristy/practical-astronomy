default:
	@echo 'Targets:'
	@echo '  all'
	@echo '  test-easter'
	@echo '  test-day-number'
	@echo '  test-julian'
	@echo '  test-time'
	@echo '  test-coordinate'

all: test-easter test-day-number test-julian test-time test-coordinate

test-easter:
	@./test-date-of-easter.py -v

test-day-number:
	@./test-day-number.py

test-julian:
	@./test-julian.py

test-time:
	@./test-time.py

test-coordinate:
	@./test-coordinate.py
