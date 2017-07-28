#!/usr/bin/env ruby

$stdout.sync = true

require 'shellwords'

def to9(xs)
  s = xs.map{|x| '%09b' % x}.join
  s += '0' * (8 - s.size % 8) if s.size % 8 != 0
  [s].pack('B*')
end

def from9(s)
  s
    .unpack('B*')[0]
    .chars
    .each_slice(9)
    .select{|x| x.size == 9}
    .map(&:join)
    .map{|x| x.to_i(2)}
end

def test
  100.times do
    xs = rand(1..100).times.map{rand(512)}
    fail unless from9(to9(xs)) == xs
  end
end

if ARGV.empty?
  puts "Usage: #{__FILE__} [COMMANDS...]"
  exit 1
end

trap(:INT) do
  $stdout.puts "\e[1;31m[SIGINT]\e[0m"
  exit
end

cmd = ARGV.shelljoin
prog = IO.popen(cmd, 'r+')

begin
  loop do
    rs, _, _ = IO.select([prog, $stdin])
    if rs.include?(prog)
      s = prog.readpartial(4095) # 4095 % 9 == 0
      xs = from9(s)
      if xs.max >= 256
        $stdout.puts "\e[1;34msome bytes >= 256: #{xs.inspect}\e[0m"
      end
      $stdout.write xs.pack('C*')
    end
    if rs.include?($stdin)
      s = $stdin.readpartial(4096)
      prog.write to9(s.bytes)
    end
  end
rescue EOFError
  $stdout.puts "\e[1;31m[EOF]\e[0m"
end
