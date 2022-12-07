TARGET_DIR = ./day$(DAY)

run:
	python3 $(TARGET_DIR)/solution.py < $(TARGET_DIR)/input.txt

new:
	cp -r day/ day$(DAY)/