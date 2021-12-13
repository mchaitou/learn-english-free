import subprocess
import glob

flac_dir = 'fragments'


for infile in sorted(glob.glob(f'{flac_dir}/*.flac')):
  outfile = infile[:-4] + 'mp3'
  subprocess.run(["ffmpeg", "-i", infile, outfile])
