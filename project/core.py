import logging
logging.basicConfig(level=logging.INFO)

def process(data):
    logging.info(f"Processing {data}")
    return [item * 3 for item in data if isinstance(item, int)]
# Main branch change
