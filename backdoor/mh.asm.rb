#!/usr/bin/env ruby
# encoding: ascii-8bit
require_relative 'asm_util'

@asm = AsmUtil::Asm.new('mh')
def f;@asm;end
def cat(*a);@asm.cat(*a);end
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
  byte = 270 / 9
  l = f.label('bbbbeta')
  back = f.label('back')
  cat '@get_beta:'

  cat 'or R02, RA, RA'
  cat "b #{l}"
  cat back + ':'
  cat 'or R01, RA, RA'
  cat "mui R00, R00, #{byte}"
  cat 'ad R00, R01, R00'
  cat 'or RA, R02, R02'
  cat 're'

  cat l + ':'
  cat 'car ' + back
  @beta.each.with_index do |b, i|
    cat "@beta_#{i}:"
    # 270 bits each number
    ar = []
    byte.times do
      ar << (b & 0x1ff)
      b >>= 9
    end
    cat "!data " +  ar.join(',')
  end
end

def fix_stack
  cat 'mov R00, 0x2948c00'
  cat 'mov R01, 10'
  cat 'smp R00, R01, RW'
  cat 'mov ST, 0x294b300'
end

def fix_perm
  cat 'mov R00, 0x400'
  cat 'mov R01, 8'
  cat 'smp R00, R01, R'
end

fix_stack
fix_perm # this should be comment out in patch

f.func_call('MAIN') do |ret_l|
  # for i in 0..29
  f.times(30, 'R10') do |i|
    cat "or R00, #{i}, #{i}"
    cat 'car @mh'
  end
  cat 'ht'
end

# summation of beta[*][idx] and write out
f.func_call('mh') do
  regs = (10..28).map{ |c| 'R%02d' % c }
  idx = regs.shift
  cat "or #{idx}, R00, R00"

  sum = regs.shift
  cat "xr #{sum}, #{sum}, #{sum}"
  do_sum = f.label('do_sum')
  f.times(26, regs.shift) do |i|
    cat "or R00, #{i}, #{i}"
    cat "car @FETCH_FLAG"
    flag = regs.shift
    cat "or #{flag}, R00, R00"
    # j = 0..7 bit test and use beta_{i * 8 + j}
    f.times(8, regs.shift) do |j, continue|
      # if flag & j == 1
      cat "sr R02, #{flag}, #{j}"
      cat "ani R02, R02, 1"
      cat 'cmi R02, 1'
      cat "be #{do_sum}"
      cat "b #{continue}"
      cat do_sum + ':'
      # sum += beta[i * 8 + j][idx]
      cat "mui R01, #{i}, 8"
      cat "ad R01, R01, #{j}"
      cat 'or R00, R01, R01'
      cat 'car @get_beta'
      cat "ad R00, R00, #{idx}" # beta[i * 8 + j][idx]
      cat 'lds R00, [R00 + 0, 1]'
      cat "ad #{sum}, #{sum}, R00"
    end
  end

  cat "stt #{sum}, [ST]"
  cat 'or R00, ST, ST'
  cat 'mov R01, 3'
  cat 'car @SYS_WRITE'
end

f.sys_write

f.func_call('FETCH_FLAG', 0) do |_ret_l|
  cat "mov R01, 0x4010000"
  cat "ad R01, R01, R00"
  cat "lds R00, [R01 + 0, 1]"
end

write_beta

f.close
