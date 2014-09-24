#!/usr/bin/env python
import alsaaudio
output = '<!DOCTYPE html\n\
PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n\
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n\
<html>\n\
	<head>\n\
		<title>Muted</title>\n\
	</head>\n\
	<body>\n\
            <p>Muted</p>\n\
	</body>\n\
</html>' 
m = alsaaudio.Mixer(control='Master',id=0,cardindex=0)
m.setmute(1)
print(output)
