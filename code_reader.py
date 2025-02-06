import glob
import os
import shutil
import git  # You'll need to run: pip install gitpython

class CodeReader:
    def __init__(self):
        self.temp_dir = "temp_repo"

    def read_from_directory(self, dir_path):
        python_files = glob.glob(f"{dir_path}/**/*.py", recursive=True)
        return python_files

    def read_from_github(self, github_url):
        import git
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
        git.Repo.clone_from(github_url, self.temp_dir)
        return self.read_from_directory(self.temp_dir)
