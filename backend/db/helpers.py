from pathlib import Path

def fetch_files(dir_name="docs", sub_dir_name=None, extension_type=".pdf"):
    """
    Wrapper function to fetch files from a directory.

    Args:
        dir_name: the name of the directory to search in.
        sub_dir_name: the name of a subdirectory to search in (optional).
        extension_type: the file extension to search for (default is ".pdf").

    Returns:
        A list of Path objects representing the files found.
    """
    global FILES
    FILES = []
    PDF_DIR = (Path(__file__).resolve().parent).joinpath(dir_name)
    if sub_dir_name:
        PDF_DIR = PDF_DIR.joinpath(sub_dir_name)
    fetch_files_from_directory(PDF_DIR, extension_type)
    return FILES

def fetch_files_from_directory(dir_path, extension):
    """
    Recursively fetch files from a directory.

    Args:
        dir_path: a Path object representing the directory to search in.
        extension: the file extension to search for.

    Returns:
        None.
    """
    files = [f for f in dir_path.iterdir() if f.is_file() and f.suffix == extension]
    FILES.extend(files)
    sub_dirs = [d for d in dir_path.iterdir() if d.is_dir()]
    if sub_dirs:
        [fetch_files_from_directory(d, extension) for d in sub_dirs]
