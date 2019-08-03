#!/bin/bash

echo "Content-type: text/html"
echo ""

echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<title>Update</title>'
echo '</head>'
echo '<body>'
echo "Pull:"
echo `git pull` 
echo '</body>'
echo '</html>'
exit 0
