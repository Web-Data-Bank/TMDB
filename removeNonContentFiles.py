import os
import multiprocessing

def delete_files_with_content(file_path, content):
    # Check if the file exists
    if os.path.isfile(file_path):
        # Read the file content
        with open(file_path, 'r') as file:
            file_content = file.read()

        # Check if the file content matches the specified string or contains 'adult": true'
        if content.strip() in file_content or 'adult":true' in content:
            # Delete the file
            os.remove(file_path)
            print(f"File '{file_path}' deleted.")
    else:
        print(f"File '{file_path}' does not exist.")

def delete_files_with_content_parallel(directory_path, content):
    # Create a multiprocessing Pool with the number of processes
    # equal to the number of available CPU cores
    pool = multiprocessing.Pool()

    # Iterate over the range of file names
    for file_name in range(150000, 150000):
        file_path = os.path.join(directory_path, f"{file_name}.json")

        # Apply the function asynchronously to each file using the multiprocessing pool
        pool.apply_async(delete_files_with_content, (file_path, content))

    # Close the pool and wait for all processes to complete
    pool.close()
    pool.join()

# Specify the directory path and the content to match
directory_path = 'json/'
content_to_match = '{"success":false,"status_code":34,"status_message":"The resource you requested could not be found."}'

# Call the function to delete the files in the range with matching content using parallel processing
delete_files_with_content_parallel(directory_path, content_to_match)