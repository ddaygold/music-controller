#!/usr/bin/env python
import alsaaudio
output = '<!DOCTYPE html\
PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\
<html>\
	<head>\
		<title>Muted</title>\
	</head>\
	<body>\
            <p>Muted</p>\
	</body>\
</html>' 
m = alsaaudio.Mixer(control='Master',id=0,cardindex=0)
m.setmute(1)
print(output)
