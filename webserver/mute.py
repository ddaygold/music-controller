import alsaaudio
output = '<!DOCTYPE html>\
<html>\
<head>\
    <title>MUTE</title>\
    <style>\
    .full { color: white; background-color: red; width: 100%; height: 100%; text-align: center; font-size: 1500%}\
    </style>\
</head>\
<body>\
<div class="full">\
MUTED\
</div>\
</body>\
</html>\
'
m = alsaaudio.Mixer(control='Master',id=0,cardindex=0)
m.setmute(1)
print(output)
