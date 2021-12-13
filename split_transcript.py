import glob
import os, os.path
text_file = 'transcript.txt'
flac_dir = 'fragments'
out_dir = 'text_dir'
MAX_WORDS = 10 # max words per line

# Read the transcript file
with open(text_file, 'r') as f:
  content = f.readlines()

# print(content[0][1:-2])

clean_content = [c[1:-2] for c in content ]

# print(clean_content[0])

# Create a separate text file for each sentence in the transcript
# Remove a flac file less than 75 KB of size
# Remove the corresponding text file
count = 0
for infile in sorted(glob.glob(f'{flac_dir}/*.flac')):
  sentence_file = out_dir + '\\' + infile.split('\\')[-1][:-4]+'txt'
  with open(sentence_file, 'w') as f:
    if len(clean_content[count].split()) > 2  * MAX_WORDS:
      f.writelines(" ".join(clean_content[count].split()[:MAX_WORDS]))
      f.writelines("\n")
      f.writelines(" ".join(clean_content[count].split()[MAX_WORDS: 2 * MAX_WORDS]))
      f.writelines("\n")
      f.writelines(" ".join(clean_content[count].split()[2 * MAX_WORDS:]))
    else:
      if len(clean_content[count].split()) > MAX_WORDS:
        f.writelines(" ".join(clean_content[count].split()[:MAX_WORDS]))
        f.writelines("\n")
        f.writelines(" ".join(clean_content[count].split()[MAX_WORDS:]))
      else:
        f.writelines(clean_content[count])
    count += 1

for infile in sorted(glob.glob(f'{flac_dir}/*.flac')):
  sentence_file = out_dir + '\\' + infile.split('\\')[-1][:-4]+'txt'
  try:
      if os.path.getsize(infile) < 75 * 1024:
        os.remove(infile)
        os.remove(sentence_file)
  except WindowsError:
    print("Error" + infile)

