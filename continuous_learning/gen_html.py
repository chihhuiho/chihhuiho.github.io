import os

f=open("index.html", "w")
f.write("<!doctype html>\n\
<html lang=\"en\">\n\
<head>\n\
<meta charset=\"utf-8\">\n\
<meta http-equiv=\"x-ua-compatible\" content=\"ie=edge\">\n\
<title>Continuous Learning</title>\n\
<link rel=\"stylesheet\" href=\"static/css/normalize.css\">\n\
<link rel=\"stylesheet\" href=\"static/themes/classic/galleria.classic.css\">\n\
<link rel=\"stylesheet\" href=\"static/css/style.css\">\n\
</head>\n\
<body>\n\
<div class=\"container\">\n\
<header>\n")
for cls in os.listdir("gif"):
    f.write("<h1>" + str(cls) + "</h1>")
    for gif in os.listdir("gif/" + str(cls)):
        f.write("<h1></h1><img src=\"gif/" + str(cls) + "/" + str(gif) + "\"")
    f.write("<p> </p>")
f.write("<p> </p>\
</header>\
</div>\
</body>\
</html>")
f.close()
