#!/usr/bin/env ruby
# ruby script that outputs: [SENDER],[RECEIVER],[FLAGS]
# combined :- puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")

from = ARGV[0].scan(/from:(.*?)\]/)
to = ARGV[0].scan(/to:(.*?)\]/)
flags = ARGV[0].scan(/flags:(.*?)\]/)
puts [from, to, flags].join(",")
