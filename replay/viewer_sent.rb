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
  puts "Example: #{__FILE__} stream/5566"
  exit 1
end

BPL = 16
def view(fname, stop)
  puts fname
  tot = 0
  JSON.parse(IO.binread fname).each do |i|
    id = i['id']
    data = i['data']
    next if data.empty?
    next if id == 1
    data = from9(data.unpack('m')[0])
    tot += data.size
    if tot >= 10000 and stop
      puts "Stripted, file #{fname} is more than 10000 bytes."
      puts "Use `#{__FILE__} #{fname}` to view full information."
      return
    end
    if id == 0
      $stdout.puts "\e[1;33mSent 0x" + data.size.to_s(16) + ' bytes: '
    else
      $stdout.puts "\e[0;38mReceived 0x" + data.size.to_s(16) + ' bytes: '
    end
    data
      .each_slice(BPL)
      .each_with_index do |arr, i|
      $stdout.write('  %07x:' % (BPL * i))
      arr.each do |c|
        $stdout.write(' %03x' % c)
      end
      $stdout.write(' ' * (17 - arr.size) * 4)
      $stdout.write '|'
      arr.each { |c| $stdout.write(c.between?(32, 127) ? c.chr : ".") }
      $stdout.puts '|'
    end
    $stdout.puts "\e[0m"
  end
end

ARGV.each do |fname|
  if File.directory?(fname)
    d = fname.dup
    d << '/' if d[-1] != '/'
    Dir.glob("#{d}*").each do |f|
      next if File.directory? f
      view(f,true)
      puts '==============='
      $stdout.puts 'Press Enter to continue..'
      $stdin.gets
    end
  elsif File.exists?(fname)
    view(fname,false)
    puts '==============='
    $stdout.puts 'Press Enter to continue..'
    $stdin.gets
  else
    puts "#{fname} not exists"
  end
end
nd
