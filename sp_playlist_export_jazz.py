import subprocess, os, sys, argparse

l_Parser = argparse.ArgumentParser()
l_Parser.add_argument('passwd')
l_Args = l_Parser.parse_args()

os.chdir(os.path.abspath(os.path.dirname(__file__)))

l_PlaylistList = ['Funk', 'Rythm & Blues', 'Blues', 'Soul', 'Groove', 'Jazz FM']

for l_Playlist in l_PlaylistList:
    
    l_DirPath = os.path.join('/run/media/benweet/F84E-1690', l_Playlist)
    if not os.path.isdir(l_DirPath):
        os.mkdir(l_DirPath)
        
    while(True):
        l_Result = subprocess.call(['./sp_playlist_export', 'Benweet', l_Args.passwd, '/run/media/benweet/F84E-1690', l_Playlist])
        if l_Result != 1:
            break
    
    if l_Result:
        print("ERROR:", l_Result)
        sys.exit(l_Result)
