#!/usr/bin/env ruby

require 'json'

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
  puts "Usage: #{__FILE__} [pcap_stream.json or directory]"
  puts ''
  puts "Example: #{__FILE__} pcap_stream.json"
  puts "Example: #{__FILE__} stream/"
  puts "Example: #{__FILE__} stream/5566"
  exit 1
end

def check(fname)
  JSON.parse(IO.binread fname).each do |i|
    id = i['id']
    data = i['data']
    next if data.empty?
    next if id == 0
    data = from9(data.unpack('m')[0])
      .map { |i| i.between?(32, 127) ? i : 0 }
      .map(&:chr)
      .join
    pos = /[0-9a-zA-Z]{26}/ =~ data
    return data[pos, 26] if pos
  end
  return nil
end

found = false
ARGV.each do |fname|
  if File.directory?(fname)
    d = fname.dup
    d << '/' if d[-1] != '/'
    pset = []
    Dir.glob("#{d}**/*")
      .reject { |f| File.directory? f }
      .each do |f|
      if s = check(f)
        puts f,s
        found = true
      end
    end
  elsif File.exists?(fname)
    if s = check(fname)
      found = true
      puts fname,s
    end
  end

end
puts 'Not found' unless found 
