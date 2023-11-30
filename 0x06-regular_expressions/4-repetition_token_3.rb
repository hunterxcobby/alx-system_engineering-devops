#!/usr/bin/env ruby
# ruby script that matches "hbn, hbtn, hbtttttn" not "hbon"

puts ARGV[0].scan(/hbt*n/).join
