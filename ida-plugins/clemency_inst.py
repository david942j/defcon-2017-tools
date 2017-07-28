#!/usr/bin/env python

import sys
import idaapi
from idaapi import *

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
    "format": "AD rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "ADC rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "ADCI rA, rB, IMM",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "ADCIM rA, rB, IMM",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "ADCM rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "ADF rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "ADFM rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "ADI rA, rB, IMM",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "ADIM rA, rB, IMM",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "ADM rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "AN rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "ANI rA, rB, IMM",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "ANM rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "Bcc Offset",
    "feature": CF_USE1 | CF_JUMP
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
    "format": "BF rA, rB",
    "feature": CF_CHG1 | CF_USE2
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
    "format": "BFM rA, rB",
    "feature": CF_CHG1 | CF_USE2
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
    "format": "BRcc rA",
    "feature": CF_USE1 | CF_JUMP
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
    "format": "BRA Location",
    "feature": CF_USE1 | CF_JUMP
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
    "format": "BRR Offset",
    "feature": CF_USE1 | CF_JUMP
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
    "format": "Ccc Offset",
    "feature": CF_USE1 | CF_CALL
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
    "format": "CAA Location",
    "feature": CF_USE1 | CF_CALL
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
    "format": "CAR Offset",
    "feature": CF_USE1 | CF_CALL
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
    "format": "CM rA, rB",
    "feature": CF_CHG1 | CF_USE2
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
    "format": "CMF rA, rB",
    "feature": CF_CHG1 | CF_USE2
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
    "format": "CMFM rA, rB",
    "feature": CF_CHG1 | CF_USE2
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
    "format": "CMI rA, IMM",
    "feature": CF_USE1 | CF_USE2
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
    "format": "CMIM rA, IMM",
    "feature": CF_USE1 | CF_USE2
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
    "format": "CMM rA, rB",
    "feature": CF_USE1 | CF_USE2
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
    "format": "CRcc rA",
    "feature": CF_USE1 | CF_CALL
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
    "format": "DBRK",
    "feature": CF_STOP,
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
    "format": "DI rA",
    "feature": CF_USE1
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
    "format": "DMT rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "DV rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "DVF rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "DVFM rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "DVI rA, rB, IMM",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "DVIM rA, rB, IMM",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "DVIS rA, rB, IMM",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "DVISM rA, rB, IMM",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "DVM rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "DVS rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "DVSM rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "EI rA",
    "feature": CF_USE1
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
    "format": "FTI rA, rB",
    "feature": CF_CHG1 | CF_USE2
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
    "format": "FTIM rA, rB",
    "feature": CF_CHG1 | CF_USE2
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
    "format": "HT",
    "feature": CF_STOP
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
    "format": "IR",
    "feature": CF_STOP
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
    "format": "ITF rA, rB",
    "feature": CF_CHG1 | CF_USE2
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
    "format": "ITFM rA, rB",
    "feature": CF_CHG1 | CF_USE2
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
    "format": "LDSm rA, [rB + Offset, RegCount]",
    "feature": CF_CHG1 | CF_USE2
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
    "format": "LDTm rA, [rB + Offset, RegCount]",
    "feature": CF_CHG1 | CF_USE2
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
    "format": "LDWm rA, [rB + Offset, RegCount]",
    "feature": CF_CHG1 | CF_USE2
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
    "format": "MD rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "MDF rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "MDFM rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "MDI rA, rB, IMM",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "MDIM rA, rB, IMM",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "MDIS rA, rB, IMM",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "MDISM rA, rB, IMM",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "MDM rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "MDS rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "MDSM rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "MH rA, IMM",
    "feature": CF_CHG1 | CF_USE2
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
    "format": "ML rA, IMM",
    "feature": CF_CHG1 | CF_USE2
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
    "format": "MS rA, IMM",
    "feature": CF_CHG1 | CF_USE2
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
    "format": "MU rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "MUF rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "MUFM rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "MUI rA, rB, IMM",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "MUIM rA, rB, IMM",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "MUIS rA, rB, IMM",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "MUISM rA, rB, IMM",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "MUM rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "MUS rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "MUSM rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "NG rA, rB",
    "feature": CF_CHG1 | CF_USE2
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
    "format": "NGF rA, rB",
    "feature": CF_CHG1 | CF_USE2
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
    "format": "NGFM rA, rB",
    "feature": CF_CHG1 | CF_USE2
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
    "format": "NGM rA, rB",
    "feature": CF_CHG1 | CF_USE2
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
    "format": "NT rA, rB",
    "feature": CF_CHG1 | CF_USE2
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
    "format": "NTM rA, rB",
    "feature": CF_CHG1 | CF_USE2
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
    "format": "OR rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "ORI rA, rB, IMM",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "ORM rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "RE",
    "feature": CF_STOP
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
    "format": "RF rA",
    "feature": CF_CHG1
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
    "format": "RL rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "RLI rA, rB, IMM",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "RLIM rA, rB, IMM",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "RLM rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "RMP rA, rB",
    "feature": CF_CHG1 | CF_USE2
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
    "format": "RND rA",
    "feature": CF_CHG1
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
    "format": "RNDM rA",
    "feature": CF_CHG1
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
    "format": "RR rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "RRI rA, rB, IMM",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "RRIM rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "RRM rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "SA rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "SAI rA, rB, IMM",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "SAIM rA, rB, IMM",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "SAM rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "SB rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "SBC rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "SBCI rA, rB, IMM",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "SBCIM rA, rB, IMM",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "SBCM rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "SBF rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "SBFM rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "SBI rA, rB, IMM",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "SBIM rA, rB, IMM",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "SBM rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "SES rA, rB",
    "feature": CF_CHG1 | CF_USE2
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
    "format": "SEW rA, rB",
    "feature": CF_CHG1 | CF_USE2
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
    "format": "SF rA",
    "feature": CF_USE1
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
    "format": "SL rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "SLI rA, rB, IMM",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "SLIM rA, rB, IMM",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "SLM rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "SMP rA, rB, FLAGS",
    "feature": CF_USE1 | CF_USE2 | CF_USE3
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
    "format": "SR rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "SRI rA, rB, IMM",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "SRIM rA, rB, IMM",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "SRM rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "STSm rA, [rB + Offset, RegCount]",
    "feature": CF_USE1 | CF_CHG2
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
    "format": "STTm rA, [rB + Offset, RegCount]",
    "feature": CF_USE1 | CF_CHG2
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
    "format": "STWm rA, [rB + Offset, RegCount]",
    "feature": CF_USE1 | CF_CHG2
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
    "format": "WT",
    "feature": CF_STOP
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
    "format": "XR rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "XRI rA, rB, IMM",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "XRM rA, rB, rC",
    "feature": CF_CHG1 | CF_USE2 | CF_USE3
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
    "format": "ZES rA, rB",
    "feature": CF_CHG1 | CF_USE2
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
    "format": "ZEW rA, rB",
    "feature": CF_CHG1 | CF_USE2
  }
]

