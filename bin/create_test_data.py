import sys
import os.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import glob
import json
from app import app
from app.util.vinspect import extract_json, get_frame
from pprint import pprint


print "Writing data to", sys.argv[1]
files = glob.glob(app.config['VIDEOS_DIRECTORY'] + '/*.*')
print "Processing:"
results = []
for idx, file in enumerate(files):
    print " ->", file
    base = os.path.basename(file)
    extracted = extract_json(file)
    info = json.loads(extracted)
    info['filename'] = file
    info['basename'] = base
    info['title'] = base.split('.')[0].upper().replace('_', ' ')
    info['frame'] = get_frame(file)
    info['static_frame'] = '/'.join(('/media', 'frames', os.path.basename(info['frame'])))
    info['text'] = "Lorem ipsum dolor sit amet, ex mea nostrud assentior, ei mea vide menandri, vim ad incorrupte referrentur interpretaris. Pri oblique persius equidem in. Quis menandri eam cu. Sed suas aliquip vivendo no. An modus accusam vel."
    results.append(info)
with open(sys.argv[1], 'w') as outfile:
    json.dump(results, outfile, indent=4)
