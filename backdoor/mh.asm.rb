#!/usr/bin/env ruby
# encoding: ascii-8bit
require 'pwn'        # https://github.com/peter50216/ruby-pwntools

@f = File.open('mh.asm', 'wb')
def f;@f;end

# ---------------- vars -------------------
srand(31337)
seq = [1]
(26 * 8 - 1).times do |i|
  s = seq.inject(:+)
  seq << rand(s) + s + 1
end
m = 2 ** ((Math.log2(seq[-1]) + 1).to_i)
r = rand(m) | 1
@beta = seq.map { |c| c * r % m }
p Math.log2(m)
# -----------------------------------------

def write_beta
  @beta.each.with_index do |b, i|
    f.puts "@beta_#{i}:"
    # 270 bits each number
    ar = []
    (270 / 9).times do
      ar << (b & 0x1ff)
      b >>= 9
    end
    f.puts "!data " +  ar.join(',')
  end
end

tpl = <<EOS
@MAIN:
push R28
or R28, ST, ST

re
EOS

write_beta

f.close
