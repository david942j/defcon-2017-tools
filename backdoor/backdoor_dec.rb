#!/usr/bin/env ruby
# encoding: ascii-8bit
require 'base64'
byte = 30


if ARGV.empty?
  puts "backdoor_dec <base64>"
  exit 1
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

def endian(s)
  s.map! do |ar|
    (ar[1] << 18) + (ar[2] << 9) + ar[0]
  end
end

s = ARGV.join.split.join
s = Base64.decode64(s)[0, byte * 4].scan(/..../m).map {|c| from9(c).reverse }.reverse
exit if s.size != byte
endian(s)
ans = 0
# p s
s.each do |c|
  ans = ans * 512 + c
end
# p ans
srand(31337)
seq = [1]
(26 * 8 - 1).times do |i|
  s = seq.inject(:+)
  seq << rand(s) + s + 1
end
m = 2 ** ((Math.log2(seq[-1]) + 1).to_i)
r = rand(m) | 1

rr = 398646047252318044030398963993230676106658905944448669034282264967397283070073797
val = rr * ans % m
ap = ''
seq.reverse.each do |c|
  if val >= c
    ap << '1'
    val -= c
  else
    ap << '0'
  end
end
puts ap.scan(/.{8}/).map{|c|c.to_i(2).chr}.join.reverse
