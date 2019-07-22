#!/usr/bin/ruby
require "cgi"
formData = CGI.new
print "Content-type: text/html\n\n"
print "<html><head><title>Sample</title></head><body>"
print "Now Uploading...<br>"
fh = open("| touch temp.jpg")
fh = open("| chmod 666 temp.jpg")
open("./temp.jpg","w") do |fh|
  fh.binmode
  fh.write formData['file'][0].read
end
fh = open("| mv temp.jpg data.jpg")
print "Upload End"
print "<img src='data.jpg'></body></html>"
