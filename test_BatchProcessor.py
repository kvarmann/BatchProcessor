import pytest
from BatchProcessor import BatchProcessor

def test_create_batches():
    # Create an instance of RecordBatcher
    batcher = BatchProcessor()

    # Test case 1: Records fit within the maximum batch size and maximum number of records per batch
    input_records = ["record1", "record2", "record3"]
    expected_output = [["record1", "record2", "record3"]]
    assert batcher.create_batches(input_records) == expected_output

def test_create_batches_with_large_records():
    # Create an instance of RecordBatcher
    batcher = BatchProcessor()

    # Test case 2: Records exceed the maximum batch size (simulate by creating large records)
    record_size_1mb = "a" * (1 * 1024 * 1024)
    input_records = [record_size_1mb, record_size_1mb, record_size_1mb, record_size_1mb, record_size_1mb, "record6"]
    expected_output = [
        [record_size_1mb, record_size_1mb, record_size_1mb, record_size_1mb, record_size_1mb],
        ["record6"]
    ]
    assert batcher.create_batches(input_records) == expected_output

def test_create_batches_with_many_records():
    # Create an instance of RecordBatcher
    batcher = BatchProcessor()

    # Test case 3: Records exceed the maximum number of records per batch (simulate 501 small records)
    input_records = ["record"] * 501
    expected_output = [ ["record"] * 500, ["record"] ]
    assert batcher.create_batches(input_records) == expected_output

def test_create_batches_with_discarded_records():
    # Create an instance of RecordBatcher
    batcher = BatchProcessor()

    # Test case 5: Records larger than the max record size are discarded
    record_size_1mb = "a" * (1 * 1024 * 1024)
    record_size_2mb = "b" * (2 * 1024 * 1024)
    input_records = [record_size_1mb, record_size_2mb, "record"]
    expected_output = [[record_size_1mb, "record"]]
    assert batcher.create_batches(input_records) == expected_output

def test_create_batches_with_empty_records():
    # Create an instance of RecordBatcher
    batcher = BatchProcessor()

    # Test case 6: Empty input records
    input_records = []
    expected_output = []
    assert batcher.create_batches(input_records) == expected_output

if __name__ == "__main__":
    # Run the tests using pytest
    pytest.main()
