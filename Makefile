TARGET_DIR = ./day$(DAY)

run_cpp:
	g++ $(TARGET_DIR)/cpp/solution.cpp -o $(TARGET_DIR)/cpp/solution.out
	$(TARGET_DIR)/cpp/solution.out < $(TARGET_DIR)/input.txt

run_python:
	python3 $(TARGET_DIR)/python/solution.py < $(TARGET_DIR)/input.txt

new:
	cp -r day/ day$(DAY)/