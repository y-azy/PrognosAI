from global_logger import global_logger

def test_logger():
    # Test different log levels
    global_logger.info("Test info message")
    global_logger.error("Test error message")
    global_logger.debug("Test debug message")
    
    # Test with extra data
    global_logger.info("Test with data", extra={"data": "test_value"})

    print("Check the log file and console output for messages")

if __name__ == "__main__":
    test_logger()
