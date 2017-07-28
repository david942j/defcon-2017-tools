#!/usr/bin/env python

inst_json = [
  {
    "name": "AD",
    "desc": "Add",
    "args": [
      {
        "value": "0000000",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "AD rA, rB, rC"
  },
  {
    "name": "ADC",
    "desc": "Add With Carry",
    "args": [
      {
        "value": "0100000",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "ADC rA, rB, rC"
  },
  {
    "name": "ADCI",
    "desc": "Add Immediate With Carry",
    "args": [
      {
        "value": "0100000",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "01",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "ADCI rA, rB, IMM"
  },
  {
    "name": "ADCIM",
    "desc": "Add Immediate Multi Reg With Carry",
    "args": [
      {
        "value": "0100010",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "01",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "ADCIM rA, rB, IMM"
  },
  {
    "name": "ADCM",
    "desc": "Add Multi Reg With Carry",
    "args": [
      {
        "value": "0100010",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "ADCM rA, rB, rC"
  },
  {
    "name": "ADF",
    "desc": "Add Floating Point",
    "args": [
      {
        "value": "0000001",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "ADF rA, rB, rC"
  },
  {
    "name": "ADFM",
    "desc": "Add Floating Point Multi Reg",
    "args": [
      {
        "value": "0000011",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "ADFM rA, rB, rC"
  },
  {
    "name": "ADI",
    "desc": "Add Immediate",
    "args": [
      {
        "value": "0000000",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "01",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "ADI rA, rB, IMM"
  },
  {
    "name": "ADIM",
    "desc": "Add Immediate Multi Reg",
    "args": [
      {
        "value": "0000010",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "01",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "ADIM rA, rB, IMM"
  },
  {
    "name": "ADM",
    "desc": "Add Multi Reg",
    "args": [
      {
        "value": "0000010",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "ADM rA, rB, rC"
  },
  {
    "name": "AN",
    "desc": "And",
    "args": [
      {
        "value": "0010100",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "AN rA, rB, rC"
  },
  {
    "name": "ANI",
    "desc": "And Immediate",
    "args": [
      {
        "value": "0010100",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "01",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "ANI rA, rB, IMM"
  },
  {
    "name": "ANM",
    "desc": "And Multi Reg",
    "args": [
      {
        "value": "0010110",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "ANM rA, rB, rC"
  },
  {
    "name": "B",
    "desc": "Branch Conditional",
    "args": [
      {
        "value": "110000",
        "width": 6
      },
      {
        "value": "Condition",
        "width": 4
      },
      {
        "value": "Offset",
        "width": 17
      }
    ],
    "format": "Bcc Offset"
  },
  {
    "name": "BF",
    "desc": "Bit Flip",
    "args": [
      {
        "value": "101001100",
        "width": 9
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "1000000",
        "width": 7
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "BF rA, rB"
  },
  {
    "name": "BFM",
    "desc": "Bit Flip Multi Reg",
    "args": [
      {
        "value": "101001110",
        "width": 9
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "1000000",
        "width": 7
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "BFM rA, rB"
  },
  {
    "name": "BR",
    "desc": "Branch Register Conditional",
    "args": [
      {
        "value": "110010",
        "width": 6
      },
      {
        "value": "Condition",
        "width": 4
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "000",
        "width": 3
      }
    ],
    "format": "BRcc rA"
  },
  {
    "name": "BRA",
    "desc": "Branch Absolute",
    "args": [
      {
        "value": "111000100",
        "width": 9
      },
      {
        "value": "Location",
        "width": 27
      }
    ],
    "format": "BRA Location"
  },
  {
    "name": "BRR",
    "desc": "Branch Relative",
    "args": [
      {
        "value": "111000000",
        "width": 9
      },
      {
        "value": "Offset",
        "width": 27
      }
    ],
    "format": "BRR Offset"
  },
  {
    "name": "C",
    "desc": "Call Conditional",
    "args": [
      {
        "value": "110101",
        "width": 6
      },
      {
        "value": "Condition",
        "width": 4
      },
      {
        "value": "Offset",
        "width": 17
      }
    ],
    "format": "Ccc Offset"
  },
  {
    "name": "CAA",
    "desc": "Call Absolute",
    "args": [
      {
        "value": "111001100",
        "width": 9
      },
      {
        "value": "Location",
        "width": 27
      }
    ],
    "format": "CAA Location"
  },
  {
    "name": "CAR",
    "desc": "Call Relative",
    "args": [
      {
        "value": "111001000",
        "width": 9
      },
      {
        "value": "Offset",
        "width": 27
      }
    ],
    "format": "CAR Offset"
  },
  {
    "name": "CM",
    "desc": "Compare",
    "args": [
      {
        "value": "10111000",
        "width": 8
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      }
    ],
    "format": "CM rA, rB"
  },
  {
    "name": "CMF",
    "desc": "Compare Floating Point",
    "args": [
      {
        "value": "10111010",
        "width": 8
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      }
    ],
    "format": "CMF rA, rB"
  },
  {
    "name": "CMFM",
    "desc": "Compare Floating Point Multi Reg",
    "args": [
      {
        "value": "10111110",
        "width": 8
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      }
    ],
    "format": "CMFM rA, rB"
  },
  {
    "name": "CMI",
    "desc": "Compare Immediate",
    "args": [
      {
        "value": "10111001",
        "width": 8
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 14
      }
    ],
    "format": "CMI rA, IMM"
  },
  {
    "name": "CMIM",
    "desc": "Compare Immediate Multi Reg",
    "args": [
      {
        "value": "10111101",
        "width": 8
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 14
      }
    ],
    "format": "CMIM rA, IMM"
  },
  {
    "name": "CMM",
    "desc": "Compare Multi Reg",
    "args": [
      {
        "value": "10111100",
        "width": 8
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      }
    ],
    "format": "CMM rA, rB"
  },
  {
    "name": "CR",
    "desc": "Call Register Conditional",
    "args": [
      {
        "value": "110111",
        "width": 6
      },
      {
        "value": "Condition",
        "width": 4
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "000",
        "width": 3
      }
    ],
    "format": "CRcc rA"
  },
  {
    "name": "DBRK",
    "desc": "Debug Break",
    "args": [
      {
        "value": "111111111111111111",
        "width": 18
      }
    ],
    "format": "DBRK"
  },
  {
    "name": "DI",
    "desc": "Disable Interrupts",
    "args": [
      {
        "value": "101000000101",
        "width": 12
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "0",
        "width": 1
      }
    ],
    "format": "DI rA"
  },
  {
    "name": "DMT",
    "desc": "Direct Memory Transfer",
    "args": [
      {
        "value": "0110100",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "00000",
        "width": 5
      }
    ],
    "format": "DMT rA, rB, rC"
  },
  {
    "name": "DV",
    "desc": "Divide",
    "args": [
      {
        "value": "0001100",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "DV rA, rB, rC"
  },
  {
    "name": "DVF",
    "desc": "Divide Floating Point",
    "args": [
      {
        "value": "0001101",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "DVF rA, rB, rC"
  },
  {
    "name": "DVFM",
    "desc": "Divide Floating Point Multi Reg",
    "args": [
      {
        "value": "0001111",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "DVFM rA, rB, rC"
  },
  {
    "name": "DVI",
    "desc": "Divide Immediate",
    "args": [
      {
        "value": "0001100",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "01",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "DVI rA, rB, IMM"
  },
  {
    "name": "DVIM",
    "desc": "Divide Immediate Multi Reg",
    "args": [
      {
        "value": "0001110",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "01",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "DVIM rA, rB, IMM"
  },
  {
    "name": "DVIS",
    "desc": "Divide Immediate Signed",
    "args": [
      {
        "value": "0001100",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "11",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "DVIS rA, rB, IMM"
  },
  {
    "name": "DVISM",
    "desc": "Divide Immediate Signed Multi Reg",
    "args": [
      {
        "value": "0001110",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "11",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "DVISM rA, rB, IMM"
  },
  {
    "name": "DVM",
    "desc": "Divide Multi Reg",
    "args": [
      {
        "value": "0001110",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "DVM rA, rB, rC"
  },
  {
    "name": "DVS",
    "desc": "Divide Signed",
    "args": [
      {
        "value": "0001100",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0010",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "DVS rA, rB, rC"
  },
  {
    "name": "DVSM",
    "desc": "Divide Signed Multi Reg",
    "args": [
      {
        "value": "0001110",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0010",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "DVSM rA, rB, rC"
  },
  {
    "name": "EI",
    "desc": "Enable Interrupts",
    "args": [
      {
        "value": "101000000100",
        "width": 12
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "0",
        "width": 1
      }
    ],
    "format": "EI rA"
  },
  {
    "name": "FTI",
    "desc": "Float to Integer",
    "args": [
      {
        "value": "101000101",
        "width": 9
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "00000000",
        "width": 8
      }
    ],
    "format": "FTI rA, rB"
  },
  {
    "name": "FTIM",
    "desc": "Float to Integer Multi Reg",
    "args": [
      {
        "value": "101000111",
        "width": 9
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "00000000",
        "width": 8
      }
    ],
    "format": "FTIM rA, rB"
  },
  {
    "name": "HT",
    "desc": "Halt",
    "args": [
      {
        "value": "101000000011000000",
        "width": 18
      }
    ],
    "format": "HT"
  },
  {
    "name": "IR",
    "desc": "Interrupt Return",
    "args": [
      {
        "value": "101000000001000000",
        "width": 18
      }
    ],
    "format": "IR"
  },
  {
    "name": "ITF",
    "desc": "Integer to Float",
    "args": [
      {
        "value": "101000100",
        "width": 9
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "00000000",
        "width": 8
      }
    ],
    "format": "ITF rA, rB"
  },
  {
    "name": "ITFM",
    "desc": "Integer to Float Multi Reg",
    "args": [
      {
        "value": "101000110",
        "width": 9
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "00000000",
        "width": 8
      }
    ],
    "format": "ITFM rA, rB"
  },
  {
    "name": "LDS",
    "desc": "Load Single",
    "args": [
      {
        "value": "1010100",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Register Count",
        "width": 5
      },
      {
        "value": "Adjust rB",
        "width": 2
      },
      {
        "value": "Memory Offset",
        "width": 27
      },
      {
        "value": "000",
        "width": 3
      }
    ],
    "format": "LDSm rA, [rB + Offset, RegCount]"
  },
  {
    "name": "LDT",
    "desc": "Load Tri",
    "args": [
      {
        "value": "1010110",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Register Count",
        "width": 5
      },
      {
        "value": "Adjust rB",
        "width": 2
      },
      {
        "value": "Memory Offset",
        "width": 27
      },
      {
        "value": "000",
        "width": 3
      }
    ],
    "format": "LDTm rA, [rB + Offset, RegCount]"
  },
  {
    "name": "LDW",
    "desc": "Load Word",
    "args": [
      {
        "value": "1010101",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Register Count",
        "width": 5
      },
      {
        "value": "Adjust rB",
        "width": 2
      },
      {
        "value": "Memory Offset",
        "width": 27
      },
      {
        "value": "000",
        "width": 3
      }
    ],
    "format": "LDWm rA, [rB + Offset, RegCount]"
  },
  {
    "name": "MD",
    "desc": "Modulus",
    "args": [
      {
        "value": "0010000",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "MD rA, rB, rC"
  },
  {
    "name": "MDF",
    "desc": "Modulus Floating Point",
    "args": [
      {
        "value": "0010001",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "MDF rA, rB, rC"
  },
  {
    "name": "MDFM",
    "desc": "Modulus Floating Point Multi Reg",
    "args": [
      {
        "value": "0010011",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "MDFM rA, rB, rC"
  },
  {
    "name": "MDI",
    "desc": "Modulus Immediate",
    "args": [
      {
        "value": "0010000",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "01",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "MDI rA, rB, IMM"
  },
  {
    "name": "MDIM",
    "desc": "Modulus Immediate Multi Reg",
    "args": [
      {
        "value": "0010010",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "01",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "MDIM rA, rB, IMM"
  },
  {
    "name": "MDIS",
    "desc": "Modulus Immediate Signed",
    "args": [
      {
        "value": "0010000",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "11",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "MDIS rA, rB, IMM"
  },
  {
    "name": "MDISM",
    "desc": "Modulus Immediate Signed Multi Reg",
    "args": [
      {
        "value": "0010010",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "11",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "MDISM rA, rB, IMM"
  },
  {
    "name": "MDM",
    "desc": "Modulus Multi Reg",
    "args": [
      {
        "value": "0010010",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "MDM rA, rB, rC"
  },
  {
    "name": "MDS",
    "desc": "Modulus Signed",
    "args": [
      {
        "value": "0010000",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0010",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "MDS rA, rB, rC"
  },
  {
    "name": "MDSM",
    "desc": "Modulus Signed Multi Reg",
    "args": [
      {
        "value": "0010010",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0010",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "MDSM rA, rB, rC"
  },
  {
    "name": "MH",
    "desc": "Move High",
    "args": [
      {
        "value": "10001",
        "width": 5
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 17
      }
    ],
    "format": "MH rA, IMM"
  },
  {
    "name": "ML",
    "desc": "Move Low",
    "args": [
      {
        "value": "10010",
        "width": 5
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 17
      }
    ],
    "format": "ML rA, IMM"
  },
  {
    "name": "MS",
    "desc": "Move Low Signed",
    "args": [
      {
        "value": "10011",
        "width": 5
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 17
      }
    ],
    "format": "MS rA, IMM"
  },
  {
    "name": "MU",
    "desc": "Multiply",
    "args": [
      {
        "value": "0001000",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "MU rA, rB, rC"
  },
  {
    "name": "MUF",
    "desc": "Multiply Floating Point",
    "args": [
      {
        "value": "0001001",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "MUF rA, rB, rC"
  },
  {
    "name": "MUFM",
    "desc": "Multiply Floating Point Multi Reg",
    "args": [
      {
        "value": "0001011",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "MUFM rA, rB, rC"
  },
  {
    "name": "MUI",
    "desc": "Multiply Immediate",
    "args": [
      {
        "value": "0001000",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "01",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "MUI rA, rB, IMM"
  },
  {
    "name": "MUIM",
    "desc": "Multiply Immediate Multi Reg",
    "args": [
      {
        "value": "0001010",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "01",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "MUIM rA, rB, IMM"
  },
  {
    "name": "MUIS",
    "desc": "Multiply Immediate Signed",
    "args": [
      {
        "value": "0001000",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "11",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "MUIS rA, rB, IMM"
  },
  {
    "name": "MUISM",
    "desc": "Multiply Immediate Signed Multi Reg",
    "args": [
      {
        "value": "0001010",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "11",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "MUISM rA, rB, IMM"
  },
  {
    "name": "MUM",
    "desc": "Multiply Multi Reg",
    "args": [
      {
        "value": "0001010",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "MUM rA, rB, rC"
  },
  {
    "name": "MUS",
    "desc": "Multiply Signed",
    "args": [
      {
        "value": "0001000",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0010",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "MUS rA, rB, rC"
  },
  {
    "name": "MUSM",
    "desc": "Multiply Signed Multi Reg",
    "args": [
      {
        "value": "0001010",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0010",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "MUSM rA, rB, rC"
  },
  {
    "name": "NG",
    "desc": "Negate",
    "args": [
      {
        "value": "101001100",
        "width": 9
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "0000000",
        "width": 7
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "NG rA, rB"
  },
  {
    "name": "NGF",
    "desc": "Negate Floating Point",
    "args": [
      {
        "value": "101001101",
        "width": 9
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "0000000",
        "width": 7
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "NGF rA, rB"
  },
  {
    "name": "NGFM",
    "desc": "Negate Floating Point Multi Reg",
    "args": [
      {
        "value": "101001111",
        "width": 9
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "0000000",
        "width": 7
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "NGFM rA, rB"
  },
  {
    "name": "NGM",
    "desc": "Negate Multi Reg",
    "args": [
      {
        "value": "101001110",
        "width": 9
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "0000000",
        "width": 7
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "NGM rA, rB"
  },
  {
    "name": "NT",
    "desc": "Not",
    "args": [
      {
        "value": "101001100",
        "width": 9
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "0100000",
        "width": 7
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "NT rA, rB"
  },
  {
    "name": "NTM",
    "desc": "Not Multi Reg",
    "args": [
      {
        "value": "101001110",
        "width": 9
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "0100000",
        "width": 7
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "NTM rA, rB"
  },
  {
    "name": "OR",
    "desc": "Or",
    "args": [
      {
        "value": "0011000",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "OR rA, rB, rC"
  },
  {
    "name": "ORI",
    "desc": "Or Immediate",
    "args": [
      {
        "value": "0011000",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "01",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "ORI rA, rB, IMM"
  },
  {
    "name": "ORM",
    "desc": "Or Multi Reg",
    "args": [
      {
        "value": "0011010",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "ORM rA, rB, rC"
  },
  {
    "name": "RE",
    "desc": "Return",
    "args": [
      {
        "value": "101000000000000000",
        "width": 18
      }
    ],
    "format": "RE"
  },
  {
    "name": "RF",
    "desc": "Read Flags",
    "args": [
      {
        "value": "101000001100",
        "width": 12
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "0",
        "width": 1
      }
    ],
    "format": "RF rA"
  },
  {
    "name": "RL",
    "desc": "Rotate Left",
    "args": [
      {
        "value": "0110000",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "RL rA, rB, rC"
  },
  {
    "name": "RLI",
    "desc": "Rotate Left Immediate",
    "args": [
      {
        "value": "1000000",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "00",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "RLI rA, rB, IMM"
  },
  {
    "name": "RLIM",
    "desc": "Rotate Left Immediate Multi Reg",
    "args": [
      {
        "value": "1000010",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "00",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "RLIM rA, rB, IMM"
  },
  {
    "name": "RLM",
    "desc": "Rotate Left Multi Reg",
    "args": [
      {
        "value": "0110010",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "RLM rA, rB, rC"
  },
  {
    "name": "RMP",
    "desc": "Read Memory Protection",
    "args": [
      {
        "value": "1010010",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "0000000000",
        "width": 10
      }
    ],
    "format": "RMP rA, rB"
  },
  {
    "name": "RND",
    "desc": "Random",
    "args": [
      {
        "value": "101001100",
        "width": 9
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "000001100000",
        "width": 12
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "RND rA"
  },
  {
    "name": "RNDM",
    "desc": "Random Multi Reg",
    "args": [
      {
        "value": "101001110",
        "width": 9
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "000001100000",
        "width": 12
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "RNDM rA"
  },
  {
    "name": "RR",
    "desc": "Rotate Right",
    "args": [
      {
        "value": "0110001",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "RR rA, rB, rC"
  },
  {
    "name": "RRI",
    "desc": "Rotate Right Immediate",
    "args": [
      {
        "value": "1000001",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "00",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "RRI rA, rB, IMM"
  },
  {
    "name": "RRIM",
    "desc": "Rotate Right Immediate Multi Reg",
    "args": [
      {
        "value": "1000011",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "00",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "RRIM rA, rB, rC"
  },
  {
    "name": "RRM",
    "desc": "Rotate Right Multi Reg",
    "args": [
      {
        "value": "0110011",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "RRM rA, rB, rC"
  },
  {
    "name": "SA",
    "desc": "Shift Arithemetic Right",
    "args": [
      {
        "value": "0101101",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "SA rA, rB, rC"
  },
  {
    "name": "SAI",
    "desc": "Shift Arithemetic Right Immediate",
    "args": [
      {
        "value": "0111101",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "00",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "SAI rA, rB, IMM"
  },
  {
    "name": "SAIM",
    "desc": "Shift Arithemetic Right Immedi- ate Multi Reg",
    "args": [
      {
        "value": "0111111",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "00",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "SAIM rA, rB, IMM"
  },
  {
    "name": "SAM",
    "desc": "Shift Arithemetic Right Multi Reg",
    "args": [
      {
        "value": "0101111",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "SAM rA, rB, rC"
  },
  {
    "name": "SB",
    "desc": "Subtract",
    "args": [
      {
        "value": "0000100",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "SB rA, rB, rC"
  },
  {
    "name": "SBC",
    "desc": "Subtract With Carry",
    "args": [
      {
        "value": "0100100",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "SBC rA, rB, rC"
  },
  {
    "name": "SBCI",
    "desc": "Subtract Immediate With Carry",
    "args": [
      {
        "value": "0100100",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "01",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "SBCI rA, rB, IMM"
  },
  {
    "name": "SBCIM",
    "desc": "Subtract Immediate Multi Reg With Carry",
    "args": [
      {
        "value": "0100110",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "01",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "SBCIM rA, rB, IMM"
  },
  {
    "name": "SBCM",
    "desc": "Subtract Multi Reg With Carry",
    "args": [
      {
        "value": "0100110",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "SBCM rA, rB, rC"
  },
  {
    "name": "SBF",
    "desc": "Subtract Floating Point",
    "args": [
      {
        "value": "0000101",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "SBF rA, rB, rC"
  },
  {
    "name": "SBFM",
    "desc": "Subtract Floating Point Multi Reg",
    "args": [
      {
        "value": "0000111",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "SBFM rA, rB, rC"
  },
  {
    "name": "SBI",
    "desc": "Subtract Immediate",
    "args": [
      {
        "value": "0000100",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "01",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "SBI rA, rB, IMM"
  },
  {
    "name": "SBIM",
    "desc": "Subtract Immediate Multi Reg",
    "args": [
      {
        "value": "0000110",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "01",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "SBIM rA, rB, IMM"
  },
  {
    "name": "SBM",
    "desc": "Subtract Multi Reg",
    "args": [
      {
        "value": "0000110",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "SBM rA, rB, rC"
  },
  {
    "name": "SES",
    "desc": "Sign Extend Single",
    "args": [
      {
        "value": "101000000111",
        "width": 12
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "00000",
        "width": 5
      }
    ],
    "format": "SES rA, rB"
  },
  {
    "name": "SEW",
    "desc": "Sign Extend Word",
    "args": [
      {
        "value": "101000001000",
        "width": 12
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "00000",
        "width": 5
      }
    ],
    "format": "SEW rA, rB"
  },
  {
    "name": "SF",
    "desc": "Set Flags",
    "args": [
      {
        "value": "101000001011",
        "width": 12
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "0",
        "width": 1
      }
    ],
    "format": "SF rA"
  },
  {
    "name": "SL",
    "desc": "Shift Left",
    "args": [
      {
        "value": "0101000",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "SL rA, rB, rC"
  },
  {
    "name": "SLI",
    "desc": "Shift Left Immediate",
    "args": [
      {
        "value": "0111000",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "00",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "SLI rA, rB, IMM"
  },
  {
    "name": "SLIM",
    "desc": "Shift Left Immediate Multi Reg",
    "args": [
      {
        "value": "0111010",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "00",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "SLIM rA, rB, IMM"
  },
  {
    "name": "SLM",
    "desc": "Shift Left Multi Reg",
    "args": [
      {
        "value": "0101010",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "SLM rA, rB, rC"
  },
  {
    "name": "SMP",
    "desc": "Set Memory Protection",
    "args": [
      {
        "value": "1010010",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "1",
        "width": 1
      },
      {
        "value": "Memory Flags",
        "width": 2
      },
      {
        "value": "0000000",
        "width": 7
      }
    ],
    "format": "SMP rA, rB, FLAGS"
  },
  {
    "name": "SR",
    "desc": "Shift Right",
    "args": [
      {
        "value": "0101001",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "SR rA, rB, rC"
  },
  {
    "name": "SRI",
    "desc": "Shift Right Immediate",
    "args": [
      {
        "value": "0111001",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "00",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "SRI rA, rB, IMM"
  },
  {
    "name": "SRIM",
    "desc": "Shift Right Immediate Multi Reg",
    "args": [
      {
        "value": "0111011",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "00",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "SRIM rA, rB, IMM"
  },
  {
    "name": "SRM",
    "desc": "Shift Right Multi Reg",
    "args": [
      {
        "value": "0101011",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "SRM rA, rB, rC"
  },
  {
    "name": "STS",
    "desc": "Store Single",
    "args": [
      {
        "value": "1011000",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Register Count",
        "width": 5
      },
      {
        "value": "Adjust rB",
        "width": 2
      },
      {
        "value": "Memory Offset",
        "width": 27
      },
      {
        "value": "000",
        "width": 3
      }
    ],
    "format": "STSm rA, [rB + Offset, RegCount]"
  },
  {
    "name": "STT",
    "desc": "Store Tri",
    "args": [
      {
        "value": "1011010",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Register Count",
        "width": 5
      },
      {
        "value": "Adjust rB",
        "width": 2
      },
      {
        "value": "Memory Offset",
        "width": 27
      },
      {
        "value": "000",
        "width": 3
      }
    ],
    "format": "STTm rA, [rB + Offset, RegCount]"
  },
  {
    "name": "STW",
    "desc": "Store Word",
    "args": [
      {
        "value": "1011001",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Register Count",
        "width": 5
      },
      {
        "value": "Adjust rB",
        "width": 2
      },
      {
        "value": "Memory Offset",
        "width": 27
      },
      {
        "value": "000",
        "width": 3
      }
    ],
    "format": "STWm rA, [rB + Offset, RegCount]"
  },
  {
    "name": "WT",
    "desc": "Wait",
    "args": [
      {
        "value": "101000000010000000",
        "width": 18
      }
    ],
    "format": "WT"
  },
  {
    "name": "XR",
    "desc": "Xor",
    "args": [
      {
        "value": "0011100",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "XR rA, rB, rC"
  },
  {
    "name": "XRI",
    "desc": "Xor Immediate",
    "args": [
      {
        "value": "0011100",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "Immediate",
        "width": 7
      },
      {
        "value": "01",
        "width": 2
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "XRI rA, rB, IMM"
  },
  {
    "name": "XRM",
    "desc": "Xor Multi Reg",
    "args": [
      {
        "value": "0011110",
        "width": 7
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "rC",
        "width": 5
      },
      {
        "value": "0000",
        "width": 4
      },
      {
        "value": "UF",
        "width": 1
      }
    ],
    "format": "XRM rA, rB, rC"
  },
  {
    "name": "ZES",
    "desc": "Zero Extend Single",
    "args": [
      {
        "value": "101000001001",
        "width": 12
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "00000",
        "width": 5
      }
    ],
    "format": "ZES rA, rB"
  },
  {
    "name": "ZEW",
    "desc": "Zero Extend Word",
    "args": [
      {
        "value": "101000001010",
        "width": 12
      },
      {
        "value": "rA",
        "width": 5
      },
      {
        "value": "rB",
        "width": 5
      },
      {
        "value": "00000",
        "width": 5
      }
    ],
    "format": "ZEW rA, rB"
  }
]

'''
class A:
    def _init_instructions(self):
        class idef:
            def __init__(self, name, cmt, fmt, args):
                self.name = name
                self.cmt = cmt
                self.fmt = fmt
                self.args = args

        self.itable = {}
        self.imatch = {}

        for j in range(len(inst_json)):
            i = inst_json[j]
            args = []
            for a in i['args']:
                args.append((a['width'], a['value']))

            # Set itable entry for instruction #j
            self.itable[j] = idef(i['name'], i['desc'], i['format'], args)

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
            d = dict(name = x.name, feature=0)
            if x.cmt:
                d['cmt'] = x.cmt
            Instructions.append(d)
            setattr(self, 'itype_' + x.name, j)

        self.instruc_end = len(Instructions) + 1
        self.instruc = Instructions
        self.icode_return = self.itype_RE

    def fetch(self, code, n):
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

    def ana(self):

        code_bit = ''.join(map(lambda x: '{:09b}'.format(x), [0, 0, 0x20, 0, 0, 2]))
        code = int(code_bit, 2)

        for g in self.imatch:
            bitlen, masks = g
            ops, imap = self.imatch[g]
            code2 = self.fetch(code, bitlen)
            bits = tuple(map(lambda x: (code2 & x[0]) >> x[1], masks))
            print code
            print code2
            print bitlen
            print masks
            print imap
            print bits
            print '{:054b}'.format(code2)
            print '============================================='
            if bits in imap:
                idx = imap[bits]
                print self.itable[idx].name, self.itable[idx].args


a = A()
a._init_instructions()
a.ana()
'''
