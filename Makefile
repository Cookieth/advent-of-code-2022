TARGET_DIR = ./day$(DAY)

run python:
	python3 $(TARGET_DIR)/python/solution.py < $(TARGET_DIR)/input.txt

run cpp:
	g++ $(TARGET_DIR)/cpp/solution.cpp -o solution.out
	./solution.out < $(TARGET_DIR)/input.txt

new:
	cp -r day/ day$(DAY)/