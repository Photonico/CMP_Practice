# CMP Practice

The practice notes in CMP

## Git LFS

+ Install Git-LFS extension: `git lfs install`

+ Specify the file types to be managed by LFS
  + Create a file named  `.gitattributes` in the root directory of your repository
  + Specify the file types that need to be managed by LFS in this file using either the file extension or file path
    + for zip files: `*.zip filter=lfs diff=lfs merge=lfs -text`
    + for files without filetype: `large-file filter=lfs diff=lfs merge=lfs -text`

+ Track and commit LFS files
  + Track
    + for zip files: `git lfs track "*.zip"`
    + for files without filetype: `git lfs track "large-file"`
    + for the specific file: `git lfs track large-file_directory`
  + Add the LFS list
    + LFS attributes: `git add .gitattributes_directory`
    + LFS files: `git add large_file_directory`
+ Commit the changes: `git commit -m "Commit message"`
  + Push the change: `git push`

+ Pull the repository
  + Downloads the LFS files from the Git LFS server: `git lfs fetch`
  + Checks out these files from the local LFS repository: `git lfs checkout`
