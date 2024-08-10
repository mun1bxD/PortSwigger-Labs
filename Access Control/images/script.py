import os

def rename_png_files(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)

    # Filter out only the .png files
    png_files = [f for f in files if f.endswith('.png')]

    # Sort the files (optional, if you want a specific order)
    png_files.sort()

    # Loop through the .png files and rename them
    for index, file_name in enumerate(png_files):
        # Define the new file name
        new_name = f"image{index + 1}.png"
        
        # Create full path for the old and new file names
        old_file = os.path.join(folder_path, file_name)
        new_file = os.path.join(folder_path, new_name)
        
        # Rename the file
        os.rename(old_file, new_file)
        print(f'Renamed: {old_file} to {new_file}')

# Specify the path to your folder containing the .png files
folder_path = 'C:\\Users\\hp\\Desktop\\images'
rename_png_files(folder_path)
