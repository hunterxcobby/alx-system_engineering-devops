#!/usr/bin/env ruby
# ruby script that matches "htn", "hbtn" and not "hbbtn" or others

puts ARGV[0].scan(/hb?tn/).join
