

# Batch Processor

## Overview

This project implements a `BatchProcessor` class that processes a list of records into batches based on specified size and count limits. The processor ensures that each batch adheres to the following constraints:
- Maximum size of each record is 1 MB.
- Maximum size of each batch is 5 MB.
- Maximum number of records per batch is 500.

## Files

- `BatchProcessor.py`: The main script for processing records.
- `requirements.txt`: List of required Python packages.
- `Dockerfile`: Docker configuration file.
- `test_BatchProcessor.py`: Unit tests for the `BatchProcessor`.

## BatchProcessor Class

The `BatchProcessor` class (`BatchProcessor.py`) contains the following methods:
-  `__init__(self, max_record_size=1048576, max_batch_size=5242880, max_records_per_batch=500)`
- Initializes the processor with configurable limits for record size, batch size, and records per batch.
-  `create_batches(self, records: List[str]) -> List[List[str]]`
- Processes a list of records into batches based on the configured limits.
- Returns a list of batches, where each batch is a list of records.

## Example Usage

The `BatchProcessor` class can be used as follows:

```python
from BatchProcessor import BatchProcessor

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process records into batches.")
    parser.add_argument('records', metavar='R', type=str, nargs='+', help='Records to be processed')

    args = parser.parse_args()
    input_records = args.records

    batch_processor = BatchProcessor()
    output_batches = batch_processor.create_batches(input_records)

    for i, batch in enumerate(output_batches):
        print(f"Processed Batch {i+1}: {batch}")
```
## Running with Docker

### Prerequisites
Docker installed on your system.

## Building the Docker Image
To build the Docker image that includes the BatchProcessor class and the associated tests:

- Navigate to the project directory containing Dockerfile and requirements.txt.

- Run the following command to build the Docker image:

```
docker build -t batch-processor .
```
## Run the Docker container with direct input:

```
docker run batch-processor --input record1 record2 record3 record4
```

## Run the Docker container with input files:

```
docker run -v $(pwd):/app batch-processor --files input1.txt input2.txt
```
## Example with Input from the Command Line:
```
docker run batch-processor --input record1 record2 record3 record4
```
## Example with Input from Files:

### Create example input files
```
echo -e "record1\nrecord2\nrecord3" > input1.txt
echo -e "record4\nrecord5\nrecord6" > input2.txt
```

### Run the Docker container with input files
```
docker run -v $(pwd):/app batch-processor --files input1.txt input2.txt
```

## Test Cases
The project includes test cases (test/test_BatchProcessor.py) to validate the functionality of the BatchProcessor class. These test cases cover scenarios such as:

- Processing records within the maximum batch size and record count.
- Handling records that exceed the maximum batch size.
- Managing batches with a large number of records.
- Discarding records larger than the specified maximum record size.
- Handling empty input records.

## Running Tests Locally
You can also run the tests locally without Docker by installing pytest and running:

```
pytest
```
Ensure all dependencies listed in requirements.txt are installed before running the tests.