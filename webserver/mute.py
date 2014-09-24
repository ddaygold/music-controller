import alsaaudio
output = '<!DOCTYPE html\
PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\
<html>\
<head>\
    <title>MUTE</title>\
    <style text="text/javascript">\
    .full { color: white; background-color: red; width: 100%; height: 100%; text-align: center; font-size: 1500%}\
    </style>\
</head>\
<body>\
<div class="full">\
MUTED\
</div>\
</html>\
'
m = alsaaudio.Mixer(control='Master',id=0,cardindex=0)
m.setmute(1)
print(output)
