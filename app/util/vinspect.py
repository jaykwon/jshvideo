from hachoir_core.error import HachoirError
from hachoir_core.cmd_line import unicodeFilename
from hachoir_metadata import extractMetadata
from hachoir_parser import createParser
from ffvideo import VideoStream
import json
import datetime
import os.path
import sys
sys.path.append(os.path.abspath(os.path.dirname('..')))
import config


def _create_parser(filename):
    filename, realname = unicodeFilename(filename), filename
    parser = createParser(filename, realname)
    return parser

def break_time(t):
    headers = ['d', 'h', 'm', 's', 'ms']
    values = [t.days, t.seconds / 3600, t.seconds / 60, t.seconds, t.microseconds]
    return dict(zip(headers, values))

def pretty_time(bt):
    strung = {k: str(v).zfill(2) for (k, v) in bt.iteritems()}
    pt = '{0}:{1}:{2}.{3}'.format(strung['h'], strung['m'], strung['s'], strung['ms'][:3])
    return pt

def extract(filename):
    parser = _create_parser(filename)
    try:
        metadata = extractMetadata(parser)
    except HachoirError, e:
        print "Metadata error:", e
    return metadata

def make_hm_dict(metadata):
    result = {}
    keys = metadata._Metadata__data.keys()
    for key in keys:
        try:
            text = metadata.getText(key)
            raw = metadata.get(key)
        except ValueError, e:
            continue
        #datetime.datetime objects won't serialize correctly
        if type(raw) is datetime.datetime:
            raw = None
        result[key] = {
            'raw': raw,
            'text': text
        }
    return result

def extract_dict(filename):
    metadata = extract(filename)
    return make_hm_dict(metadata)

def extract_json(filename, **kwargs):
    d = extract_dict(filename)
    try:
        bt = break_time(d['duration']['raw'])
    except TypeError, e:
        bt = None
    d['duration']['alt'] = bt
    d['duration']['raw'] = str(d['duration']['raw'])
    return json.dumps(d, **kwargs)

def get_frame(filename, sec=3):
    basename = os.path.basename(filename)
    sans_ext = basename.split('.')[0]
    vs = VideoStream(filename)
    frame = vs.get_frame_at_sec(sec)
    frame_location = os.path.join(config.FRAMES_DIRECTORY, sans_ext + '.png')
    frame.image().save(frame_location)
    return frame_location

if __name__ == '__main__':
    video_path = 'app/static/media/videos/flame.avi'
    metadata = extract(video_path)
    print metadata
    print break_time(metadata.get('duration'))
    print extract_json(video_path, indent=4)
