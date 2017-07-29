from idaapi import *
import os
import sys
import re
from clemency_inst import inst_json

########################################
# Decoder Function
########################################
def is_bit_string(strg, search=re.compile(r'[^01]').search):
    return not bool(search(strg))

def SIGNEXT(x, b):
  m = 1 << (b - 1)
  x = x & ((1 << b) - 1)
  return (x ^ m) - m

def fetch(code, n):
    byte1 = (code >> (54 - 9 * 1)) & 0x1ff
    byte2 = (code >> (54 - 9 * 2)) & 0x1ff
    byte3 = (code >> (54 - 9 * 3)) & 0x1ff
    byte4 = (code >> (54 - 9 * 4)) & 0x1ff
    byte5 = (code >> (54 - 9 * 5)) & 0x1ff
    byte6 = (code >> (54 - 9 * 6)) & 0x1ff
    if n == 18:
        return (byte2 << 9) + byte1
    elif n == 27:
        return (byte2 << 18) + (byte1 << 9) + byte3
    elif n == 36:
        return (byte2 << 27) + (byte1 << 18) + (byte3 << 9) + byte4
    elif n == 54:
        return (byte2 << 45) + (byte1 << 36) + (byte3 << 27) + (byte5 << 18) + (byte4 << 9) + byte6

def calc_jump_addr(self, op):
    addr = op.addr
    if self.cmd.itype != self.itype_BRA and self.cmd.itype != self.itype_CAA:
        if self.cmd.itype == self.itype_C or self.cmd.itype == self.itype_B:
            if addr & 0x10000 != 0:
                # sign extend
                addr = self.cmd.ea - ((~addr & 0x1ffff) + 1)
            else:
                addr = addr + self.cmd.ea
        elif self.cmd.itype == self.itype_CAR or self.cmd.itype == self.itype_BRR:
            if addr & 0x4000000 != 0:
                # sign extend
                addr = self.cmd.ea - ((~addr & 0x7ffffff) + 1)
            else:
                addr = addr + self.cmd.ea
        else:
            addr = (addr + self.cmd.ea) & 0x7ffffff
    return addr

########################################
# Processor Type
########################################

def ana_ops(self, ops):
    inst = self.itable[self.cmd.itype]
    opcnt = 0
    opidx = 0
    hascc = False
    for w, v in inst.args:
        if v[0] == '0' or v[0] == '1':
            continue
        if v == 'rA' or v == 'rB' or v == 'rC':
            self.cmd[opcnt].type = o_reg
            self.cmd[opcnt].dtype = dt_dword
            self.cmd[opcnt].reg = ops[opidx]
            opcnt += 1
        elif v == 'Immediate':
            self.cmd[opcnt].type = o_imm
            self.cmd[opcnt].dtype = dt_dword
            self.cmd[opcnt].value = ops[opidx]
            opcnt += 1
        elif v == 'Location' or v == 'Offset':
            self.cmd[opcnt].type = o_near
            self.cmd[opcnt].dtype = dt_dword
            self.cmd[opcnt].addr = ops[opidx]
            opcnt += 1
        elif v == 'Register Count':
            self.cmd[opcnt - 1].type = o_displ
            self.cmd[opcnt - 1].dtype = dt_dword
            self.cmd[opcnt - 1].specval = ops[opidx]
            self.cmd[opcnt - 1].phrase = ops[opidx - 1]
            offset = ops[opidx + 2]
            if offset & 0x4000000:
                offset -= 0x8000000
            self.cmd[opcnt - 1].value = offset
        elif v == 'Adjust rB':
            self.cmd.auxpref |= ops[opidx] << 5
        elif v == 'UF':
            self.cmd.auxpref |= ops[opidx] << 4
        elif v == 'Condition':
            self.cmd.auxpref |= ops[opidx]
            hascc = True
        elif v == 'Memory Flags':
            self.cmd[opcnt].type = o_idpspec0
            self.cmd[opcnt].dtype = dt_dword
            self.cmd[opcnt].specval = ops[opidx]
            opcnt += 1
        elif v == 'Memory Offset':
            pass
        else:
            assert False
        opidx += 1
    if not hascc:
        self.cmd.auxpref |= 0xF

def ana(self):
    cmd = self.cmd
    current_ea = cmd.ea + cmd.size
    code_bit = ''
    for i in xrange(6):
        code_bit += '{:09b}'.format(get_full_byte(current_ea + i) & 0x1ff)
    code = int(code_bit, 2)
    idx = None
    for g in self.imatch:
        bitlen, masks = g
        ops, imap = self.imatch[g]
        code2 = fetch(code, bitlen)
        bits = tuple(map(lambda x: (code2 & x[0]) >> x[1], masks))
        if bits in imap:
            idx = imap[bits]
            self.cmd.itype = idx
            break
    if idx is None:
        return 0
    ana_ops(self, map(lambda x: (code2 & x[0]) >> x[1], ops))

    # Remove this block to disable simplifying ML+MH
    if cmd.itype == self.itype_MH and cmd.ea >= 3:
        code_bit = ''
        last_ea = cmd.ea - 3
        code_bit = '{:09b}{:09b}{:09b}'.format(get_full_byte(last_ea+1) & 0x1ff, get_full_byte(last_ea) & 0x1ff, get_full_byte(last_ea+2) & 0x1ff)
        code = int(code_bit, 2)
        if (code >> 22) & 0x1f == 0x12:
            regidx = (code >> 17) & 0x1f
            lo = code & 0x1ffff

            if regidx == cmd[0].reg:
                hi = cmd[1].value
                v = (hi << 10) | (lo & 0x3ff)
                cmd[1].value = v
                cmd.itype = self.itype_MEH

    # ms 0x1ffff -> ms -1
    if cmd.itype == self.itype_MS and (cmd[1].value & 0x10000):
        cmd[1].value -= 0x20000

    bytelen = bitlen // 9
    cmd.size += bytelen
    return bytelen

def add_stkpnt(self, pfn, v):
    if pfn:
        end = self.cmd.ea + self.cmd.size
        if not is_fixed_spd(end):
            add_auto_stkpnt2(pfn, end, v)
            print hex(end), v

def trace_sp(self):
    cmd = self.cmd
    pfn = get_func(cmd.ea)
    if not pfn:
        return
    if cmd.Op1.type == o_reg and cmd.Op1.reg == self.ireg_ST:
        if cmd.Op2.type == o_reg and cmd.Op2.reg == self.ireg_ST:
            if cmd.itype == self.itype_SBI:
                add_stkpnt(self, pfn, -SIGNEXT(cmd.Op3.value, 7))
            elif cmd.itype == self.itype_ADI:
                add_stkpnt(self, pfn, SIGNEXT(cmd.Op3.value, 7))

def emu(self):
    cmd = self.cmd
    aux = self.get_auxpref()

    flow = False
    if cmd.itype in [self.itype_B, self.itype_BR, self.itype_BRA, self.itype_BRR]:
        if cmd.itype != self.itype_BR:
            ua_add_cref(0, calc_jump_addr(self, cmd.Op1), fl_JN)
        if cmd.itype not in [self.itype_B, self.itype_BR] or (aux & 0xF) != 0xF:
            flow = True
    elif cmd.itype in [self.itype_C, self.itype_CR, self.itype_CAR, self.itype_CAA]:
        if cmd.itype != self.itype_CR:
            ua_add_cref(cmd.Op1.offb, calc_jump_addr(self, cmd.Op1), fl_CN)
        ua_add_cref(0, cmd.ea + cmd.size, fl_F)
    elif cmd.itype in [self.itype_RE, self.itype_HT]:
        pass
    else:
        flow = True

    if flow:
        ua_add_cref(0, cmd.ea + cmd.size, fl_F)

    if cmd.itype in [self.itype_MEH]:
        ua_add_dref(2, cmd[1].value, dr_R)
        c1 = get_full_byte(cmd[1].value) & 0x1ff
        c2 = get_full_byte(cmd[1].value+1) & 0x1ff
        c3 = get_full_byte(cmd[1].value+2) & 0x1ff
        if c1 >= 0x20 and c1 <= 0x7f \
                and c2 >= 0x20 and c2 <= 0x7f \
                and c3 >= 0x20 and c3 <= 0x7f:
            MakeCustomDataEx(cmd[1].value, 0, self.nstr_dtid, self.nstr_dfid)

    #if may_trace_sp():
    #    if flow:
    #        trace_sp(self)
    #    else:
    #        recalc_spd(self.cmd.ea)

    return True

def outop(self, op):
    optype = op.type
    if optype == o_reg:
        out_register(self.regNames[op.reg])
    elif optype == o_idpspec0:
        if op.specval == 0:
            out_symbol('N')
        elif op.specval == 1:
            out_symbol('R')
        elif op.specval == 2:
            out_symbol('R')
            out_symbol('W')
        elif op.specval == 3:
            out_symbol('E')
        else:
            out_symbol('E')
            out_symbol('R')
            out_symbol('R')
    elif optype == o_imm:
        # take size from x.dtyp
        OutValue(op, OOFW_32 | OOF_SIGNED)
    elif optype == o_near:
        addr = op.addr
        # offset
        if self.cmd.itype != self.itype_BRA and self.cmd.itype != self.itype_CAA:
            off = 0
            if self.cmd.itype == self.itype_C or self.cmd.itype == self.itype_B:
                if addr & 0x10000 != 0:
                    # sign extend
                    off = (~addr & 0x1ffff) + 1
                    addr = self.cmd.ea - ((~addr & 0x1ffff) + 1)
                    out_symbol('-')
                else:
                    off = addr
                    addr = addr + self.cmd.ea
                    out_symbol('+')
            elif self.cmd.itype == self.itype_CAR or self.cmd.itype == self.itype_BRR:
                if addr & 0x4000000 != 0:
                    # sign extend
                    off = (~addr & 0x7ffffff) + 1
                    addr = self.cmd.ea - ((~addr & 0x7ffffff) + 1)
                    out_symbol('-')
                else:
                    off = addr
                    addr = addr + self.cmd.ea
                    out_symbol('+')
            else:
                off = addr
                addr = (addr + self.cmd.ea) & 0x7ffffff
                out_symbol('+')

            OutLong(off, 16)

            out_symbol(' ')
            out_symbol('(')
            r = out_name_expr(op, addr, BADADDR)
            if not r:
                out_tagon(COLOR_ERROR)
                OutValue(op, OOF_ADDR)
                out_tagoff(COLOR_ERROR)
                QueueSet(Q_noName, self.cmd.ea)
            out_symbol(')')
        # location
        else:
            r = out_name_expr(op, addr, BADADDR)
            if not r:
                out_tagon(COLOR_ERROR)
                OutValue(op, OOF_ADDR)
                out_tagoff(COLOR_ERROR)
                QueueSet(Q_noName, self.cmd.ea)
    elif optype == o_displ:
        out_symbol('[')
        out_register(self.regNames[op.phrase])
        OutValue(op, OOFW_32 | OOFS_NEEDSIGN | OOF_SIGNED)
        out_symbol(',')
        out_symbol(' ')
        OutLine("%d" % (op.specval + 1))
        out_symbol(']')

    return True

class CLEMENCY(processor_t):
    # IDP id ( Numbers above 0x8000 are reserved for the third-party modules)
    id = 0x8000 + 0x999
    # Processor features
    flag = PR_ADJSEGS | PRN_HEX | PR_WORD_INS
    # Number of bits in a byte for code segments (usually 8)
    # IDA supports values up to 32 bits
    cnbits = 9
    # Number of bits in a byte for non-code segments (usually 8)
    # IDA supports values up to 32 bits
    dnbits = 9
    # short processor names (NULL terminated)
    # Each name should be shorter than 9 characters
    psnames = ["clemency"]
    # long processor names (NULL terminated)
    # No restriction on name lengthes.
    plnames = ["cLEMENCy"]

    segreg_size = 0

    ##########################
    # intruction
    # icode of the first instruction
    instruc_start = 0

    assembler = {
        "flag" : ASH_HEXF3 | ASD_DECF0 | ASO_OCTF1 | ASB_BINF3 | AS_NOTAB
               | AS_ASCIIC | AS_ASCIIZ,
        "uflag": 0,
        "name": "GNU assembler",

        "origin": ".org",
        "end": "end",
        "cmnt": ";",

        "ascsep": '"',
        "accsep": "'",
        "esccodes": "\"'",

        "a_ascii": ".ascii",
        "a_byte": ".byte",
        "a_word": ".word",
        "a_3byte": ".tribyte",

        "a_bss": "dfs %s",

        "a_seg": "seg",
        "a_curip": ".",
        "a_public": "",
        "a_weak": "",
        "a_extrn": ".extrn",
        "a_comdef": "",
        "a_align": ".align",

        "lbrace": "(",
        "rbrace": ")",
        "a_mod": "%",
        "a_band": "&",
        "a_bor": "|",
        "a_xor": "^",
        "a_bnot": "~",
        "a_shl": "<<",
        "a_shr": ">>",
        "a_sizeof_fmt": "size %s",
    }

    # flag for auxpref
    FL_UF              = 0x0010
    FL_CC              = 0x000F
    FL_ADJUST          = 0x0060


    module = __import__('clemency')
    def __init__(self):
        processor_t.__init__(self)
        # new data format
        self.init_data_format()
        # reload debug flag
        self.doReload = os.getenv('IDA_RELOAD')
        # init
        self._init_registers()
        self._init_instructions()

    def init_data_format(self):
        self.tribyte_dtid = register_custom_data_type(tribyte_data_type())
        self.tribyte_dfid = register_custom_data_format(self.tribyte_dtid, tribyte_data_format())
        self.nstr_dtid = register_custom_data_type(nbit_str_data_type())
        self.nstr_dfid = register_custom_data_format(self.nstr_dtid, nbit_str_data_format())


    def _init_registers(self):

        # Registers definition
        self.regNames = ["R%02d" % (i) for i in xrange(29)] + ["ST", "RA", "PC", "FL"] + ["CS", "DS"]

        # Create the ireg_XXXX constants
        for i in xrange(len(self.regNames)):
            setattr(self, 'ireg_' + self.regNames[i], i)

        # Set fake segment registers
        self.regFirstSreg = self.regCodeSreg = self.ireg_CS
        self.regLastSreg = self.regDataSreg = self.ireg_DS

    def _init_instructions(self):
        class idef:
            def __init__(self, name, cmt, fmt, cf, args):
                self.name = name
                self.cmt = cmt
                self.fmt = fmt
                self.cf = cf
                self.args = args

        self.itable = {}
        self.imatch = {}

        for j in range(len(inst_json)):
            i = inst_json[j]
            args = []
            for a in i['args']:
                args.append((a['width'], a['value']))

            # Set itable entry for instruction #j
            self.itable[j] = idef(i['name'], i['desc'], i['format'], i['feature'], args)

            # Generate matching table entry
            ws = sum([w for w, v in args])
            off = 0
            masks = []
            vals = []
            for w, v in args:
                if v[0] in '01':
                    masks.append(((1 << (ws - off)) - (1 << (ws - off - w)), ws - off - w))
                    vals.append(int(v, 2))
                off += w
            grp = (ws, tuple(masks))
            vals = tuple(vals)
            if grp not in self.imatch:
                ops = []
                off = 0
                for w, v in args:
                    if v[0] not in '01':
                        ops.append(((1 << (ws - off)) - (1 << (ws - off - w)), ws - off - w))
                    off += w
                self.imatch[grp] = (tuple(ops), {}) # (operand mask, inst match table)
            self.imatch[grp][1][vals] = j

        Instructions = []
        for j in range(len(self.itable)):
            x = self.itable[j]
            d = dict(name = x.name.lower(), feature=x.cf)
            if x.cmt:
                d['cmt'] = x.cmt
            Instructions.append(d)
            setattr(self, 'itype_' + x.name, j)

        d = dict(name = 'meh', feature=0)
        setattr(self, 'itype_MEH', len(Instructions))
        Instructions.append(d)

        self.instruc_end = len(Instructions) + 1
        self.instruc = Instructions
        self.icode_return = self.itype_RE

    def ana(self):
        if self.doReload:
            reload(self.module)
        dynana = getattr(self.module, 'ana')
        return dynana(self)

    def emu(self):
        if self.doReload:
            reload(self.module)
        dynemu = getattr(self.module, 'emu')
        return dynemu(self)

    cc_table = [
            'n',
            'e',
            'l',
            'le',
            'g',
            'ge',
            'no',
            'o',
            'ns',
            's',
            'sl',
            'sle',
            'sg',
            'sge',
            '',
            '',
            ]

    def out(self):
        buf = idaapi.init_output_buffer(1024)

        postfix = ''
        # Adjust Register
        #   e.g., LDSI, LDSD
        adjust_flag = (self.cmd.auxpref & self.FL_ADJUST) >> 5
        if adjust_flag == 1:
            postfix += 'i'
        elif adjust_flag == 2:
            postfix += 'd'

        # Conditional
        #   e.g., Bge
        cc_idx = self.cmd.auxpref & self.FL_CC
        if cc_idx != 0xf:
            idx = self.cmd.auxpref & self.FL_CC
            postfix += self.cc_table[idx]

        # Update Flag
        #   e.g., ad.
        if self.cmd.auxpref & self.FL_UF != 0:
            postfix += '.'

        OutMnem(12, postfix)

        for i in xrange(6):
            op = self.cmd[i]

            if op.type == o_void:
                break

            if i > 0:
                out_symbol(',')
                OutChar(' ')
            out_one_operand(i)

        term_output_buffer()
        cvar.gl_comm = 1
        MakeLine(buf)

    def outop(self, op):
        if self.doReload:
            reload(self.module)
        dynoutop = getattr(self.module, 'outop')
        return dynoutop(self, op)

########################################
# Data format for TriBytes (9bits)
########################################
class tribyte_data_type(data_type_t):
    ASM_KEYWORD = ".tri"
    def __init__(self):
        data_type_t.__init__(self,
                             name = "py_tribyte",
                             hotkey = 'z',
                             value_size = 1,
                             menu_name = "TriBytes (9bits)",
                             asm_keyword = tribyte_data_type.ASM_KEYWORD)

    def calc_item_size(self, ea, maxsize):
        return 3

class tribyte_data_format(data_format_t):
    def __init__(self):
        data_format_t.__init__(self,
                               name = "py_tribyte_format",
                               menu_name = "TriBytes (9bits)")

    def printf(self, value, current_ea, operand_num, dtid):
        b1 = idaapi.get_full_byte(current_ea) & 0x1ff
        b2 = idaapi.get_full_byte(current_ea+1) & 0x1ff
        b3 = idaapi.get_full_byte(current_ea+2) & 0x1ff
        return hex((b2 << 18) + (b1 << 9) + b3)

class nbit_str_data_type(data_type_t):
    ASM_KEYWORD = ".str"
    def __init__(self):
        data_type_t.__init__(self,
                             name = "py_str",
                             hotkey = ',',
                             value_size = 1,
                             menu_name = "String (9bits)",
                             asm_keyword = nbit_str_data_type.ASM_KEYWORD)

    def calc_item_size(self, ea, maxsize):
        r = 0
        while True:
            c = idaapi.get_full_byte(ea + r) & 0x1ff
            if c == 0:
                break
            r += 1

        return r + 1

class nbit_str_data_format(data_format_t):
    def __init__(self):
        data_format_t.__init__(self,
                               name = "py_str_format",
                               menu_name = "String (9bits) format")

    def printf(self, value, current_ea, operand_num, dtid):
        r = ''
        for i in xrange(len(value) - 1):
            r += chr(idaapi.get_full_byte(current_ea + i) & 0xff)
        return '"%s", 0' % (repr(r))

########################################
# Processor Plugin Entry
########################################
def PROCESSOR_ENTRY():
    # add proc into module path
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    sys.path.insert(0, script_dir)
    return CLEMENCY()
