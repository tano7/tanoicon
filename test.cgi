#!/usr/bin/ruby
# coding: utf-8
require 'cgi'

print "Content-type: text/html\n\n"

cgi = CGI.new

value = cgi.params['file'][0]
puts "file name : " <<  value.original_filename  << "<br/>" # ファイル名
puts value.read 
