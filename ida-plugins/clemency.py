from idaapi import *

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
    plnames = ["cLemency"]

    segreg_size = 0

    ##########################
    # intruction
    # icode of the first instruction
    instruc_start = 0
    # icode of the last instruction + 1
    instruc_end = 2

    instruc = [
            {'name': 'push', 'feature': CF_USE1},
            {'name': 'pop', 'feature': CF_USE1},
            ]
    ##########################

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

    def __init__(self):
        processor_t.__init__(self)
        self._init_registers()

    def _init_registers(self):

        # Registers definition
        self.regNames = ["R%d" % (i) for i in xrange(29)] + ["ST", "RA", "PC", "FL"] + ["CS", "DS"]

        # Create the ireg_XXXX constants
        for i in xrange(len(self.regNames)):
            setattr(self, 'ireg_' + self.regNames[i], i)

        # Set fake segment registers
        self.regFirstSreg = self.regCodeSreg = self.ireg_CS
        self.regLastSreg = self.regDataSreg = self.ireg_DS

    def ana(self):
        return 0

    def emu(self):
        return True

    def out(self):
        return True

    def outop(self, op):
        return True

def PROCESSOR_ENTRY():
    return CLEMENCY()
