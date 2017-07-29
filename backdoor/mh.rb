#!/usr/bin/env ruby
# encoding: ascii-8bit

srand(31337)
seq = [1]
(26 * 8 - 1).times do |i|
  s = seq.inject(:+)
  seq << rand(s) + s + 1
end
m = 2 ** ((Math.log2(seq[-1]) + 1).to_i)
r = rand(m) | 1
beta = seq.map { |c| c * r % m }
flag = 'AbcDEfghIJKlmNopQrstuVexyz'

a = flag.bytes.map { |c| '%08b' % c }.join.chars
sum = 0
a.each.with_index do |v, i|
  sum += beta[i] if v == '1'
end

p sum

p r
p m

rr = 398646047252318044030398963993230676106658905944448669034282264967397283070073797
val = rr * sum % m
ap = ''
seq.reverse.each do |c|
  if val >= c
    ap << '1'
    val -= c
  else
    ap << '0'
  end
end
p ap
p ap.reverse.scan(/.{8}/).map{|c|c.to_i(2).chr}.join
