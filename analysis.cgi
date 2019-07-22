#!/usr/bin/ruby
# coding: utf-8
require "cgi"
formData = CGI.new
print "Content-type: text/html\n\n"

fh = open("| touch temp.jpg")
fh = open("| chmod 666 temp.jpg")
open("./temp.jpg","w") do |fh|
fh.write formData.params['imgData'][0].read
end
fh = open("| mv temp.jpg data.jpg")

print <<EOF
<!DOCTYPE html>
<html lang="ja">
 <head>
 <meta charset="utf-8">
 <title>解析結果</title>
 <meta name="description" content="ウェブアプリ「読めルンです」による画像解析結果を表示するページです。">
 
 <!-- CSS -->
 <link rel="stylesheet" href="https://unpkg.com/ress/dist/ress.min.css">
 <link href="<link href="https://fonts.googleapis.com/css?family=Roboto:400,400i&display=swap" rel="stylesheet">
 <link rel="stylesheet" href="css/style.css">
 </head>
 
 <body>
<h1>読め<span>ルン</span>です。</h1>
<div class="wrap">
<div class="img">
<h2>入力画像</h2>
<div>
<img src="./data.jpg">
</div>
</div>
<div class="analysis">
<h2>解析結果</h2>
<div class="analysis-text">
<p>解析結果です。</p>
</div>
</div>
</div>
 </body>
 </html>
EOF
