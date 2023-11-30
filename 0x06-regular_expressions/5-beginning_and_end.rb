#!/usr/bin/env ruby
# ruby script that matches words/strings that start with `h` and end with `n`.
# regardless of whatever is in the middle(single character).

puts ARGV[0].scan(/h.n/).join
