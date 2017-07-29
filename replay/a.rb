#!/usr/bin/env ruby

require 'json'
require 'set'

def from9(s)
  s
    .unpack('B*')[0]
    .chars
    .each_slice(9)
    .select{|x| x.size == 9}
    .map(&:join)
    .map{|x| x.to_i(2)}
end

if ARGV.empty?
  puts "Usage: #{__FILE__} pcap_stream.json"
  exit 1
end



Dir.glob("#{ARGV[0]}/*").each do |f|
  puts f
  puts `./viewer.rb #{f}`
  puts '==============='
  $stdin.gets
end
