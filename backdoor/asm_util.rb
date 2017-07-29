class Integer
  def hex
    if self < 0
      '-0x%x' % (-self)
    else
      '0x%x' % self
    end
  end
end

module AsmUtil
  class Asm
    attr_reader :file
    def initialize(filename)
      @file = File.open(filename + '.asm', 'wb')
      @label_num = 0
    end

    def puts(str)
      @file.puts str
    end

    def cat(s)
      if s.start_with?('@')
        puts(s)
      else
        puts('  ' + s)
      end
    end

    # @return @{name}_x
    def label(name)
      @label_num += 1
      "@#{name}_#{@label_num}"
    end

    def times(n, reg)
      fail if reg == 'R09'
      # n.times do
      cat "xr #{reg}, #{reg}, #{reg}" # i = 0
      l = label('LOOP')
      end_loop = label('END_LOOP')
      cat l + ':'
      cat "cmi #{reg}, #{n}"
      cat "be #{end_loop}" # break if i == n

      cont = label('continue')
      yield(reg, cont)
      cat cont + ':'

      cat "adi #{reg}, #{reg}, 1" # i++
      cat 'b ' + l
      cat end_loop + ':'
    end

    def func_call(name, stk_size = 0x7f)
      cat "@#{name}:"
      cat 'sttd        R09, [ST + 0, 22]'
      cat 'or.         R09, ST, ST'
      if stk_size <= 0x7f
        cat "sbi ST, ST, #{stk_size.hex}"
      else
        cat "mov R08, #{stk_size.hex}"
        cat "sb ST, ST, R08"
      end
      ret_l = label('RET')
      # do NOT use R09
      yield(ret_l)
      cat ret_l + ':'

      if stk_size <= 0x7f
        cat "adi ST, ST, #{stk_size.hex}"
      else
        cat "mov R08, #{stk_size.hex}"
        cat "ad ST, ST, R08"
      end

      cat 'ldt         R09, [R09 + 0, 22]'
      cat 're'
    end

    def sys_write
      cat "@SYS_WRITE:"
      cat 'or          R04, R01, R01'
      cat 'mov         R02, 0x5010000'
      cat 'ldt         R03, [R02 + 0x2000, 1]'
      cat 'cmi         R03, 0'
      cat 'be          8'
      cat 'wt'
      cat 'b           -0xE'
      cat 'ml          R03, 0x1FFF'
      cat 'cm          R01, R03'
      cat 'bg          0x11'
      cat 'dmt         R02, R00, R01'
      cat 'stt         R01, [R02 + 0x2000, 1]'
      cat 'or          R00, R04, R04'
      cat 're'
      cat 'dmt         R02, R00, R03'
      cat 'ad          R00, R00, R03'
      cat 'stt         R03, [R02 + 0x2000, 1]'
      cat 'sb          R01, R01, R03'
      cat 'b           -0x36'
    end

    def close
      @file.close
    end
  end
end
