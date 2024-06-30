from typing import List
import argparse
class BatchProcessor:
    def __init__(self, max_record_size: int = 1 * 1024 * 1024, max_batch_size: int = 5 * 1024 * 1024, max_records_per_batch: int = 500):
        self.max_record_size = max_record_size
        self.max_batch_size = max_batch_size
        self.max_records_per_batch = max_records_per_batch

    def create_batches(self, records: List[str]) -> List[List[str]]:
        """
        Process batches of records based on size and record count limits.

        Args:
            records (list): A list of records to be processed.

        Returns:
            list: A list of batches, where each batch is a list of records.
        """
        batches = []
        current_batch = []
        current_batch_size = 0

        for record in records:
            record_size = len(record.encode('utf-8'))

            if record_size > self.max_record_size:
                # Discard records larger than the max record size
                continue

            # Check if adding the current record will exceed the maximum batch size or the maximum number of records per batch
            if (current_batch_size + record_size > self.max_batch_size) or (len(current_batch) >= self.max_records_per_batch):
                # Finish the current batch and start a new one
                batches.append(current_batch)
                current_batch = []
                current_batch_size = 0

            # Add the current record to the current batch
            current_batch.append(record)
            current_batch_size += record_size

        # Check if there are any remaining records in the current batch
        if current_batch:
            batches.append(current_batch)

        return batches

def read_records_from_files(file_paths: List[str]) -> List[str]:
    records = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            records.extend(file.read().splitlines())
    return records

def read_records_from_input(inputs: List[str]) -> List[str]:
    return inputs

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process batches of records.")
    parser.add_argument('-f', '--files', metavar='F', type=str, nargs='*', help='input files containing records')
    parser.add_argument('-i', '--input', metavar='I', type=str, nargs='*', help='input records provided directly')
    args = parser.parse_args()

    if args.files:
        input_records = read_records_from_files(args.files)
    elif args.input:
        input_records = read_records_from_input(args.input)
    else:
        raise ValueError("Either --files or --input must be provided.")

    batch_processor = BatchProcessor()
    output_batches = batch_processor.create_batches(input_records)
    for i, batch in enumerate(output_batches):
        print(f"Processed Batch {i+1}: {batch}")
